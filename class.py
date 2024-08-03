class cal:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def sum(self):
        return self.left + self.right
    def mul(self):
        return self.left * self.right

class better_cal(cal):
    def pow(self):
        return self.left ** self.right
    def mul(self):
        if self.left == 7 or self.right == 7:
            return 'Lucky Number!'
        else:
            return self.left * self.right
    
object_cal = cal(2, 10)

print(object_cal.sum())
print(object_cal.mul())

object_b_cal = better_cal(2, 10)
print(object_b_cal.pow())
object_b_cal.right = 7
print(object_b_cal.mul())
