import cv2

classificador = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

imagem = cv2.imread('./pessoas/pessoas3.jpg')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)

facesDetectadas = classificador.detectMultiScale(imagemCinza,scaleFactor=1.3, minNeighbors=3)

print(len(facesDetectadas))

for (x, y, l, a) in facesDetectadas:
    print(x, y, l, a)
    cv2.rectangle(imagem, (x, y), (x+l, y+a), (0, 255, 0), 2)

cv2.imshow("Faces", imagem)
cv2.waitKey()
