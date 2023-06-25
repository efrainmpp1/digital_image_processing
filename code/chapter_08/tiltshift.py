import cv2
import numpy as np

def apply_tilt_shift(image, region_height, decay, center_position):
    # Converter a imagem para escala de cinza
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calcular o tamanho da região superior e inferior com base na altura da região central
    height, width = image.shape[:2]
    top_region_height = int(center_position - region_height / 2)
    bottom_region_height = int(center_position + region_height / 2)

    # Aplicar o desfoque na região superior
    blurred_top = cv2.GaussianBlur(image_gray[:top_region_height, :], (0, 0), sigmaX=decay)

    # Aplicar o desfoque na região inferior
    blurred_bottom = cv2.GaussianBlur(image_gray[bottom_region_height:, :], (0, 0), sigmaX=decay)

    # Combinar as regiões borradas e a região central nítida
    result = np.vstack((blurred_top, image_gray[top_region_height:bottom_region_height, :], blurred_bottom))

    # Converter a imagem resultante para colorida
    result = cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)

    # Retornar o resultado
    return result

# Carregar a imagem
image = cv2.imread("image.jpg")

# Definir os parâmetros iniciais
region_height = 200  # Altura da região central que entrará em foco
decay = 10  # Força de decaimento da região borrada
center_position = 300  # Posição vertical do centro da região que entrará em foco

# Aplicar o tilt shift na imagem
result = apply_tilt_shift(image, region_height, decay, center_position)

# Exibir a imagem resultante
cv2.imshow("Tilt Shift", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Salvar a imagem resultante em arquivo
cv2.imwrite("result.jpg", result)
