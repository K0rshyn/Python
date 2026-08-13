class turtle(object):
    def __init__(self, s, y = 0, x = 0):
        self.absciss = x
        self.ordinat = y
        self.length = s

    def go_up(self):
        self.ordinat += self.length

    def go_down(self):
        self.ordinat -= self.length

    def go_left(self):
        self.absciss -= self.length

    def go_right(self):
        self.absciss += self.length

    def evolve(self):
        self.length += 1

    def degrade(self):
        if self.length - 1 <= 0:
            raise ValueError("Шаг не может быть меньше или равен 0")
        self.length -= 1
    def count_moves(self, x2, y2):
        dx = abs(x2 - self.absciss)
        dy = abs(y2 - self.ordinat)

        if dx == 0 and dy == 0:
            return 0

        max_s = max(self.length, dx, dy) + 1

        best = float('inf')

        for new_s in range(1, max_s + 1):
            if dx % new_s == 0 and dy % new_s == 0:
                change_steps = abs(new_s - self.length)
                move_steps = dx // new_s + dy // new_s
                total = change_steps + move_steps
                if total < best:
                    best = total

        return -1 if best == float('inf') else best
t = turtle(0, 0, 1)
print(t.count_moves(3, 3))  

        