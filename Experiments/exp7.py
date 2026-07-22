import cv2

cap = cv2.VideoCapture("Myvideo.avi")

speed = 100
# speed = 30
# speed = 5

while cap.isOpened():

    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Video", frame)

    if cv2.waitKey(speed) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
