import pickle  # export it into one file
import cv2     # opencv
import numpy as np  # handling numeric things


# camera settings
cam_id = 1 # change this accordingly
width, height = 1280, 720  # change this to image resolution


# initialize variables

cap = cv2.VideoCapture(cam_id)  # For Webcam  # video capturer
cap.set(3, width)  # set width
cap.set(4, height)  # set height
points = np.zeros((4, 2), int)  # Array to store clicked points x and y positions
counter = 0  # Counter to track the number of clicked points

def mousePoints(event, x, y, flags, params ):

    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        points[counter] = x, y # store the clicked points
        counter += 1 # increment counter
        print(f"Clicked Points: {points}")

def warp_image(img, points, size=[1280,720]):

    pts1 = np.float32(points) # convert points to float32
    pts2 = np.float32([[0, 0], [size[0], 0], [0, size[1]], [size[0], size[1]]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)  # Calculate perspective transformation matrix
    imgOutput = cv2.warpPerspective(img, matrix, (size[0], size[1]))  # Warp the image
    return imgOutput, matrix

f=0
while True:
    success, img = cap.read()

    if counter == 4:
        # save selected points in file
        fileObj = open("map.p", "wb")
        pickle.dump(points, fileObj)
        fileObj.close()
        if f==0:
            print("Points saved to file: map.p")
            f = 1

        # warp the image
        imgOutput, matrix = warp_image(img, points)
        # Display warped image
        cv2.imshow("Output Image ", imgOutput)

    # Draw circles at clicked points
    for x in range(0,4):
        cv2.circle(img, (points[x][0], points[x][1]), 3, (0, 255, 0), cv2.FILLED)
    cv2.imshow("Original Image", img)
    cv2.setMouseCallback("Original Image", mousePoints)
    cv2.waitKey(1) # Wit for key press

# Release resources

cap.release()
cv2.destroyAllWindows()


