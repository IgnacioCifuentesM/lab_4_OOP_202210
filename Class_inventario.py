inventario=[["nombre","autor","genero",1," serie"],["rapunzel","pedra","drama",1,"1234"],["ender game","diego","accion",1,"1235"],["cenicienta","mateo","drama",1,"1236"]]
libros_arrendados=[["nombre","nombre arrendatario","fecha arriendo"],["gob","samuel","25/07/2021"]]
class Inventario:
    def ver_inventario():
        print(inventario)
    def ver_disponibilidad():
        disponible=input("que libro desea ver si esta disponible?\n")
        n=0
        for i in libros_arrendados:
            for j in i:
                if j==disponible:
                    print("el libro no esta disponible")
                    n=1
                    break
        if n==0:
            print("el libro esta disponible")
myinventario=Inventario()
m=Inventario.ver_inventario()
n=Inventario.ver_disponibilidad()