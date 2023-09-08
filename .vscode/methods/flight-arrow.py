class Arrow:
    def __init__(self, distance, speed) -> int:
        self.distance = distance
        self.speed = speed


def run(arrow):
    while True:
        arrow.distance -= arrow.speed
        print(f'the arrow is {arrow.distance} away from the target')
        if arrow.distance <= 0:
            break


run(Arrow(50, 10))
