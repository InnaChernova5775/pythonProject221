from rectangle import Restangle, Square,Circle

rest_1= Restangle(3,4)
rest_2= Restangle(12,5)
print(rest_1.get_area())
print(rest_2.get_area())

square_1=Square(5)
square_2=Square(10)
print(square_1.get_area_square(),square_2.get_area_square())

circle_1= Circle(4)
circle_2= Circle(7)
print(circle_1.get_area_circle(),circle_2.get_area_circle())

figures=[rest_1, rest_2, square_1, square_2,circle_1,circle_2]

for figure in figures:
    if isinstance(figure,Square):
        print(figure.get_area_square())
    elif isinstance(figure,Circle):
        print(figure.get_area_circle())
    else:
        print(figure.get_area())



        print(figure.get_area())
