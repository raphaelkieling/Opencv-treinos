import cv2

classificador = cv2.CascadeClassifier('./cars.xml')
video = cv2.VideoCapture(
    './Carros saltam em rodovia por causa de elevação.mp4')

while True:
    c, f = video.read()
    carrosEncontrados = classificador.detectMultiScale(
        cv2.cvtColor(f, cv2.COLOR_RGB2GRAY), 2.3,minNeighbors=3)

    for (x, y, l, a) in carrosEncontrados:
        cv2.rectangle(f, (x, y), (x+l, y+a), (0, 255, 0), 2)

    cv2.imshow("Video carros", f)
    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
