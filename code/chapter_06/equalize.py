import cv2

def equalize_histogram(image):
    # Converter a imagem para escala de cinza (caso necessário)
    if len(image.shape) > 2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplicar a equalização do histograma
    equalized_image = cv2.equalizeHist(image)

    # Retornar a imagem equalizada
    return equalized_image

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Câmera indisponível")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Não foi possível capturar a imagem")
        break

    # Aplicar a equalização do histograma na imagem
    equalized_frame = equalize_histogram(frame)

    # Exibir a imagem equalizada
    cv2.imshow("Equalized Image", equalized_frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
