from Class_inventario import Inventario
from class_rental import Rental
from class_person import Person
from Class_employee import Employee
inventario=[["nombre","autor","genero",1," serie"],["rapunzel","pedra","drama",1,"1234"],["ender game","diego","accion",1,"1235"],["cenicienta","mateo","drama",1,"1236"]]
libros_arrendados=[["nombre","nombre arrendatario","fecha arriendo"],["gob","samuel","25/07/2021"]]
menu=1
while menu!=0:
    print("Menu principal\n"
          "1) ver inventario\n"
          "2) Manejar arriendos\n"
          "3) Categorizar el inventario\n"
          "4) Modificar el catalogo\n"
          "5) Devolver un libro\n"
          "0) Para cerrar\n")
    menu=int(input("ingrese de forma numerica que opcion desea\n"))
    if menu==1:
        myinventario=Inventario()
        m=Inventario.ver_inventario()
        n=Inventario.ver_disponibilidad()
    if menu==2:
        rental=Rental()
        menu2=0
        menu2=int(input("1) ver libros arrendados\n"
                        "2) buscar arrendatario\n"
                        "3) arrendar libro\n"))
        if menu2==1:
            m=Rental.ver_libros_arrendados()
        if menu2==2:
            y=Rental.buscar_arrendatario()
        if menu2==3:
            g=Rental.arrendar_libro()
        else:
            print("esa opcion no esta disponible")
    if menu==3:
        t=Inventario.categorizar_inventario()
    if menu==4:
        menu3=0
        menu3=int(input("1) Añadir libro\n"
                        "2) Eliminar libro\n"))
        if menu3==1:
            y=Inventario.agregar_libro()
        if menu3==2:
            r=Inventario.eliminar_libro()
    if menu==5:
        menu4=(input("Es usted empleado?\n"))
        if menu4=="si":
            myperson=Person()
            myemployee=Employee(myperson)
            r=Employee.checkout_Employee()
        else:
            myperson=Person()
            re=Person.checkout()
        