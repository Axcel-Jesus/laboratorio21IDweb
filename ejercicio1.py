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

try:
    figura=input("Ingrese la figura:\n1. rectangulo\n2. triangulo\n3. circulo\n")
    if figura=="1":
        base=float(input("Ingrese la base del rectangulo: "))
        altura=float(input("Ingrese la altura del rectangulo: "))
        rect=rectangulo(base,altura)
        print("Area del rectangulo: ",rect.area())
        print("Perimetro del rectangulo: ",rect.perimetro())
    elif figura=="2":
        base=float(input("Ingrese la base del triangulo: "))
        altura=float(input("Ingrese la altura del triangulo: "))
        tri=triangulo(base,altura)
        print("Area del triangulo: ",tri.area())
        print("Perimetro del triangulo: ",tri.perimetro())
    elif figura=="3":
        radio=float(input("Ingrese el radio del circulo: "))
        circ=circulo(radio)
        print("Area del circulo: ",circ.area())
        print("Perimetro del circulo: ",circ.perimetro())
    else:
        print("Figura no reconocida.")
except ValueError:
    print("Entrada invalida. Por favor ingrese numeros validos.")