import cv2
import numpy as np
import math

SIDE = 256
PERIODOS = 4

# Criar uma matriz de zeros para a imagem
image = np.zeros((SIDE, SIDE), dtype=np.float32)

for i in range(SIDE):
    for j in range(SIDE):
        image[i, j] = 127 * math.sin(2 * math.pi * PERIODOS * j / SIDE) + 128

# Salvar a imagem em formato YML
ss_yml = f"senoide-{SIDE}.yml"
fs = cv2.FileStorage(ss_yml, cv2.FILE_STORAGE_WRITE)
fs.write("mat", image)
fs.release()

# Normalizar a imagem para o intervalo [0, 255]
image_normalized = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)

# Converter a imagem para o tipo de dados uint8
image_normalized_uint8 = image_normalized.astype(np.uint8)

# Salvar a imagem em formato PNG
ss_png = f"senoide-{SIDE}.png"
cv2.imwrite(ss_png, image_normalized_uint8)

# Exibir a imagem
cv2.imshow("Senoide", image_normalized_uint8)
cv2.waitKey(0)
cv2.destroyAllWindows()
