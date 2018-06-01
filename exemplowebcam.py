import cv2

classificator = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
classificatorOlhos = cv2.CascadeClassifier(
    './haarcascade_eye.xml')
video = cv2.VideoCapture(0)

while True:
    conectado, frame = video.read()

    frameCinza = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    facesDetectadas = classificator.detectMultiScale(frameCinza)

    for (x, y, l, a) in facesDetectadas:
        imagem = cv2.rectangle(frame, (x, y), (x+l, y+a), (0, 255, 0), 2)
        regiao = imagem[y:y+a, x:x+l]
        olhosDetectados = classificatorOlhos.detectMultiScale(regiao)
        for (ox, oy, ol, oa) in olhosDetectados:
            cv2.rectangle(regiao, (ox, oy), (ox+ol, oy+oa), (255, 255, 0), 2)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
