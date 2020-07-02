class Circle:

    def __init__(self, radius = 1.0):
        if type(radius) != int and type(radius) != float:
            raise('Not a Number')
        self.radius = radius

    def get_area(self):
        return 3.142 * self.radius ** 2

    def get_perimeter(self):
        return 2 * 3.142 * self.radius
        
