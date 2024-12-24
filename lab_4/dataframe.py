import cv2
import pandas as pd


def create_dataframe(csv_path: str) -> pd.DataFrame:
    """
    Создает дата фрейм из файла аннотации, считывает изображения и записывает их ширину, высоту и глубину,
    печатает статистическую информацию.
    :param csv_path: путь к файлу аннотации
    :return: дата фрейм, содержащий пути к изображениям и свойства изображений
    """
    try:
        df = pd.read_csv(csv_path, names=["absolute_path", "relative_path"])
        width = []
        height = []
        channels = []

        for img_path in df["absolute_path"]:
            img = cv2.imread(img_path)
            if img is not None:
                width.append(img.shape[1])
                height.append(img.shape[0])
                channels.append(img.shape[2])
            else:
                raise FileNotFoundError(f"Image could not be read from {img_path}")

        df["width"] = width
        df["height"] = height
        df["channels"] = channels
        stats = df[["width", "height", "channels"]].describe()
        print(stats)
        return df
    except FileNotFoundError:
        print(f"Annotation file not found at {csv_path}")


def filter_dataframe(df: pd.DataFrame, max_width: int, max_height: int) -> pd.DataFrame:
    """
    Фильтрует дата фрейм по максимальной ширине и максимальной высоте.
    :param df: дата фрейм
    :param max_width: максимальная ширина изображения
    :param max_height: максимальная высота изображения
    :return: отфильтрованный дата фрейм
    """
    return df[(df["width"] <= max_width) & (df["height"] <= max_height)]


def add_area_and_sort(df: pd.DataFrame) -> pd.DataFrame:
    """
    Добавляет столбец с площадью изображения и сортирует.
    :param df: дата фрейм
    :return: дата фрейм с новым столбцом, отсортированный по площади
    """
    df["area"] = df["width"] * df["height"]
    return df.sort_values("area")
