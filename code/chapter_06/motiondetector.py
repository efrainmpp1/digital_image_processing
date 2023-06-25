import cv2
import numpy as np

def calculate_histogram(image):
    # Converter a imagem para escala de cinza (caso necessário)
    if len(image.shape) > 2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calcular o histograma da imagem
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

    # Normalizar o histograma
    histogram = cv2.normalize(histogram, histogram)

    # Retornar o histograma normalizado
    return histogram

def compare_histograms(hist1, hist2):
    # Calcular a correlação de Pearson entre os histogramas
    correlation = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

    return correlation

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Câmera indisponível")
    exit()

threshold = 0.9  # Limiar de similaridade para ativar o alarme
previous_histogram = None

while True:
    ret, frame = cap.read()

    if not ret:
        print("Não foi possível capturar a imagem")
        break

    # Calcular o histograma da imagem atual
    current_histogram = calculate_histogram(frame)

    if previous_histogram is not None:
        # Comparar o histograma atual com o histograma anterior
        similarity = compare_histograms(current_histogram, previous_histogram)

        # Verificar se a diferença entre os histogramas ultrapassou o limiar
        if similarity < threshold:
            print("Alarme ativado!")

    # Atualizar o histograma anterior com o histograma atual
    previous_histogram = current_histogram

    # Exibir a imagem
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
