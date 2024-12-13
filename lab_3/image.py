import cv2
import matplotlib.pyplot as plt
from histogram import plot_histogram


def process_image(original_path: str, inverted_path: str) -> None:
    """
    Считывает изображение, отображает его и его инверсию и сохраняет инверсию.
    :param original_path: путь к файлу оригинального изображения
    :param inverted_path: путь для сохранения инвертированного изображения
    """
    image = cv2.imread(original_path)
    if image is None:
        raise FileNotFoundError(f"Image could not be read from {original_path}")

    print(f"Image size: {image.shape[1]}x{image.shape[0]}")
    plot_histogram(image)
    inverted_image = cv2.bitwise_not(image)
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.title("original")
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.title("inverted")
    plt.imshow(cv2.cvtColor(inverted_image, cv2.COLOR_BGR2RGB))
    plt.axis("off")

    plt.show()
    if not cv2.imwrite(inverted_path, inverted_image):
        raise OSError(f"Image could not be saved to {inverted_path}")
