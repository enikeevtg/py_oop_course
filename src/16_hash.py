#16. Магические методы __eq__ и __hash__

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))


p1 = Point(1, 2)
p2 = Point(1, 2)
print(hash(p1), hash(p2), sep="\n")
# -3550055125485641917
# -3550055125485641917

d ={}
d[p1] = 1
d[p2] = 11
print(d)
# {<__main__.Point object at 0x7f42765cffd0>: 11}


# if __eq__ and __hash__ commented
# 8739374207025
# 8739374206989
# {<__main__.Point object at 0x7f2cb4b90310>: 1, <__main__.Point object at 0x7f2cb4b900d0>: 11}
