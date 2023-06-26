import cv2
import numpy as np

nClusters = 8
nRodadas = 1

if len(sys.argv) != 3:
    print("python kmeans.py entrada.jpg saida.jpg")
    sys.exit(0)

img = cv2.imread(sys.argv[1], cv2.IMREAD_COLOR)
samples = img.reshape(-1, 3).astype(np.float32)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10000, 0.0001)
flags = cv2.KMEANS_RANDOM_CENTERS

_, labels, centers = cv2.kmeans(samples, nClusters, None, criteria, nRodadas, flags)

centers = np.uint8(centers)
result = centers[labels.flatten()]
result = result.reshape(img.shape)

cv2.imshow("kmeans", result)
cv2.imwrite(sys.argv[2], result)
cv2.waitKey(0)
