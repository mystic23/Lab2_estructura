from Nodo import Nodo

class LinkedList:
    def __init__(self):
        self.PTR = None
        self.ULT = None

    def AddNode(self,data, list):
        """"
        Adds a Node with a Barrio with data and list
        """
        P = Nodo(data, list)
        if (self.PTR == None):
            self.PTR = P
            self.ULT = P 
        else:
            self.ULT.next = P
            self.ULT = P  

    def Recorrido(self):
        P = self.PTR
        while(P != None):
            print(P.Barrio, end="->")
            P = P.next
        print("None")
    
    def __repr__(self):
        respuesta = ""
        P = self.PTR
        while(P != None):
            respuesta = respuesta + str(P.Barrio)+"->"
            P = P.next
        respuesta = respuesta + "None"
        return respuesta

    def search(self, prim: str, sec: str, ter: str):
        """
        Devuelve lista con Barrios que cumplen con preferencias
        """
        ls =[] # Lista principal
        ls1=[]
        ls2=[]
        ls3=[]
        # Listas para cada caso en orden de importancia
        N = self.PTR
        while(N!=None): # Recorriendo Nodos de LinkedList
            P = N.Barrio
            p1 = getattr(P,prim)
            p2 = getattr(P,sec)
            p3 = getattr(P,ter)
            # Obtiene valor de atributo con nombre de preferencia
            txt =P.name
            # Según caso añade Barrio y contenido
            if (p1==1 and p2==1 and p3==1):
                txt += ": "+prim+" "+sec+" "+ter
                ls1.append(txt) # Caso 1: Están todos
            elif (p1==1 and p2==1):
                txt += ": "+prim+" "+sec
                ls2.append(txt)  # Caso 2: Está primario y secundario
            elif (p1==1):
                txt += ": "+prim
                ls3.append(txt)      # Case 3: Está solo primario
            N = N.next # Siguiente Nodo

        ls.extend(ls1)
        ls.extend(ls2)
        ls.extend(ls3)
        if(10>len(ls)):
             end = len(ls)
        else: # 10<len(ls)
             end = 10
        # Agregan casos a lista principal y muestran hasta 10 primeros casos
        ls = [ls[i] for i in range(end)]    
        return ls

    def search2(self, prim: str, sec: str=None, ter: str=None, cuat: str=None, quin: str=None):
        """
        Devuelve lista con Barrios que cumplen con preferencias
        Las preferencias van de 1 a 5
        """
        ls =[] # Lista principal
        ls1=[] # Lista de 5 preferencias cumplidas
        ls2=[] # Lista de 4 preferencias ...
        ls3=[] # Lista de 3..
        ls4=[] # 2...
        ls5=[] # 1
        # Listas para cada caso en orden de importancia
        N = self.PTR
        while(N!=None): # Recorriendo Nodos de LinkedList
            P = N.Barrio
            txt =P.name # Nombre del Barrio
            p1 = getattr(P,prim)
            if(quin!=None): 
                p5 = getattr(P,quin) # Si la preferencia fue solicitada se obtiene el atributo
            else:
                p5=0                 # De no serlo se asume que es 0 y no entra en condicionales
            if (cuat!=None):
                p4 = getattr(P,cuat)            # Idem
            else:
                p4=0
            if (ter!=None):
                 p3 = getattr(P,ter)
            else:
                p3=0
            if(sec!=None):
                 p2 = getattr(P,sec)
            else:
                p2=0
           
             # Dependiendo del numero de preferencias se buscan condiciones cumplidas
            if (p1==1 and p2==1 and p3==1 and p4==1 and p5==1):
                txt += ": "+prim+" "+sec+" "+ter+" "+cuat+" "+quin  # Agrega a Barrio su info cumplida
                ls1.append(txt) # Agrega a lista Barrio e info
            elif (p1==1 and p2==1 and p3==1 and p4==1):
                txt += ": "+prim+" "+sec+" "+ter+" "+cuat
                ls2.append(txt)  
            elif (p1==1 and p2==1 and p3==1):
                txt += ": "+prim+" "+sec+" "+ter
                ls3.append(txt)      
            elif (p1==1 and p2==1):
                txt += ": "+prim+" "+sec
                ls4.append(txt)
            elif (p1==1):
                txt += ": "+prim
                ls5.append(txt)
            
            
            N = N.next # Siguiente Nodo

        ls.extend(ls1) 
        ls.extend(ls2)
        ls.extend(ls3)
        ls.extend(ls4)
        ls.extend(ls5)
        # Extiende lista principal en orden de jerarquia (Es preferible tener todas las pedidas)
        if(10>len(ls)):
             end = len(ls)
        else: # 10<len(ls)
             end = 10
        # Agregan casos a lista principal y muestran hasta 10 primeros casos
        ls = [ls[i] for i in range(end)]    
        return ls
