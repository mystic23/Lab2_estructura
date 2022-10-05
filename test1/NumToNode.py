from LinkedList import LinkedList
from random import randint

def rand_dig(digits:int):
    """
    Genera un numero aleatorio
    con exactamente digits digitos
    """
    n=""
    n+=str(randint(1,9))
    for i in range(digits-1):
        n+=str(randint(0,9))
    neg = randint(1,2)
    if neg==2:
        return int(n)*-1
    else:
        return int(n)

def numToNode(num: int):
    """
    Retorna una lista enlazada simple
    a base de un numero dado
    """
    print("num es ",num)
    num1 = LinkedList()
    n = False
    while num!=0:
        if(num<0):
            num*=-1
            n = True
        a_dig = num%10
        num1.InsertPTR(a_dig) # Agregan valores al inicio
        num = num//10
    if(n):
        num1.set_negative() # funcion para distinguirla como negativa
    return num1

def listToNum(list: LinkedList):
    """
    Retorna un numero a base de una
    lista enlazada simple
    """
    conv = ""
    value = 0
    P = list.PTR
    while(P!=None):
        conv+=str(P.data) # Usa string para concatenar
        P = P.next
    if(list.negative==True): # Vuelve entero y da signo
        value = -1*int(conv)
    else:
        value = int(conv)
    return value

def punto1():
    print("Insertar numero de digitos")
    digits = int(input())
    a = rand_dig(digits)
    b = rand_dig(digits)
    num1 = numToNode(a)
    num2 = numToNode(b)
    print(num1)
    print(num2)
    print("Resultado")
    """
    La estructura de operar dos numeros
    con igual signo es sencilla

    Sin embargo al tener un negativo, 
    procesos unitarios no son eficientes 
    excepto en la forma

    a-b 
    si |a|>|b|

    La siguiente función
    busca operar de esta forma
    alterando signos y orden

    Ejemplo:
    11-30 -> -(30-11)
    -11+30 -> 30-11 
    """
    show = 0
    if (a>0 and b>0) or (a<0 and b<0) or (abs(a)==abs(b)):
        # Casos base
        num1.sumalistas(num2)
        print(num1)
    else:
        # Cuando hay un negativo busca operar mayor sobre menor
        if abs(a)<abs(b) and b<0:
            num2.negative = False
            num1.set_negative()

            num2.sumalistas(num1)

            num2.set_negative()
            print(num2)
            show = 1
        elif abs(a)>abs(b) and a<0:
            num1.negative = False
            num2.set_negative()
            num1.sumalistas(num2)
            num1.set_negative()
            print(num1)
        elif abs(a)<abs(b) and a<0:
            num2.sumalistas(num1)
            print(num2)
            show = 2
        elif abs(a)>abs(b) and b<0:
            num1.sumalistas(num2)
            print(num1)
    if show==1:
        print(listToNum(num2))
    else:
        print(listToNum(num1))
def punto(a,b):
    """
    Funcion usada para
    dos numeros especificos
    a y b
    """
    num1 = numToNode(a)
    num2 = numToNode(b)
    print(num1)
    print(num2)
    print("Resultado")
    if (a>0 and b>0) or (a<0 and b<0) or (abs(a)==abs(b)):
        num1.sumalistas(num2)
        print(num1)
    else:
        if abs(a)<abs(b) and b<0:
            num2.negative = False
            num1.set_negative()

            num2.sumalistas(num1)

            num2.set_negative()
            print(num2)
        elif abs(a)>abs(b) and a<0:
            num1.negative = False
            num2.set_negative()
            num1.sumalistas(num2)
            num1.set_negative()
            print(num1)
        elif abs(a)<abs(b) and a<0:
            num2.sumalistas(num1)
            print(num2)
        elif abs(a)>abs(b) and b<0:
            num1.sumalistas(num2)
            print(num1)

punto1()

