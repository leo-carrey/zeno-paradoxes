class Zeno:
    def __init__(self, distance) -> int:
        self.distance = distance

    def rock(self):
        for i in range(10):
            self.distance /= 2
            print(f'the stone is {self.distance} away from the tree')


Zeno(20).rock()
