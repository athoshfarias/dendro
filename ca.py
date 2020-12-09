import cv2
import numpy as np

winName = 'Janela de Teste para o SOPT'
cv2.namedWindow(winName, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(winName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

img = cv2.imread("D9.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
suave = cv2.GaussianBlur(img, (7, 7), 0)
canny1 = cv2.Canny(suave, 20, 55)
canny2 = cv2.Canny(suave, 20, 31)
kernel = np.ones((5,5),np.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
resultado = np.vstack([
np.hstack([img, suave ]),
np.hstack([canny1, canny2])
])
cv2.imshow(winName, resultado)

cv2.waitKey(0)
