from typing import Iterator


class iterDemo(Iterator):
    def __init__(self) -> None:
        self.data = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.data > 5:
            raise StopIteration
        else:
            self.data += 1
            return self.data

a = iterDemo()
for x in a:
    print(x)