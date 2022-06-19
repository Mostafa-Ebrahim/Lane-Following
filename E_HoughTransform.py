from cv2 import cv2
import numpy as np


def can(x):
    pass


def houghtransform(video):
    cv2.namedWindow('canny')
    cv2.createTrackbar('kernel', 'canny', 7, 10, can)
    cv2.createTrackbar('low_thresh', 'canny', 150, 255, can)
    cv2.createTrackbar('high_thresh', 'canny', 200, 255, can)
    cv2.createTrackbar('min_line_length', 'canny', 40, 50, can)
    cv2.createTrackbar('max_line_gap', 'canny', 20, 25, can)
    cv2.createTrackbar('rho', 'canny', 2, 5, can)
    cv2.createTrackbar('threshold', 'canny', 15, 20, can)

    while True:
        ret, frame = video.read()
        if ret == 0:
            main()

        low_threshold = cv2.getTrackbarPos('low_thresh', 'canny')
        high_threshold = cv2.getTrackbarPos('high_thresh', 'canny')
        kernel = cv2.getTrackbarPos('kernel', 'canny')
        min_line_length = cv2.getTrackbarPos('min_line_length', 'canny')
        max_line_gap = cv2.getTrackbarPos('max_line_gap', 'canny')
        rho = cv2.getTrackbarPos('rho', 'canny')
        threshold = cv2.getTrackbarPos('threshold', 'canny')
        theta = np.pi / 180
        if kernel % 2 == 0:
            kernel += 1
        if rho == 0:
            rho += 1

        grey_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        blur_gray = cv2.GaussianBlur(grey_frame, (kernel, kernel), 0)
        edges = cv2.Canny(blur_gray, low_threshold, high_threshold)
        line_image = np.zeros_like(frame)

        shape = frame.shape
        mask = np.zeros_like(edges)
        vertices = np.array([[(0, shape[0]), (450, 290), (490, 290), (shape[1], shape[0])]], dtype=np.int32)
        cv2.fillPoly(mask, vertices, 255)
        masked_edges = cv2.bitwise_and(edges, mask)

        lines = cv2.HoughLinesP(masked_edges, rho, theta, threshold, np.array([]),
                                min_line_length, max_line_gap)

        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(line_image, (x1, y1), (x2, y2), (200, 0, 0), 10)

        color_edges = np.dstack((edges, edges, edges))
        combo = cv2.addWeighted(color_edges, 0.8, line_image, 1, 0)
        cv2.imshow('Edges', combo)
        if cv2.waitKey(10) & 0xFF == 27:
            break


def main():
    video = cv2.VideoCapture('solidYellowLeft.mp4')
    houghtransform(video)


if __name__ == '__main__':
    main()
