from typing import List


class Barrio:
    def __init__(self, name, list: List) -> None:
        """"
        store name
        turn elements of list into ints
        store in each attribute of place
        """
        self.name = name
        self.ls = [int(i) for i in list]
        self.School = self.ls[0]
        self.Gym = self.ls[1]
        self.Bar = self.ls[2]
        self.Shop = self.ls[3]
        self.Park = self.ls[4]
        

    def __repr__(self) -> str:
        return f"{self.name}"
    
    
class Nodo: 
    def __init__(self, data, list) -> None:
        """ 
        Create a Barrio that is contained with data and list
        """
        self.Barrio = Barrio(data, list)
        self.next = None

"""
Get Attribute value by name
b = Barrio("Candelaria",[1,0,2,3,4])
a = "School"
print(getattr(b,"Park"))
"""


