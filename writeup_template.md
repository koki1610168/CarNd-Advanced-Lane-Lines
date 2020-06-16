## Writeup Template

### You can use this file as a template for your writeup if you want to submit it as a markdown file, but feel free to use some other method and submit a pdf if you prefer.

---

**Advanced Lane Finding Project**

The goals / steps of this project are the following:

* Compute the camera calibration matrix and undistort the image
* Apply this camera calibration to test images
* Color Transofrm and Gradient
It took several hours to just find the right thresholds
* Apply a perspective transform to rectify binary image ("birds-eye view").
* Detect lane pixels and fit to find the lane boundary.
* Determine the curvature of the lane and vehicle position with respect to center.
* Warp the detected lane boundaries back onto the original image.
* Output visual display of the lane boundaries and numerical estimation of lane curvature and vehicle position.

[//]: # (Image References)

[image1]: ./undistort.png "Undistortion"
[image2]: ./color_gradient.png "Color Transformt and Gradient"
[image3]: ./warped_img.png "Warped Image"
[image4]: ./peak_finding.png "Find the peak on the image"
[image5]: ./find_lane.png "Apply window on the image"
[image6]: ./final_img.png "Final Image"
[video1]: ./project_video_output.mp4 "Video"

## [Rubric](https://review.udacity.com/#!/rubrics/571/view) Points

### Here I will consider the rubric points individually and describe how I addressed each point in my implementation.  

---

### Camera Calibration and Undistortion
Since a camera distorts a image it took, so we need to undistort the image to have a correct information.
![alt_text][image1]

### Color Transform and Gradient
Transform color to reduce the size of the image. Apply gradient to detect lanes clearly and reduce noises.
![alt text][image2]

### Warp Image
![alt text][image3]

### Peak Finding
Preprocessing for fiding line 
![alt text][image4]

### Apply Window for fidning lane
!{alt text][image5]

### Final Image
![alt text][image6]

### Final Video
![alt text][video1]
