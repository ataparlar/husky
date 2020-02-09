#!/usr/bin/env python

import cv2
import numpy as np
import rospy
import cv2.aruco as aruco
import json
from std_msgs.msg import String


def load_camera_params(filename='/home/berkealgul/rover_20_ws/src/rover_20/rover_20_image/src/logi-g922-config.json'):
    with open(filename, 'r') as loadFile:
        data = json.load(loadFile)
        mtx = np.array(data['mtx'])
        dist = np.array(data['dist'])
    return mtx, dist

def main(mtx, dist):
    cap = cv2.VideoCapture(1)

    while not rospy.is_shutdown():
        ret, frame = cap.read()
        # operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Change grayscale
        aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_250)  # Use 5x5 dictionary to find markers
        parameters = aruco.DetectorParameters_create()  # Marker detection parameters
        # lists of ids and the corners beloning to each id
        corners, ids, rejected_img_points = aruco.detectMarkers(gray, aruco_dict,
                                                                parameters=parameters,
                                                                cameraMatrix=mtx,
                                                                distCoeff=dist)

        if np.all(ids is not None):  # If there are markers found by detector
            for i in range(0, len(ids)):  # Iterate in markers
                # Estimate pose of each marker and return the values rvec and tvec---different from camera coefficients
                #rvec, tvec, markerPoints = aruco.estimatePoseSingleMarkers(corners[i], 0.02, mtx, dist)
                #(rvec - tvec).any()  # get rid of that nasty numpy value array error
                aruco.drawDetectedMarkers(frame, corners)
                #aruco.drawAxis(frame, mtx, dist, rvec, tvec, 0.01)  # Draw Axis
        else:
            coordinatePublisher.Publish('-')

        if len(ids) == 2:
            w = frame.shape[1]
            h = frame.shape[0]
            x,y,r = find_center(corners[0])
            coordinatePublisher.publish(str(x) +","+ str(y) + "," + str(w) + "," + str(h))
            
            x,y,r = find_center(markers[1])
            coordinatePublisher1.publish(str(x) +","+ str(y) + "," + str(w) + "," + str(h))
         elif len(ids) == 1:
            w = frame.shape[1]
            h = frame.shape[0]
            x,y,r = find_center(corners[0])
            coordinatePublisher.publish(str(x) +","+ str(y) + "," + str(w) + "," + str(h))
         else:
            coordinatePublisher.Publish('-')
            coordinatePublisher1.Publish('-')

        cv2.imshow('frame', frame)

        key = cv2.waitKey(3) & 0xFF
        if key == ord('q'):  # Quit
            break

    cap.release()
    cv2.destroyAllWindows()

rospy.init_node('rover_detect_aruco')

mtx, dis = load_camera_params()
coordinatePublisher = rospy.Publisher('/px_coordinates', String, queue_size = 1)
coordinatePublisher1 = rospy.Publisher('/px_coordinates1', String, queue_size = 1)
main(mtx, dist)
