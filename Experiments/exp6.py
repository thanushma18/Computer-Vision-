import cv2

cap = cv2.VideoCapture("sample.mp4")

speed = 100    # Slow Motion
# speed = 30   # Normal Speed
# speed = 5    # Fast Motion

while cap.isOpened():

    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Video", frame)

    if cv2.waitKey(speed) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
