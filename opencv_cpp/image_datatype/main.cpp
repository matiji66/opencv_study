#include <stdio.h>
#include <opencv2/opencv.hpp>
using namespace cv;
using namespace std;


void create_array()
{
  cv::Mat m = cv::Mat::eye( 10, 10, CV_32FC1 );
  printf(
        "Element (3,3) is %f\n",
        m.at<float>(3,3)
        );

  cv::Mat n = cv::Mat::eye( 10, 10, CV_32FC2 );
  printf(
  "Element (3,3) is (%f,%f)\n",
  n.at<cv::Vec2f>(3,3)[0],
  n.at<cv::Vec2f>(3,3)[1]
  );
}

void access_by_iterator()
{
  int sz[3] = { 4, 4, 4 };
  cv::Mat m( 3, sz, CV_32FC3 );
  cv::randu( m, -1.0f, 1.0f );
  // A three-dimensional array of size 4-by-4-by-4
  // fill with random numbers from -1.0 to 1.0
  float max = 0.0f;
  // minimum possible value of L2 norm
  cv::MatConstIterator_<cv::Vec3f> it = m.begin<cv::Vec3f>();
  while( it != m.end<cv::Vec3f>() ) {
    float len2 = (*it)[0]*(*it)[0]+(*it)[1]*(*it)[1]+(*it)[2]*(*it)[2];
    if( len2 > max ) max = len2;
    it++;
  }
  std::cout << max  << std::endl;
}

const std::string image_file_path = "/home/scott/Pictures/me.jpg";

int convert_to_CV_32FC1()
{
  /*
  Mat.convertTo: only convert the type. the value is not sacled properly.
  Eg:
  at location (3,3). when data type is uint8. the value is 13
  after convert to float32, the value is still 13. so, image can't display correctly.

  */
  cv::Mat img = cv::imread(image_file_path, CV_LOAD_IMAGE_GRAYSCALE);
  // cout<< CV_LOAD_IMAGE_ANYDEPTH << CV_LOAD_IMAGE_COLOR << CV_LOAD_IMAGE_GRAYSCALE<<endl;
  if (img.empty())
  {
    std::cout << "open file failed"<<std::endl;
    return -1;
  }
  cv::namedWindow("Example1", cv::WINDOW_AUTOSIZE);
  cv::imshow("Example1", img);
  cv::waitKey();
  cout << " R Type: "<< img.type()<< endl;
  cout << "at <3,3>: "<< int(img.at<uchar>(3,3)) << endl;

  cv::Mat img2;
  img.convertTo(img2, CV_32FC1);
  cout << "after conversion: "<<img2.at<float>(3,3) << endl;
  cv::imshow("Example1", img2);
  cv::waitKey();
  cout << "after conversion channel count: " << img2.channels()<<" Type: " << img2.type() << endl;

  cv::Mat img3;
  img2.convertTo(img3, CV_8UC1);
  cout << "after conversion 22: "<<int(img3.at<uchar>(3,3)) << endl;
  cv::imshow("Example1", img3);
  cv::waitKey();

  cv::destroyWindow("Example1");
  return 0;
}

int main(int argc, char** argv )
{
  convert_to_CV_32FC1();
  return 0;
}
