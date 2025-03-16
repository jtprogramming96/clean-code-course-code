class Point:
    def __init__(self, x, y):                                           # coordX y coordY no están mal, pero una versión más simple es x e y.
        self.x = x                                                      # Dado el contexto, se entiende que x e y son las coordenadas de un punto,
        self.y = y                                                      # y el prefijo coord es información redundante en este caso y por eso, se quita


class Rectangle:
    def __init__(self, origin, width, height):                          # origin es más simple que starting_point, que es más largo
        self.origin = origin
        self.width = width                                              # broad es amplitud, width es ancho
        self.height = height                                            # high es alto, height es altura

    def get_area(self):                                                 # area es un comando, por lo tanto es un método. Y los métodos son acciones, por eso renombramos get_area ya que es más adecuado
        return self.width * self.height
    
    def print_area(self):
        return print('Area: ' + str(self.get_area()))

    def end_points(self):
        end_point_coordX = self.origin.coordX + self.width
        end_point_coordY = self.origin.coordY + self.height
        print('Starting Point (X): ' + str(self.origin.coordX))
        print('Starting Point (Y): ' + str(self.origin.coordY))
        print('End Point (X): ' + str(end_point_coordX))
        print('End Point (Y): ' + str(end_point_coordY))


def build_rectangle():
    rectangle_origin = Point(50, 100)
    rectangle = Rectangle(rectangle_origin, 90, 10)

    return rectangle


rectangle = build_rectangle()                                           # jamás debes color nombres con prefijo mi: my_rectangle. Esta es una mala práctica promovida por muchos tutoriales no profesionales. Porqué mi? a quién pertenece? al desarrollador? al usuario final?

rectangle.print_area()
rectangle.end_points()
