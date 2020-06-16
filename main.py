from moviepy.editor import VideoFileClip
from IPython.display import HTML
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

from camera_calibration import CameraPreprocessing
from color_and_gradient import ColorAndGradient
from warp_find_lane import WarpAndFindLane
from find_lane_pixels import FindLanePixels
from offset_and_curve import OffsetAndCurve

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 9))
fig.tight_layout()

def process_img(image):
    chess_board_imgs = os.listdir('camera_cal')

    prepro = CameraPreprocessing(chess_board_imgs)
    undistorted_img = prepro.undistort(image)

    cg = ColorAndGradient(undistorted_img)
    cg_comb_binary = cg.combined()

    warping = WarpAndFindLane(cg_comb_binary)
    warped_img, M, Minv = warping.warp()

    histogram = warping.hist(warped_img/255)

    find_pix = FindLanePixels(warped_img)
    left_fit, right_fit, left_fitx, right_fitx, ploty, out_img = find_pix.fit_polynomial()
    leftx, rightx, result, ploty = find_pix.search_around_poly()

    options = OffsetAndCurve()
    left_curverad, right_curverad = options.curvature_radius(warped_img, left_fitx, right_fitx)
    offsetx = options.car_offset(image, left_fitx, right_fitx)

    img_lane = options.draw_trapazoid(image, undistorted_img, warped_img, left_fitx, right_fitx, ploty, Minv)
    out_img = options.add_info(img_lane, warped_img, left_fitx, right_fitx)

    return out_img

video = 'project_video.mp4'
output_video = 'project_video_output.mp4'
clip1 = VideoFileClip(video)
white_clip = clip1.fl_image(process_img)
white_clip.write_videofile(output_video, audio=False)

#image = mpimg.imread('test_images/test2.jpg')
#out_img = process_img(image)

#ax1.imshow(image)
#ax1.axis('off')
#ax1.set_title('Original image', fontsize=50)


#ax2.imshow(out_img)
#ax2.axis('off')
#ax2.set_title('Processed image', fontsize=50)
#plt.show()
