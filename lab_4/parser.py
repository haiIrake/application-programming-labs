import argparse


def parse() -> tuple[str, int, int]:
    """
    Парсинг аргументов командной строки.
    :return: кортеж с путем к файлу аннотации, максимальной шириной и максимальной высотой изображения
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("annotation", type=str, help="path to the annotation file")
    parser.add_argument("max_width", type=int, help="max width of image")
    parser.add_argument("max_height", type=int, help="max height of image")
    args = parser.parse_args()
    return args.annotation, args.max_width, args.max_height
