import cv2
import numpy as np

def calculate_laplacian_of_gaussian(image):
    # Converter a imagem para escala de cinza
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplicar o filtro de Gaussiano na imagem em escala de cinza
    blurred = cv2.GaussianBlur(image_gray, (3, 3), 0)

    # Calcular o Laplaciano da imagem filtrada
    laplacian = cv2.Laplacian(blurred, cv2.CV_64F)

    # Converter a imagem de ponto flutuante para inteiro de 8 bits
    laplacian = cv2.convertScaleAbs(laplacian)

    # Retornar o resultado
    return laplacian

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Câmera indisponível")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Não foi possível capturar a imagem")
        break

    # Calcular o Laplaciano do Gaussiano da imagem atual
    laplacian = calculate_laplacian_of_gaussian(frame)

    # Exibir a imagem resultante
    cv2.imshow("Laplacian of Gaussian", laplacian)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
