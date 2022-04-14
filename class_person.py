valores_libros=[3,4,5,6]
libros_arrendados=[["nombre","nombre arrendatario","fecha arriendo"],["gob","samuel","25/07/2021"]]
inventario=[["nombre","autor","genero",1," serie"],["rapunzel","pedra","drama",1,"1234"],["ender game","diego","accion",1,"1235"],["cenicienta","mateo","drama",1,"1236"]]
from abc import ABC, abstractmethod
class Person(ABC):
    @abstractmethod
    def checkout():
        nombre_libro=input("ingrese nombre del libro a devolver\n")
        n=int(input("cuantos dias tuvo el libro\n"))
        for i in libros_arrendados:
            z=valores_libros[i]
            for j in i:
                if j==nombre_libro:
                    pago=n*z
                    print(f"debe pagar un total de {pago}")