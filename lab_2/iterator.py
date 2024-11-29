import csv


class ImageIterator:
    def __init__(self, annotation: str):
        self.images = []
        self.index = 0
        with open(annotation, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            for line in reader:
                abs_path = line[0]
                self.images.append(abs_path)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.images):
            image_path = self.images[self.index]
            self.index += 1
            return image_path
        else:
            raise StopIteration
