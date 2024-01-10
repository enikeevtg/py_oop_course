#19. Магические методы __iter__ и __next__

class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step  # см метод __next__

    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration


class FRange2D:
    def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):
        self.rows = rows
        self.frange = FRange(start, stop, step)

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < self.rows:
            self.value += 1
            return self.frange
            # return iter(self.frange)
        else:
            raise StopIteration


fr = FRange(0, 1, 0.5)
print(fr.__next__())
print(next(fr))
# 0.0
# 0.5

for el in fr:
    print(el)
# 0.0
# 0.5

for el in fr:
    print(el)
# 0.0
# 0.5

fr2d = FRange2D(0, 2, 0.5, 4)
for row in fr2d:
    for el in row:
        print(el, end=' ')
    print()
# 0.0 0.5 1.0 1.5
# 0.0 0.5 1.0 1.5
# 0.0 0.5 1.0 1.5
# 0.0 0.5 1.0 1.5
