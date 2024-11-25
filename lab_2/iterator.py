class ImageIterator:
    def __init__(self, annotation: str):
        self.annotation = annotation
        self.file = open(annotation, "r", encoding="utf-8")
        next(self.file)

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if line:
            return line.split(",")[0]
        else:
            raise StopIteration
