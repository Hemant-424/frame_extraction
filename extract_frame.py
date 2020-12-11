import cv2

capture_video = cv2.VideoCapture('video.mp4')   #video.mp4 is file with 30minutes duration
i=0
while(capture_video.isOpened()):
    ret, frame = capture_video.read()
    if ret == False:
        break

    cv2.imwrite('Hemant'+str(i)+'.jpg',frame)
    i += 1

capture_video.release()
capture_video.destroyAllWindows()
