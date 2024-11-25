from annotation import create_annotation
from downloader import download_images
from iterator import ImageIterator
from parser import parse


def main():
    try:
        keyword, image_dir, csv_path, num = parse()
        download_images(keyword, image_dir, num)
        create_annotation(csv_path, image_dir)
        image_iterator = ImageIterator(csv_path)
        for image in image_iterator:
            print(image)
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
