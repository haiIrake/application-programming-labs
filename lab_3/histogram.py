import cv2
import matplotlib.pyplot as plt
import numpy as np


def plot_histogram(image: np.ndarray) -> None:
    """
    Вычисляет и строит гистограмму для трех цветовых каналов изображения.
    :param image: изображение в формате numpy.ndarray
    """
    plt.figure(figsize=(10, 5))
    colors = ("blue", "green", "red")

    for i, col in enumerate(colors):
        histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(histogram, color=col)

    plt.title("histogram")
    plt.xlabel("intensity")
    plt.ylabel("frequency")
    plt.xlim([0, 256])
    plt.legend(colors)
    plt.show()
