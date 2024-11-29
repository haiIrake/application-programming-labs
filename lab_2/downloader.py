from icrawler.builtin import GoogleImageCrawler
import os


def download_images(keyword: str, image_dir: str, num: int) -> None:
    """
    Сохранение изображений из Google в указанную директорию.
    :param keyword: ключевое слово для поиска
    :param image_dir: путь к папке для сохранения
    :param num: количество изображений
    """
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
    google_crawler = GoogleImageCrawler(storage={"root_dir": image_dir},
                                        downloader_threads=4,
                                        parser_threads=4)
    google_crawler.crawl(keyword, max_num=num)
