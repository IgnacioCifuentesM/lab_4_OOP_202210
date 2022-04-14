inventario=[["nombre","autor","genero",1," serie",0],["rapunzel","pedra","drama",1,"1234",3],["ender game","diego","accion",1,"1235",4],["cenicienta","mateo","drama",1,"1236",7]]
libros_arrendados=[["nombre","nombre arrendatario"],["gob","samuel"]]
class Rental:
    def ver_libros_arrendados():
        print(libros_arrendados)
    def buscar_arrendatario():
        nombre_libro_a=input("ingrese nombre libro arrendado\n")
        for i in libros_arrendados:
            for j in i:
                if j==nombre_libro_a:
                    print("el dueño del libro ",nombre_libro_a," es ",libros_arrendados[i][1])
    def arrendar_libro():
        libro_arrendar=input("que libro desea arrendar?\n")
        libro_arrendado=[]
        for i in inventario:
            for j in i:
                if i==libro_arrendar:
                    libro_arrendado.append(i)
                    if inventario[j][3]>0:
                        inventario[j][3]-=1
                    else:
                        inventario.remove(i)
                    
                
                

