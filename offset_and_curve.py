import numpy as np
import cv2
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
class OffsetAndCurve:
    def curvature_radius(self, binary_warped, left_fitx, right_fitx):
        ym_per_pix = 30/720
        xm_per_pix = 3.7/800

        ploty = np.linspace(0, binary_warped.shape[0] - 1, binary_warped.shape[0])

        left_fitx = left_fitx[::-1]
        right_fitx = right_fitx[::-1]

        left_fit_cr = np.polyfit(ploty*ym_per_pix, left_fitx*xm_per_pix, 2)
        right_fit_cr = np.polyfit(ploty*ym_per_pix, right_fitx*xm_per_pix, 2)

        y_eval = np.max(ploty)

        left_curverad = (1+(2*left_fit_cr[0]*y_eval*ym_per_pix+left_fit_cr[1])**2)**(3/2)/np.absolute(2*left_fit_cr[0])
        right_curverad = (1+(2*right_fit_cr[0]*y_eval*ym_per_pix+right_fit_cr[1])**2)**(3/2)/np.absolute(2*right_fit_cr[0])

        return left_curverad, right_curverad

    def car_offset(self, img, left_fitx, right_fitx):
        xm_perpix = 3.7/800
        mid_imgx = img.shape[1]//2
        car_pos = (left_fitx[-1] + right_fitx[-1])/2
        offsetx = (mid_imgx - car_pos) * xm_perpix

        return offsetx

    def draw_trapazoid(self, img, undist, warped_img, left_fitx, right_fitx, ploty, Minv):
        warp_zero = np.zeros_like(warped_img).astype(np.uint8)
        color_warp = np.dstack((warp_zero, warp_zero, warp_zero))
        
        pts_left = np.array([np.transpose(np.vstack([left_fitx, ploty]))])
        pts_right = np.array([np.flipud(np.transpose(np.vstack([right_fitx, ploty])))])
        pts = np.hstack((pts_left, pts_right))
        
        color = (0, 255, 0)
        cv2.fillPoly(color_warp, np.int_([pts]), (0, 255, 0))

        newwarp = cv2.warpPerspective(color_warp, Minv, (img.shape[1], img.shape[0]))
        result = cv2.addWeighted(undist, 1, newwarp, 0.3, 0)
        return result
        
    def add_info(self, img, binary_warped, left_fitx, right_fitx):
        left_curvature_rad, right_curvature_rad = self.curvature_radius(binary_warped, left_fitx, right_fitx)
        offset = self.car_offset(img, left_fitx, right_fitx)

        out_img = img.copy()

        cv2.putText(out_img, 'Radius of Curvature(L) = {}m'.format(round(left_curvature_rad)), (60, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 5)
        cv2.putText(out_img, 'Radius of Curvature(R) = {}m'.format(round(right_curvature_rad)), (60, 110), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 5)
        if offset > 0:
            cv2.putText(out_img, 'Vehicle is {:.2f}m right of center'.format(np.absolute(offset)), (60, 160), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 5)
        if offset < 0:
            cv2.putText(out_img, 'Vehicle is {:.2f}m left of center'.format(np.absolute(offset)), (60, 160), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 5)

        return out_img	

