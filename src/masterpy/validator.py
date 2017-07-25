import itertools
class Result:
    def __init__(self, black, white):
        self.black = black
        self.white = white

class Validator():
    def validate(self, solution, combination):
        black = len(list(filter(lambda xy: xy[0] == xy[1], zip(solution, combination))))

        return Result(black, 0)
