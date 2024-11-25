import csv
import os


def create_annotation(csv_path: str, image_dir: str) -> None:
    """
    Создание файла аннотации с абсолютным и относительным путем к каждому изображению.
    :param csv_path: путь к файлу аннтотации
    :param image_dir: путь к папке с изображениями
    """
    with open(csv_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["absolute_path", "relative_path"])
        for image in os.listdir(image_dir):
            abs_path = os.path.abspath(os.path.join(image_dir, image))
            rel_path = os.path.relpath(abs_path, image_dir)
            writer.writerow([abs_path, rel_path])
