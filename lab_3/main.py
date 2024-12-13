from image import process_image
from parser import parse


def main():
    try:
        original_path, inverted_path = parse()
        process_image(original_path, inverted_path)
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
