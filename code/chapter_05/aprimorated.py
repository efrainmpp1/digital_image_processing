import cv2
import numpy as np

def count_bubbles(image):
    # Copiar a imagem original para preservar os dados originais
    labeled_image = image.copy()

    # Definir valores para os rótulos dos objetos e dos buracos
    object_label = 1
    hole_label = -1

    # Marcar os objetos que tocam as bordas da imagem
    height, width = image.shape
    border_label = np.zeros((height, width), dtype=np.uint8)
    border_label[0, :] = border_label[:, 0] = border_label[height-1, :] = border_label[:, width-1] = 1

    # Percorrer a imagem para rotular os objetos e os buracos
    for i in range(height):
        for j in range(width):
            if labeled_image[i, j] == 255:
                # Achou um objeto
                if border_label[i, j] == 0:
                    # Se o objeto não toca a borda, rotular como objeto
                    cv2.floodFill(labeled_image, None, (j, i), object_label)
                    object_label += 1
                else:
                    # Se o objeto toca a borda, rotular como buraco
                    cv2.floodFill(labeled_image, None, (j, i), hole_label)
                    hole_label -= 1

    # Contar o número de objetos excluindo os buracos
    n_objects = object_label - 1

    return labeled_image, n_objects

# Carregar a imagem
image = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)

# Aplicar um limiar para binarizar a imagem (caso necessário)
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Realizar a contagem de bolhas
labeled_image, n_objects = count_bubbles(binary_image)

# Exibir os resultados
cv2.imshow('Original Image', image)
cv2.imshow('Labeled Image', labeled_image)
print('Número de Bolhas:', n_objects)

cv2.waitKey(0)
cv2.destroyAllWindows()
