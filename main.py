import cv2
from vehicle_detector import VehicleDetector

vd = VehicleDetector()

img = cv2.imread("test1.jpg")

boxes = vd.detect_vehicles(img)
cv2.imshow("cars", img)

cv2.waitKey(0)