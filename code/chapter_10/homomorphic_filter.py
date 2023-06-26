import cv2
import numpy as np

def homomorphic_filter(image, cutoff_freq, gamma_l, gamma_h, c):
    # Aplica a transformada de Fourier na imagem
    complex_image = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
    complex_image_shifted = np.fft.fftshift(complex_image)

    # Calcula o espectro de magnitude
    magnitude_spectrum = cv2.magnitude(complex_image_shifted[:,:,0], complex_image_shifted[:,:,1])
    magnitude_spectrum = np.log1p(magnitude_spectrum)

    # Aplica o filtro homomórfico no domínio da frequência
    rows, cols = image.shape
    center_row, center_col = rows // 2, cols // 2

    # Cria a matriz de filtro homomórfico
    filter_ = np.ones((rows, cols), dtype=np.float32)

    for i in range(rows):
        for j in range(cols):
            dist_squared = (i - center_row)**2 + (j - center_col)**2
            filter_[i, j] = (gamma_h - gamma_l) * (1 - np.exp(-c * dist_squared / cutoff_freq**2)) + gamma_l

    # Aplica o filtro no espectro de magnitude
    filtered_spectrum = magnitude_spectrum * filter_

    # Retorna ao domínio espacial realizando a transformada inversa
    filtered_complex = np.zeros(complex_image_shifted.shape, dtype=np.float32)
    filtered_complex[:,:,0] = np.expm1(filtered_spectrum)
    filtered_complex_shifted = np.fft.ifftshift(filtered_complex)
    filtered_image = cv2.idft(filtered_complex_shifted)
    filtered_image = cv2.magnitude(filtered_image[:,:,0], filtered_image[:,:,1])
    filtered_image = np.exp(filtered_image) - 1

    # Normaliza a imagem filtrada para exibição
    filtered_image = cv2.normalize(filtered_image, None, 0, 255, cv2.NORM_MINMAX)
    filtered_image = np.uint8(filtered_image)

    return filtered_image

# Carrega a imagem mal iluminada
image = cv2.imread('mal_iluminada.png', cv2.IMREAD_GRAYSCALE)

# Define os parâmetros do filtro homomórfico
cutoff_freq = 30
gamma_l = 0.3
gamma_h = 1.5
c = 1

# Aplica o filtro homomórfico na imagem
filtered_image = homomorphic_filter(image, cutoff_freq, gamma_l, gamma_h, c)

# Mostra a imagem original e a imagem filtrada
cv2.imshow('Original', image)
cv2.imshow('Filtrada', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
