class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if self.pointer > self.stop and self.step > 0:
            raise StopIteration()
        elif self.pointer < self.stop and self.step < 0:
            raise StopIteration()
        self.pointer += self.step
        return self.pointer - self.step


iter1 = Iterator(6, 15, 2)
for i in iter1:
    print(i, end=' ')

print()

iter2 = Iterator(10, 15)
for i in iter2:
    print(i, end=' ')

print()

try:
    iter3 = Iterator(10, 15, 0)
    for i in iter3:
        print(i, end=' ')
except StepValueError:
    print('Шаг не должен быть равен нулю')

iter4 = Iterator(-5, 1)
for i in iter4:
    print(i, end=' ')

print()

iter5 = Iterator(5, 1, -1)
for i in iter5:
    print(i, end=' ')

print()
