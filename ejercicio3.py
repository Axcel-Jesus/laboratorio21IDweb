operacion=input("Ingrese la operacion entre dos numeros que desee\n")
try:
    num1=float(operacion.split()[0])
    num2=float(operacion.split('/','+','*','-')[1])
    operacion=operacion.replace(str(num1),'').replace(str(num2),'')
    if operacion=='+':10
        print("El resultado de la suma es: ",num1+num2)
    elif operacion=='-':
        print("El resultado de la resta es: ",num1-num2)
    elif operacion=='*':
        print("El resultado de la multiplicacion es: ",num1*num2)
    elif operacion=='/':
        if num2==0:
            print("Error: Division por cero no permitida.")
        else:
            print("El resultado de la division es: ",num1/num2)
    else:
        print("Operacion no reconocida.")
except ValueError:
    print("Entrada invalida. Por favor ingrese una operacion valida.")

      