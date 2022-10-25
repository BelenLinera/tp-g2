import sqlite3
import datetime
from datetime import date
import time


class ProgramaPrincipal:

    def menu(self):
        while True:
            print("Menu de opciones")
            print("0- Salir de menu")
            print("1- Cargar Monopatines")
            print("2- Modificar Monopatin")
            print("3- Borrar Monopatin")
            print("4- Cargar disponibilidad")
            print("5- Listado de productos")
            print("6- Crear tabla con nuevos atributos")
            print("7- Actualizar precios por el aumento del dolar")
            print("8- Mostrar registros anteriores a una fecha especifica")
            nro = int(input("Por favor ingrese un número: "))
            if nro == 1:
                marca = input("Por favor ingrese la marca del monopatin: ")
                precio = float(input("Por favor ingrese el precio del monopatin: "))
                cantidadDisponibles = input("Por favor ingrese la cantidad de unidades disponibles: ")
                nuevo_monopatin = Monopatin()
                nuevo_monopatin.marca=marca
                nuevo_monopatin.precio=precio
                nuevo_monopatin.cantidadDisponibles=cantidadDisponibles
                nuevo_monopatin.cargar_monopatin()
            if nro ==2:
                marca = input("Por favor ingrese la marca del monopatin a modificar: ")
                precio = float(input("Por favor ingrese el nuevo precio: "))
                monopatin_a_modificar = Monopatin()
                monopatin_a_modificar.marca = marca
                monopatin_a_modificar.precio=precio
                monopatin_a_modificar.modificar_monopatines()
            if nro ==3:
                id_usuario = input("ingrese el id del monopatin a eliminar: ")    
                eliminar_monopatin(id_usuario)
            if nro ==4:
                marca = input("Por favor ingrese la marca del monopatin: ")
                sumar_disponibilidad =Monopatin()
                sumar_disponibilidad.marca=marca
                sumar_disponibilidad.cargar_disponibilidad()
            if nro ==5:
                lista_ordenada =Monopatin()
                lista_ordenada.mostrar_productos()
            if nro ==6:
                modelo= input("Por favor ingrese el modelo del monopatin: ")
                marca = input("Por favor ingrese la marca del monopatin: ")
                potencia = input("Por favor ingrese la potencia del monopatin: ")
                precio = float(input("Por favor ingrese el precio del monopatin: "))
                color = input("Por favor ingrese el color del monopatin: ")
                fechaUltimoPrecio=time.strftime("%x %X")
                nuevo_monopatin2 = Monopatin2()
                nuevo_monopatin2.modelo=modelo
                nuevo_monopatin2.marca=marca
                nuevo_monopatin2.potencia=potencia
                nuevo_monopatin2.precio=precio
                nuevo_monopatin2.color=color
                nuevo_monopatin2.fechaUltimoPrecio=fechaUltimoPrecio
                nuevo_monopatin2.cargar_monopatin2()    
            if nro==7:
                fechaActual= time.strftime("%x %X")
                datos_a_insertar=historicoPrecios()
                datos_a_insertar.insertarDatos()
                precio_actualizado=Monopatin2()
                precio_actualizado.actualizar_precio(fechaActual)
            if nro==8:
                fechaAIngresar = input("Ingrese una fecha y la hora para buscar los registros con el formato: '(MM/DD/YY hh:mm:ss)': ")
                Monopatin2.listado_fechas(fechaAIngresar)
            if nro==0:
                break
    
    def crearTablas(self):
        conexion = Conexiones()
        conexion.abrirConexion() 
        conexion.miCursor.execute("CREATE TABLE IF NOT EXISTS MONOPATINES (id_usuario INTEGER PRIMARY KEY AUTOINCREMENT, marca  VARCHAR(30) ,precio FLOAT NOT NULL, cantidadDisponibles INTEGER NOT NULL, UNIQUE(marca))")    
        conexion.miConexion.commit()
        conexion.cerrarConexion() 

    def crearTablas2(self):
        conexion = Conexiones() 
        conexion.abrirConexion() 
        conexion.miCursor.execute("CREATE TABLE IF NOT EXISTS MONOPATINES2 (id_mono INTEGER PRIMARY KEY AUTOINCREMENT, modelo VARCHAR(30), marca  VARCHAR(30),potencia VARCHAR(30), precio VARCHAR(30), color VARCHAR(30), fechaUltimoPrecio DATETIME)")
        conexion.miConexion.commit() 
        conexion.cerrarConexion()
    
    def crearTablaHP(self):
        conexion = Conexiones() 
        conexion.abrirConexion() 
        conexion.miCursor.execute("CREATE TABLE IF NOT EXISTS HISTORICO_PRECIOS (id_mono INTEGER PRIMARY KEY AUTOINCREMENT, modelo VARCHAR(30), marca  VARCHAR(30),potencia VARCHAR(30), precio VARCHAR(30), color VARCHAR(30), fechaUltimoPrecio DATETIME)")
        conexion.miConexion.commit()  
        conexion.cerrarConexion()

class Monopatin:
    def init(self,marca,precio=None,cantidadDisponibles=None):
        self.marca = marca
        self.precio = precio
        self.cantidadDisponibles = cantidadDisponibles
        
    def cargar_monopatin(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("INSERT INTO MONOPATINES(marca,precio,cantidadDisponibles) VALUES('{}','{}','{}')".format(self.marca, self.precio,self.cantidadDisponibles))
            conexion.miConexion.commit()
            print("Monopatin cargado exitosamente")
        except:
            print("Error al agregar un monopatin")
        finally:
            conexion.cerrarConexion()

    
    def modificar_monopatines(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE MONOPATINES SET precio='{}' where marca='{}' ".format(self.precio, self.marca))
            conexion.miConexion.commit()
            print("Monopatin modificado correctamente")
        except:
            print('Error al actualizar un monopatin')
        finally:
            conexion.cerrarConexion()  

    def cargar_disponibilidad(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute ("UPDATE MONOPATINES SET cantidadDisponibles = cantidadDisponibles + 1 where marca='{}'".format(self.marca))
            conexion.miConexion.commit()
            print("Cantidad disponible")
        except:
            print('Error al actualizar la disponibilidad')
        finally:
            conexion.cerrarConexion()
        
    def mostrar_productos(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM MONOPATINES")
            conexion.miConexion.commit()
            print("id_usuario, marca, precio, cantidadDisponible")
            for Row in conexion.miCursor.execute("SELECT * FROM MONOPATINES"):
                print(Row) 
            
        finally:
            conexion.cerrarConexion()

def eliminar_monopatin(id_usuario):
    conexion = Conexiones()
    conexion.abrirConexion()
    try: 
        conexion.miCursor.execute("DELETE FROM MONOPATINES where id_usuario='{}'".format(id_usuario)) 
        conexion.miConexion.commit()
        print("Se ha eliminado correctamente")
    except:
        print("Error, no se encontro el id")
    finally:
        conexion.cerrarConexion()

class Monopatin2:
    def init(self,modelo,marca,potencia,precio,color,fechaUltimoPrecio):
        self.modelo = modelo
        self.marca = marca
        self.potencia = potencia
        self.precio = precio
        self.color = color
        self.fechaUltimoPrecio = fechaUltimoPrecio

    def cargar_monopatin2(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("INSERT INTO MONOPATINES2 (modelo,marca,potencia,precio,color,fechaUltimoPrecio) VALUES('{}','{}','{}','{}','{}','{}')".format(self.modelo, self.marca, self.potencia, self.precio, self.color, self.fechaUltimoPrecio))
            conexion.miConexion.commit()
            print("Monopatin cargado exitosamente")
            
        except:
            print("Error al agregar un monopatin")
        finally:
            conexion.cerrarConexion() 

    def actualizar_precio(self,fechaActual):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute ("UPDATE MONOPATINES2 SET precio = (precio * 1.23)")   
            
            conexion.miCursor.execute ("UPDATE MONOPATINES2 SET fechaUltimoPrecio = '{}'".format(fechaActual))            
            conexion.miConexion.commit()
            print("Precio actualizado")
        except:
            print('Error al actualizar los precios')
        finally:
            conexion.cerrarConexion()

    @classmethod
    def listado_fechas(cls,fechaAIngresar):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM MONOPATINES2 WHERE fechaUltimoPrecio <= '{}'".format(fechaAIngresar))
            monopatines = conexion.miCursor.fetchall()
            for monopatin in monopatines:
                id,modelo,marca,potencia,precio,color,fechaUltimoPrecio = monopatin
                print("El monopatin con ID: "+str(id)+" marca: "+str(marca)+ " modelo: "+str(modelo)+ " potencia: "+str(potencia)+" precio: "+str(precio)+" color "+str(color)+" fecha: "+str(fechaUltimoPrecio))
        except:
            print("Error no se han encontrado registros anteriores a esa fecha")
        finally:
            conexion.cerrarConexion()

class historicoPrecios:
    def init(self,modelo,marca,potencia,precio,color,fechaUltimoPrecio):
        self.modelo = modelo
        self.marca = marca
        self.potencia = potencia
        self.precio = precio
        self.color = color
        self.fechaUltimoPrecio = fechaUltimoPrecio
        
    def insertarDatos(self):
        conexion = Conexiones() 
        conexion.abrirConexion() 
        conexion.miCursor.execute("INSERT INTO HISTORICO_PRECIOS (modelo,marca,potencia,precio,color,fechaUltimoPrecio) SELECT modelo,marca,potencia,precio,color,fechaUltimoPrecio FROM MONOPATINES2")  
        conexion.miConexion.commit()  
        conexion.cerrarConexion() 

class Conexiones:
    def abrirConexion(self):
        self.miConexion = sqlite3.connect("monopatiness.db")
        self.miCursor = self.miConexion.cursor()  
    def cerrarConexion(self):
        self.miConexion.close()   


            
programa = ProgramaPrincipal()
programa.crearTablas()
programa.crearTablas2()
programa.crearTablaHP()
programa.menu()