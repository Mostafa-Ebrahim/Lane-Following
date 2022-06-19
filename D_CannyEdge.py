from cv2 import cv2

def can(x):
    pass

def cannyedge(video):
    cv2.namedWindow('canny')
    cv2.createTrackbar('kernel','canny', 1, 10, can)
    cv2.createTrackbar('low_thresh','canny', 0, 255, can)
    cv2.createTrackbar('high_thresh','canny', 0, 255, can)

    while True:
        ret, frame = video.read()
        low_threshold = cv2.getTrackbarPos('low_thresh', 'canny')
        high_threshold = cv2.getTrackbarPos('high_thresh', 'canny')
        kernel = cv2.getTrackbarPos('kernel', 'canny')
        if kernel % 2 == 0:
            kernel += 1

        grey_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        blur_gray = cv2.GaussianBlur(grey_frame,(kernel, kernel),0)
        edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

        cv2.imshow('Edges', edges)
        if cv2.waitKey(10) & 0xFF == 27:
            break


    cv2.destroyAllWindows()

def main():
    video = cv2.VideoCapture('solidYellowLeft.mp4')
    # video = cv2.VideoCapture(0)

    cannyedge(video)

if __name__ == '__main__':
    main()