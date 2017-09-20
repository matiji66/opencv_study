import cv2

from .managers import WindowManager,CaptureManager

VIDEO_FILE= "/home/scott/temp/opencv/pycv-master/first_edition/chapter2/miscellaneous/MyInputVid.avi"

class Cameo(object):
    def __init__(self):
        self._windowManager = WindowManager('Cameo',
        self.onKeypress) # pass a class method to another class, is this s problem?
        self._captureManger = CaptureManager(
                    cv2.VideoCapture(VIDEO_FILE),self._windowManager,True
                )

    def run(self):
        """Run the main loop"""
        # import pdb; pdb.set_trace()
        self._windowManager.createWindows()
        while self._windowManager.isWindowCreated():
            self._captureManger.enterFrame()
            frame = self._captureManger.frame
            # todo: Filter the frame
            self._captureManger.exitFrame()
            self._windowManager.processEvents()

    def onKeypress(self,keycode):
        """
        handle a keypress:
        space -> Take a screen shot
        tab   -> start/stop recording a screencast
        escape -> Quit
        """
        if keycode == 32: # space
            self._captureManger.writeImage("screenshot.png")
        elif keycode == 0: # tab
            if not self._captureManger.isWritingVideo:
                self._captureManger.startWritingVideo('screencast.avi')
            else:
                self._captureManger.stopWritingVideo()
        elif keycode == 27: # escape
            self._windowManager.destoryWindow()

if __name__ == "__main__":
    # import pdb; pdb.set_trace()
    myCameo = Cameo()
    myCameo.run()
