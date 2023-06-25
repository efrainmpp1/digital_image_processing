import cv2

def swap_image_quadrants(image):
    # Obter as dimensões da imagem
    height, width = image.shape

    # Dividir a imagem em quatro quadrantes
    quadrant_1 = image[0:height//2, 0:width//2]
    quadrant_2 = image[0:height//2, width//2:width]
    quadrant_3 = image[height//2:height, 0:width//2]
    quadrant_4 = image[height//2:height, width//2:width]

    # Trocar os quadrantes em diagonal
    swapped_image = cv2.vconcat([cv2.hconcat([quadrant_4, quadrant_3]), cv2.hconcat([quadrant_2, quadrant_1])])

    return swapped_image

# Carregar a imagem
image = cv2.imread("bolhas.png", cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Não foi possível abrir a imagem.")
else:
    # Trocar os quadrantes em diagonal
    swapped_image = swap_image_quadrants(image)

    # Exibir a imagem resultante
    cv2.imshow("Imagem com Quadrantes Trocados", swapped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
