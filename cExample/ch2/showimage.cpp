#include <stdio.h>
#include <opencv/highgui.h>



void showImage(char* imageFile){
  IplImage* img = cvLoadImage( imageFile );
  cvNamedWindow( "Example1", CV_WINDOW_AUTOSIZE );
  cvShowImage( "Example1", img );
  cvWaitKey(0);
  cvReleaseImage( &img );
  cvDestroyWindow( "Example1" );
}

void showVideo(char* videofile){
  cvNamedWindow("Example2", CV_WINDOW_AUTOSIZE);
  CvCapture* capture = cvCreateFileCapture(videofile);
  IplImage* frame;
  while(1){
    frame = cvQueryFrame(capture);
    if(!frame) break;
    printf("show image..");
    cvShowImage("Example2", frame);
    char c = cvWaitKey(1);
    if(c==27) break;
  }
  cvReleaseCapture(&capture);
  cvDestroyWindow("Example2");
}


int main(int argc, char** argv){
  if(argc != 3){
    printf("Usage: exe video/image filepath\n");
    return -1;
  }
  if(argv[1] == "video")
    showVideo(argv[2]);
  else
    showImage(argv[2]);

}
