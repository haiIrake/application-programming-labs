import argparse


def parse() -> tuple[str, str]:
    """
    Парсинг аргументов командной строки.
    :return: кортеж с путем к файлу оригинального изображения и путем для сохранения инвертированного изображения
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("original_path", type=str, help="path to the original image")
    parser.add_argument("inverted_path", type=str, help="path to save inverted image")
    args = parser.parse_args()
    return args.original_path, args.inverted_path
