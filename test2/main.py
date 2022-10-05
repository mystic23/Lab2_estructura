from Nodo import Barrio, Nodo
from LinkedList import LinkedList
path = "Estructura_Lab02\\test2\\data.txt"
a = LinkedList()

"""
partition(delimitation)
delimitation: criterio de partición
En 0 retorna antes de delimitation
En 1 returna delimitation
En 2 returns despues de delimitation
"""
def substring_after(s, delim):
    return s.partition(delim)[2] 
def get_name(s, delim):
    return  s.partition(delim)[0] 

f = open(path, "r", encoding='utf-8') # Encoding permite guardar caracteres con tilde "´"
f.readline()
for line in f:
    name = get_name(line,",") # Guarda nombre del Barrio
    #print(name)
    data = substring_after(line,",") # Guarda información despues del nombre
    data= data.split(",") # Guardar informacion en lista
    #print(data)
    a.AddNode(name, data) # Añadir Nodo con Barrio a LinkedList

# a.Recorrido() #M Muestra todos los barrios en cadena

op = ["School","Gym","Bar","Shop","Park",""] # Opciones validas
print("Opciones: School, Gym, Bar, Shop, Park")
print("Seleccione preferencias:")

print("Preferencia primaria")
prim = input()
while(prim not in op or prim==""): # Opcion primaria no podría estar vacía
    print("Opcion no valida")
    prim = input()

print("Preferencia secundaria") 
sec = input()
while(sec not in op):  # Validación simple
    print("Opcion no valida")
    sec = input()
if(sec==""):    # Cambio vacio significa ignorar campo
    sec=None

if(sec!=None): # Si hubo preferencia pasada podría haber siguiente
    print("Preferencia terciaria")
    ter = input()
    while(ter not in op):
        print("Opcion no valida")
        ter = input()
    if(ter==""):
        ter=None
else: # Si no hay pasadas, las demás serían ignoradas
    ter=None

if(ter!=None):  # Idem
    print("Preferencia cuaternaria")
    cuat = input()
    while(cuat not in op):
        print("Opcion no valida")
        cuat = input()
    if(cuat==""):
        cuat=None
else:
    cuat=None
if(cuat!=None):
    print("Preferencia quinaria")
    quin = input()
    while(quin not in op):
        print("Opcion no valida")
        quin = input()
    if(quin==""):
        quin=None
else:
    quin = None
results = a.search2(prim, sec, ter,cuat, quin) # Realiza busqueda en LinkedList
print(results)
