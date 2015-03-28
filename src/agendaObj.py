# -*- coding: utf-8 -*-

import traceback


class Agenda(object):
    agendaDB = []

    """docstring for Agenda"""
    def __init__(self, arg):
        super(Agenda, self).__init__()
        self.arg = arg

    def Guardar(self, nombre, direccion, telefono, email):
        self.agendaDB.append(
            {
            'nombre' : nombre, 
            'direccion' : direccion,
            'telefono' : telefono,
            'email' : email
            }
        )

    def Guardar2(self, Name, Last_Name, **kwars):
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
        self.agendaDB.append(s)
        return True

    '''
    usando el buscar, si se encuetra el registro, quitarlo del array
    '''
    def Borrar(self, searchTerms):
        r = Buscar(searchTerms)
        if r is not None:
            self.agendaDB.remove(r)
            return True
        return False

    '''
    devuelve el registro que coincida con los terminos de busqueda

    hacer un split del parametro de busqueda, por ' ', para comparar 
    por un lado el nombre y por otro el apellido
    '''
    def Buscar(self, searchTerms):
        terms = searchTerms.split(' ')
        for a in self.agendaDB:
            if a['name'] in terms and a['last_name'] in terms:
                return [a]
        return []

    '''
    Listar

    devolver registros, no solo imprimir por pantalla 
    '''
    def Listar(self):
        return self.agendaDB


