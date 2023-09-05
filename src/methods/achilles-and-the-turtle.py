class AchillesAndTurtle:
    def __init__(self, name, speed, position) -> int:
        self.name = name
        self.speed = speed
        self.position = position

def race(achilles, turtle):
    for i in range(15):
        achilles.position -= achilles.speed
        turtle.position -= turtle.speed
        achilles.speed /= 2
        turtle.speed /= 2
        print(f'achilles is in: {achilles.position} and the turtle is in: {turtle.position}')

race(AchillesAndTurtle("Achille",10,25), AchillesAndTurtle("Tortue",5,15))