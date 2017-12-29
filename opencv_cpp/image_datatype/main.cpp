#include <stdio.h>
#include <opencv2/opencv.hpp>
using namespace cv;


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

int main(int argc, char** argv )
{
  access_by_iterator();
  return 0;
}
