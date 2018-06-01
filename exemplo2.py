import cv2

classificator = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
classificatorOlhos = cv2.CascadeClassifier(
    './haarcascade_eye.xml')

imagem = cv2.imread('./pessoas/beatles.jpg', cv2.IMREAD_GRAYSCALE)

rostos = classificator.detectMultiScale(imagem)

for (x, y, l, a) in rostos:
    imagem = cv2.rectangle(imagem, (x, y), (x+l, y+a), (0, 255, 0), 2)
    regiao = imagem[y:y+a, x:x+l]
    olhosDetectados = classificatorOlhos.detectMultiScale(regiao)
    for (ox, oy, ol, oa) in olhosDetectados:
        cv2.rectangle(regiao, (ox, oy), (ox+ol, oy+oa), (255, 255, 0), 2)

cv2.imshow('Faces e olhoso', imagem)
cv2.waitKey()
