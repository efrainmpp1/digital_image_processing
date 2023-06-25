import cv2

def display_image_with_negative_region(image, p1, p2):
    # Criar uma cópia da imagem
    result = image.copy()

    # Garantir que as coordenadas de P1 e P2 estejam dentro dos limites da imagem
    p1 = (max(0, min(p1[0], image.shape[1]-1)), max(0, min(p1[1], image.shape[0]-1)))
    p2 = (max(0, min(p2[0], image.shape[1]-1)), max(0, min(p2[1], image.shape[0]-1)))

    # Inverter as coordenadas para obter os pontos opostos do retângulo
    x_min, x_max = min(p1[0], p2[0]), max(p1[0], p2[0])
    y_min, y_max = min(p1[1], p2[1]), max(p1[1], p2[1])

    # Aplicar o negativo da imagem na região do retângulo
    result[y_min:y_max+1, x_min:x_max+1] = 255 - result[y_min:y_max+1, x_min:x_max+1]

    # Exibir a imagem resultante
    cv2.imshow("Imagem com Região Negativa", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Carregar a imagem
image = cv2.imread("bolhas.png", cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Não foi possível abrir a imagem.")
else:
    # Solicitar ao usuário as coordenadas de P1 e P2
    p1_x = int(input("Digite a coordenada X de P1: "))
    p1_y = int(input("Digite a coordenada Y de P1: "))
    p2_x = int(input("Digite a coordenada X de P2: "))
    p2_y = int(input("Digite a coordenada Y de P2: "))

    # Exibir a imagem com a região negativa
    display_image_with_negative_region(image, (p1_x, p1_y), (p2_x, p2_y))
