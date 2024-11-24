import argparse


def parse() -> tuple[str, str, str, int]:
    """
    Парсинг аргументов командной строки.
    :return: кортеж с ключевым словом для поиска, путем к папке для
    сохранения, путем к файлу аннтотации и количеством изображений
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword", type=str, help="keyword to search images")
    parser.add_argument("directory", type=str, help="path to the folder to download")
    parser.add_argument("annotation", type=str, help="path to the annotation file")
    parser.add_argument("number", type=int, help="number of images")
    args = parser.parse_args()
    return args.keyword, args.directory, args.annotation, args.number
