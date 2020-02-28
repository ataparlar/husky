#include <iostream>
#include <vector>
#include <ros/ros.h>
#include <opencv2/opencv.hpp>
#include <opencv2/aruco.hpp>

using namespace std;
using namespace cv;
using namespace aruco;

int main(int argc, char **argv)
{
	ros::init(argc, argv, "aruco_cpp");

	VideoCapture cap;
	Ptr<DetectorParameters> params = DetectorParameters::create();
	Ptr<Dictionary> dictionary = getPredefinedDictionary(DICT_5X5_250); 

	cap.open(0);

	if(!cap.isOpened())
	{
		cout << "Camera is not open!! Shutting down!!\n";
		return 1;
	}


	while(ros::ok())
	{
		Mat frame;
		vector<Point2f> corners;
		Mat ids;

		cap.read(frame);

		detectMarkers(frame, dictionary, corners, ids ,params);
		drawDetectedMarkers(frame, corners);

		imshow("frame", frame);

		ros::spinOnce();
		if(waitKey(1) == 27) //27 == esc
			break;
	}

	return 0;
}