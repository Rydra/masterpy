class Result:
    def __init__(self, black, white):
        self.black = black
        self.white = white

class Validator():
    def validate(self, solution, combination):
        black = 0
        for (slot1, slot2) in zip(solution, combination):
            black += 1 if slot1 == slot2 else 0

        return Result(black, 0)
