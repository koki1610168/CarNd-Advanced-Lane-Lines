import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import glob

f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(24, 9))
f.tight_layout()

img1 = mpimg.imread('./camera_cal/calibration3.jpg')
print(img1.shape)
#plt.imshow(img)
#plt.show()

img2 = img1.copy()
print(img2.shape)
objpoints = []
imgpoints = []

objp = np.zeros((6*9, 3), np.float32)
objp[:, :2] = np.mgrid[0:9, 0:6].T.reshape(-1, 2)

gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

ret, corners = cv2.findChessboardCorners(gray, (9, 6), None)

if ret == True:
    imgpoints.append(corners)
    objpoints.append(objp)

    img1 = cv2.drawChessboardCorners(img1, (9, 6), corners, ret)
    ax1.axis('off')
    ax1.imshow(img1)


ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
undist = cv2.undistort(img2, mtx, dist, None, mtx)

ax2.axis('off')
ax2.imshow(img2)
ax3.axis('off')
ax3.imshow(undist)
plt.show()

