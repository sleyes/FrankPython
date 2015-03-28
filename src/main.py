# -*- coding: utf-8 -*-

from agendaObj import Agenda
# u'somestring' -> unicode string

def main():
    obj_agenda = Agenda()
    opcion = 0
    while opcion != "5":
        print "\n"*80
        print "="*30
        print "Bienvenidos a mi agenda"
        print "="*30
        print "Opciones:"
        print '-'*30
        print '1) Ver agenda'
        print '2) Agregar registro'
        print '3) Borrar registro'
        print '4) Buscar registro'
        print '5) Salir'
        opcion = raw_input("Ingrese opcion: ")
        if opcion == '1':
            print '+'*30
            print obj_agenda.Listar()
        elif opcion == '2':
            print '+'*30
            name = raw_input("Ingrese Nombre: ")
            last_name = raw_input("Ingrese Apellido: ")
            address = raw_input("Ingrese Dirección: ")
            email = raw_input("Ingrese email: ")
            phone = raw_input("Ingrese teléfono: ")
            resultado = obj_agenda.Guardar2(
                name, 
                last_name,
                email=email,
                phone=phone,
                address=address 
                )
            if resultado: 
                print "Se guardó correctamente"
        elif opcion == "3":
            print '+'*30
            name = raw_input("Ingrese Nombre del registro a borrar: ")
            last_name = raw_input("Ingrese Apellido del registro a borrar: ")
            resultado = obj_agenda.Borrar(name, last_name)
            if resultado:
                print "El registro se borró correctamente"
            else:
                print "No se encontró registro coincidente"
        elif opcion == '4':
            print '+'*30
            name = raw_input("Ingrese Nombre y/o Apellido del registro a buscar: ")
            resultado = obj_agenda.Buscar(name)
            if len(resultado)>0:
                for a in resultado:
                    print a
            else:
                print "No se encontró registro"
        raw_input("Presione Enter para continuar. ")

if __name__ == '__main__':
    main()

