import argparse
import re


def get_filename() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str, help="input the name of file")
    args = parser.parse_args()
    return args.filename


def read_data(filename: str) -> list[str]:
    try:
        with open(filename, mode="r", encoding="UTF-8") as file:
            data = file.readlines()
        return data
    except FileNotFoundError:
        print(f"File {filename} not found")


def find_people(data: list[str]) -> list[str]:
    forms = []
    for i in range(5, len(data) - 1, 8):
        number_pattern = re.search(r"(\+7|8)(\s?)(\(?)(927)", data[i])
        if number_pattern is not None:
            forms.append(data[i - 4] + data[i - 3] + data[i - 2] + data[i - 1] + data[i] + data[i + 1])
    return forms


def print_forms(forms: list[str]) -> None:
    for el in forms:
        print(el)


def main():
    filename = get_filename()
    data = read_data(filename)
    people = find_people(data)
    print_forms(people)


if __name__ == "__main__":
    main()
