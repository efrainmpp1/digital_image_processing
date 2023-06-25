import cv2
import numpy as np

def apply_laplacian(image):
    # Converter a imagem para escala de cinza
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplicar o filtro Laplaciano na imagem em escala de cinza
    laplacian = cv2.Laplacian(image_gray, cv2.CV_64F)

    # Converter a imagem de ponto flutuante para inteiro de 8 bits
    laplacian = cv2.convertScaleAbs(laplacian)

    # Retornar o resultado
    return laplacian

def apply_laplacian_of_gaussian(image):
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

# Carregar a imagem
image = cv2.imread("image.jpg")

# Aplicar o filtro Laplaciano
laplacian = apply_laplacian(image)

# Aplicar o filtro Laplaciano do Gaussiano
laplacian_of_gaussian = apply_laplacian_of_gaussian(image)

# Exibir as imagens resultantes
cv2.imshow("Laplacian", laplacian)
cv2.imshow("Laplacian of Gaussian", laplacian_of_gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()
