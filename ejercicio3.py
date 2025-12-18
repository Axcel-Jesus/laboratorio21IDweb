class OperadorInvalidoError(Exception):
    def __init__(self, operador):
        super().__init__(f"Operador inválido: '{operador}'. Usa +, -, * o /")
operacion=input("Ingrese la operacion entre dos numeros que desee\n")
operacion=operacion.replace(',','.')
operacion=operacion.replace(' ','')
try:
    for operador in ['+','-','*','/']:
        if operador in operacion:
            num=operacion.split(operador)
            num1=float(num[0])
            num2=float(num[1])
            break
    if operador=='+':
        print("El resultado de la suma es: ",num1+num2)
    elif operador=='-':
        print("El resultado de la resta es: ",num1-num2)
    elif operador=='*':
        print("El resultado de la multiplicacion es: ",num1*num2)
    elif operador=='/':
        if num2==0:
            raise ZeroDivisionError
        else:
            print("El resultado de la division es: ",num1/num2)
    else:
        raise OperadorInvalidoError(operador)
except ZeroDivisionError:
    print("Error: Division por cero")
except ValueError as e:
    print("Error: No se puede convertir a numero")
except OperadorInvalidoError as e:
    print(f"Error de operador: {e}")
except Exception as e:
    print(f"Error: {e}")