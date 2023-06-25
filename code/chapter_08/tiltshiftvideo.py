import cv2
import numpy as np

def apply_tilt_shift(frame, region_height, decay, center_position):
    # Converter o quadro para escala de cinza
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calcular o tamanho da região superior e inferior com base na altura da região central
    height, width = frame.shape[:2]
    top_region_height = int(center_position - region_height / 2)
    bottom_region_height = int(center_position + region_height / 2)

    # Aplicar o desfoque na região superior
    blurred_top = cv2.GaussianBlur(frame_gray[:top_region_height, :], (0, 0), sigmaX=decay)

    # Aplicar o desfoque na região inferior
    blurred_bottom = cv2.GaussianBlur(frame_gray[bottom_region_height:, :], (0, 0), sigmaX=decay)

    # Combinar as regiões borradas e a região central nítida
    result = np.vstack((blurred_top, frame_gray[top_region_height:bottom_region_height, :], blurred_bottom))

    # Converter a imagem resultante para colorida
    result = cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)

    # Retornar o resultado
    return result

# Definir os parâmetros do efeito tilt-shift
region_height = 200  # Altura da região central que entrará em foco
decay = 10  # Força de decaimento da região borrada
center_position = 300  # Posição vertical do centro da região que entrará em foco

# Abrir o arquivo de vídeo de entrada
input_video = cv2.VideoCapture("input_video.mp4")

# Obter as informações do vídeo de entrada
frame_width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = input_video.get(cv2.CAP_PROP_FPS)

# Criar o objeto de gravação do vídeo de saída
output_video = cv2.VideoWriter("output_video.mp4", cv2.VideoWriter_fourcc(*"mp4v"), fps, (frame_width, frame_height))

# Processar cada quadro do vídeo de entrada
while input_video.isOpened():
    ret, frame = input_video.read()

    if not ret:
        break

    # Aplicar o efeito tilt-shift no quadro
    result = apply_tilt_shift(frame, region_height, decay, center_position)

    # Escrever o quadro processado no vídeo de saída
    output_video.write(result)

    # Exibir o quadro processado em uma janela
    cv2.imshow("Tilt Shift", result)

    # Definir a taxa de descarte de quadros para evidenciar o efeito stop motion
    # Você pode ajustar essa taxa conforme desejado
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Liberar os objetos de vídeo
input_video.release()
output_video.release()

# Fechar todas as janelas
cv2.destroyAllWindows()
