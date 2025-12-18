import ejercicio4geometria as geometria

try:
    figura=input("Ingrese la figura:\n1. rectangulo\n2. triangulo\n3. circulo\n")
    if figura=="1":
        base=float(input("Ingrese la base del rectangulo: "))
        altura=float(input("Ingrese la altura del rectangulo: "))
        rect=geometria.rectangulo(base,altura)
        print("Area del rectangulo: ",rect.area())
        print("Perimetro del rectangulo: ",rect.perimetro())
    elif figura=="2":
        base=float(input("Ingrese la base del triangulo: "))
        altura=float(input("Ingrese la altura del triangulo: "))
        tri=geometria.triangulo(base,altura)
        print("Area del triangulo: ",tri.area())
        print("Perimetro del triangulo: ",tri.perimetro())
    elif figura=="3":
        radio=float(input("Ingrese el radio del circulo: "))
        circ=geometria.circulo(radio)
        print("Area del circulo: ",circ.area())
        print("Perimetro del circulo: ",circ.perimetro())
    else:
        print("Figura no reconocida.")
except ValueError:
    print("Entrada invalida. Por favor ingrese numeros validos.")