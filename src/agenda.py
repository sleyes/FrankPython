# -*- coding: utf-8 -*-

import traceback

agendaDB = []


def Guardar(nombre, direccion, telefono, email):
    agendaDB.append(
        {
        'nombre' : nombre, 
        'direccion' : direccion,
        'telefono' : telefono,
        'email' : email
        }
    )

def Guardar2(Name, Last_Name, **kwars):
    s = {
        'name' : Name,
        'last_name' : Last_Name
    }
    if 'address' in kwars:
        s['address'] = kwars['address']
    if 'email' in kwars:
        s['email'] = kwars['email']
    if 'phone' in kwars:
        s['phone'] = kwars['phone']
    agendaDB.append(s)

'''
usando el buscar, si se encuetra el registro, quitarlo del array
'''
def Borrar(searchTerms):
    r = Buscar(searchTerms)
    if r is not None:
        agendaDB.remove(r)


'''
devuelve el registro que coincida con los terminos de busqueda

hacer un split del parametro de busqueda, por ' ', para comparar 
por un lado el nombre y por otro el apellido
'''
def Buscar(searchTerms):
    terms = searchTerms.split(' ')
    for a in agendaDB:
        if a['name'] in terms and a['last_name'] in terms:
            return a


'''
Listar

devolver registros, no solo imprimir por pantalla 
'''
def Listar(nombre):
    return agendaDB


