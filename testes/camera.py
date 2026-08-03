import cv2

cap = cv2.VideoCapture(0)

while cv2.waitKey(1) & 0xFF != ord('q'):

    success, frame = cap.read()

    if not success: break

    cv2.imshow("Camera", frame)

cap.release()
cv2.destroyAllWindows()