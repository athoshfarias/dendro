import cv2
import numpy as np

winName = 'Janela de Teste para o SOPT'
cv2.namedWindow(winName, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(winName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

img = cv2.imread("D9.jpg")
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
suave = cv2.GaussianBlur(img, (7, 7), 0)
bordas = cv2.Canny(suave, 20, 30)

#encontrar contorno Para OpenCV4 [ctns esta armazenando muitos contornos falsos]
ctns, _ = cv2.findContours(bordas, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, ctns, -1, (0,0,255), 2)
texto = 'Contornos encontrados: '+ str(len(ctns))
cv2.putText(img, texto, (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
  (255, 0, 0), 1)



#cv2.imshow('Imagem', bordas)
#cv2.imshow('Imagem2', img)
#cv2.imshow('Imagem3', suave)

resultado = np.vstack([
np.hstack([img, suave])
])

cv2.imshow(winName, resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()
