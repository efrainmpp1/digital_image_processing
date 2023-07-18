import cv2
import numpy as np

def enhance_canny_points(image, canny_image, point_radius):
    # Cria uma cópia da imagem original para desenhar os pontos
    enhanced_image = image.copy()

    # Encontra os pixels de borda na imagem de Canny
    edges = np.argwhere(canny_image > 0)

    # Desenha os pontos grandes nas posições dos pixels de borda
    for edge in edges:
        x, y = edge[0], edge[1]
        cv2.circle(enhanced_image, (y, x), point_radius, (0, 0, 0), -1)

    return enhanced_image

# Carrega a imagem pontilhista básica
points_image = cv2.imread('../chapter_08/valorant.png', cv2.IMREAD_GRAYSCALE)

# Aplica o algoritmo de Canny para detectar bordas
canny_image = cv2.Canny(points_image, 50, 150)

# Define o tamanho dos pontos a serem desenhados
point_radius = 3

# Melhora a imagem pontilhista utilizando as bordas de Canny
enhanced_image = enhance_canny_points(points_image, canny_image, point_radius)

# Mostra a imagem pontilhista original e a imagem melhorada
cv2.imshow('Pontos Original', points_image)
cv2.imshow('Pontos Melhorada', enhanced_image)
cv2.imwrite('resultado.png',enhanced_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
