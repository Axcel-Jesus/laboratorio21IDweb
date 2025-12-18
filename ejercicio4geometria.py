class figuras:
    def area(self):
        pass
    def perimetro(self):
        pass
class rectangulo(figuras):
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def area(self):
        return self.base*self.altura
    def perimetro(self):
        return 2*(self.base+self.altura)
class triangulo(figuras):
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def area(self):
        return (self.base*self.altura)/2
    def perimetro(self):
        return base+2*((self.base/2)**2+self.altura**2)**0.5
class circulo(figuras):
    def __init__(self,radio):
        self.radio=radio
    def area(self):
        return 3.14*self.radio*self.radio
    def perimetro(self):
        return 2*3.14*self.radio
