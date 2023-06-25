import cv2
import numpy as np
import sys

nbits = 3

# Verificar se o nome do arquivo de imagem foi fornecido como argumento de linha de comando
if len(sys.argv) < 2:
    print("É necessário fornecer o nome da imagem resultante da esteganografia.")
    print("Exemplo de uso: python recover_image.py esteganografia.png")
    sys.exit(1)

# Carregar a imagem resultante da esteganografia
imagem_resultante = cv2.imread(sys.argv[1], cv2.IMREAD_COLOR)

if imagem_resultante is None:
    print("Não foi possível carregar a imagem resultante da esteganografia.")
    sys.exit(1)

# Criar uma matriz de zeros para a imagem recuperada
imagem_recuperada = np.zeros_like(imagem_resultante)

for i in range(imagem_resultante.shape[0]):
    for j in range(imagem_resultante.shape[1]):
        val_resultante = imagem_resultante[i, j]
        val_recuperada = np.zeros(3, dtype=np.uint8)

        for k in range(3):
            val_resultante[k] = val_resultante[k] << (8 - nbits) >> (8 - nbits)
            val_recuperada[k] = val_resultante[k] << (8 - nbits)

        imagem_recuperada[i, j] = val_recuperada

filename = 'imagem_recuperada.png'

cv2.imwrite(filename, imagem_recuperada)
# Exibir a imagem recuperada
cv2.imshow("Imagem Recuperada", imagem_recuperada)
cv2.waitKey(0)
cv2.destroyAllWindows()
