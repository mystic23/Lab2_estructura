from Nodo import Nodo

class LinkedList:
    def __init__(self) -> None:
        self.PTR = None
        self.ULT = None
        self.negative = False

    def invertir(self):
        """
        Invierte el sentido de los enlaces
        """
        prev: Nodo = None
        current: Nodo = self.PTR
        next: Nodo = None
        while(current!=None):
            next = current.next
            if(current==self.PTR):
                self.ULT = current
            elif (current.next==None):
                self.PTR = current
            current.next = prev # El actual ahora se conecta con el anterior
            prev = current
            current = next # Seguir recorriendo

    def addNode(self, data)->None:
        """
        Adds node at last position
        """
        P = Nodo(data)
        if self.PTR == None:
            self.PTR = P
            self.ULT = P
        else:
            self.ULT.next= P
            self.ULT = P
    def numToNode(num: int):
        print("num es ",num)
        num1 = LinkedList()
        n = False
        while num!=0:
            if(num<0):
                num*=-1
                n = True
            a_dig = num%10
            num1.InsertPTR(a_dig)
            num = num//10
        if(n):
            num1.set_negative()
            print("negativo")
        return num1

    def listToNum(list: object):
        conv = ""
        value = 0
        P = list.PTR
        while(P!=None):
            conv+=str(P.data)
            P = P.next
        if(list.negative==True):
            value = -1*int(conv)
        else:
            value = int(conv)
        return value


    def sumalistas(self, a): 
        self.invertir()
        a.invertir()
        # Invierten para trabajar desde unidades mas pequeñas
        P1 = self.PTR
        P2 = a.PTR
        sobrante = 0
        suma = 0
        desc = False # booleano para reducir valor cuando se "presta"
        desc2 = False
        while P1!=None:
            
            if desc:
                if P1.data==0:  # 0 vuelve 9
                    P1.data=9
                    desc2 = True # para esto el 0 debe prestar 
                else:
                    P1.data-=1 # otros reducen en 1

            if a.negative and (self.negative is False): # Asumo a-b, abs(a)>abs(b)
                if P2.data>P1.data:   # 0-1   -> 10-1
                    desc = True
                    P1.data+=10 # prestamo
                elif desc2:
                    desc = True
                else:
                    desc = False
                suma = P1.data-P2.data
            else:
                suma = P1.data + P2.data
            suma = suma + sobrante # Si hay sobrante pasado agrega
            sobrante = 0 
            if suma>=10: 
                sum = suma%10
                sobrante = suma//10
                P1.data = str(sum)
                #Guarda suma en lista y sobrante para siguiente operación
            else:
                P1.data = str(abs(suma))
            P1 = P1.next
            P2 = P2.next
            # Avanzan por Nodos
        if sobrante>0:
            # Si quedo sobrante aumenta tamaño de lista
            self.addNode(sobrante)
        self.invertir() # Regresa lista a orden original

    def DeleteNode(self, data):
        """
        Deletes instance of Node with data
        replaces PTR but not ULT
        """
        if (self.PTR == None):
            print("Empty list")
        anteP = None
        P = self.PTR
        while(P != None):
            if (self.PTR.data == data):
                self.PTR = P.next
                del P
                P = self.PTR
            else:
                while(P != None and P.data != data):
                    anteP = P
                    P = P.next
                if (P != None and P.data == data):
                    anteP.next = P.next
                    P.next = None
                    del P
                    P = anteP.next
                else:
                    print("dato no en lista") 

    
    def __repr__(self) -> str:
        if self.negative==True:
            s ="-"
        else:
            s=""
        P = self.PTR
        while(P != None):
            s= s+str(P.data)+"->"
            P = P.next
        s=s+"None"
        return s

    def InsertPTR(self, data):
        """
        Adds node as PTR
        """
        if self.PTR == None:
            self.addNode(data)
        else :
            Q = Nodo(data)
            P = self.PTR
            self.PTR = Q
            Q.next = P
            
    def set_negative(self):
        self.negative = True

    def len(self):
        """
        devuelve numero de elementos en la lista
        """
        i=0
        P = self.PTR
        while(P!=None):
            P = P.next
            i+=1
        return i
