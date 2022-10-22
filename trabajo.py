import sqlite3

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
                id_usuario = 0
                marca = input("Por favor ingrese la marca del monopatin: ")
                precio = input("Por favor ingrese el precio del monopatin: ")
                cantidadDisponibles = input("Por favor ingrese la cantidad de unidades disponibles: ")
                nuevo_monopatin = Monopatin()
                nuevo_monopatin.id_usuario=id_usuario
                nuevo_monopatin.marca=marca
                nuevo_monopatin.precio=precio
                nuevo_monopatin.cantidadDisponibles=cantidadDisponibles
                nuevo_monopatin.cargar_monopatin()
            if nro ==2:
                marca = input("Por favor ingrese la marca del monopatin a modificar: ")
                precio = input("Por favor ingrese el nuevo precio: ")
                monopatin_a_modificar = Monopatin()
                monopatin_a_modificar.marca = marca
                monopatin_a_modificar.precio=precio
                monopatin_a_modificar.modificar_monopatines()
            if nro ==3:
                #no funciona el borrar
                id_usuario = input("ingrese el id del monopatin a eliminar: ")    
                monopatin_a_eliminar = Monopatin()
                monopatin_a_eliminar.id_usuario = id_usuario          
                monopatin_a_eliminar.eliminar_monopatin()
            if nro ==4:
                marca = input("Por favor ingrese la marca del monopatin: ")
                sumar_disponibilidad =Monopatin()
                sumar_disponibilidad.marca=marca
                sumar_disponibilidad.cargar_disponibilidad()
            if nro ==5:
                lista_ordenada =Monopatin()
                lista_ordenada.mostrar_productos()
            if nro ==6:
                color = input("Por favor ingrese el color del monopatin: ")
                potencia = input("Por favor ingrese la potencia del monopatin: ")
                fechaUltimoPrecio = input("Por favor ingrese la fecha del ultimo precio: ")
                nuevo_monopatin2 = Monopatin2()
                nuevo_monopatin2.color=color
                nuevo_monopatin2.potencia=potencia
                nuevo_monopatin2.fechaUltimoPrecio=fechaUltimoPrecio
                nuevo_monopatin2.cargar_monopatin2()
            """if nro==7:
                fechaUltimoPrecio = input("Por favor ingrese la fecha de hoy: ")
                precio_actualizado=Monopatin2()
                precio_actualizado.fechaUltimoPrecio= fechaUltimoPrecio
                precio_actualizado=actualizar_precio()"""
            
            if nro==8:
                fechaAnterior = input("Por favor ingrese una fecha desde la cual quiere mostrar los registros: ")
                fechaEspecifica = Monopatin2()
                fechaEspecifica.mostrarRegistros()
            if nro==0:
                break
    
    def crearTablas(self):
        conexion = Conexiones()
        conexion.abrirConexion() #ESTO
        conexion.miCursor.execute("DROP TABLE IF EXISTS MONOPATINES")
        conexion.miCursor.execute("CREATE TABLE MONOPATINES (id_usuario INTEGER PRIMARY KEY AUTOINCREMENT, marca  VARCHAR(30) ,precio FLOAT NOT NULL, cantidadDisponibles INTEGER NOT NULL, UNIQUE(marca))")    
        conexion.miConexion.commit()  #ESTO     
        conexion.cerrarConexion() # ESTO SIEMPRE LO MISMO

class Monopatin:
    def init(self, id_usuario, marca,precio,cantidadDisponibles):
        self.id_usuario = id_usuario
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

    def eliminar_monopatin(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try: 
            #esta mal, no lo borra
            #conexion.miCursor.execute("DELETE MONOPATINES(id_usuario,marca,precio,cantidadDisponibles) VALUES('{}','{}','{}','{}')".format(self.id_usuario, self.marca, self.precio,self.cantidadDisponibles))
            conexion.miCursor.execute("DELETE MONOPATINES VALUES ('{}','{}','{}','{}')".format(self.id_usuario, self.marca, self.precio,self.cantidadDisponibles))
            conexion.miConexion.commit()
        except:
            print("Error, no se encontro el id")
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

class Monopatin2:
    def init(self,id_mono, modelo, marca, potencia, precio, color, fechaUltimoPrecio):
        self.id_mono = id_mono
        self.modelo = modelo
        self.marca = marca
        self.potencia = potencia
        self.precio = precio
        self.color = color
        self.fechaUltimoPrecio = fechaUltimoPrecio

    def crearTablas2(self):
        conexion = Conexiones() 
        conexion.abrirConexion() 
        conexion.miCursor.execute("DROP TABLE IF EXISTS MONOPATINES2")
        #asi esta bien para que guarde los valores?
        conexion.miCursor.execute("CREATE TABLE MONOPATINES2 (id_mono INTEGER PRIMARY KEY AUTOINCREMENT, modelo  VARCHAR(30), marca VARCHAR(30), potencia VARCHAR(30), precio INTEGER,color VARCHAR(30),fechaUltimoPrecio DATETIME")  
        conexion.miCursor.execute("INSERT INTO MONOPATINES2(id_mono,marca,precio) SELECT  id_usuario, marca, precio where Monopatines")
        conexion.miConexion.commit() 
        conexion.cerrarConexion()

    def cargar_monopatin2(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try: 
            conexion.miCursor.execute("INSERT INTO MONOPATINES2(potencia,color,fechaUltimoPrecio) values('{}''{}''{}'") 
            conexion.miConexion.commit()
            print("Monopatines cargado con EXITO")
        except:
            print("Error al cargar Monopatin")  
        finally:
            conexion.cerrarConexion() 
##aca
    def crearTablaHistoricoPrecio(self):
        conexion = Conexiones() 
        conexion.abrirConexion() 
        conexion.miCursor.execute("DROP TABLE IF EXISTS MONOPATINES2")
        conexion.miCursor.execute("CREATE TABLE HISTORICO_PRECIOS (id_hist, historico_precios)")  
        conexion.miCursor.execute("INSERT INTO HISTORICO_PRECIOS(id_mono,precio) SELECT  id_hist, historico_precio where MONOPATINES2")  
        conexion.miConexion.commit()  
        conexion.cerrarConexion() 

    def crearTablasHistoricoMono(self):
        conexion = Conexiones() 
        conexion.abrirConexion() 
        conexion.miCursor.execute("DROP TABLE IF EXISTS MONOPATINES2")
        conexion.miCursor.execute("CREATE TABLE HISTORICO_MONO (id_mono INTEGER PRIMARY KEY AUTOINCREMENT, modelo  VARCHAR(30), marca VARCHAR(30), potencia VARCHAR(30), precio INTEGER,color VARCHAR(30),fechaUltimoPrecio DATETIME")  
        conexion.miCursor.execute("INSERT INTO HISTORICO_MONO(id_mono,modelo,marca,potencia,precio,color,fechaUltimoPrecio) SELECT  id_mono,modelo,marca,potencia,precio,color,fechaUltimoPrecio where MONOPATINES2")
        conexion.miConexion.commit() 
        conexion.cerrarConexion()

    def actualizar_precio(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            #esta bien poner asi lo de precio. Y si esta bien agregar self.precio. si necesita un * para q modifique a todos
            #como hacemos para que modifique la fecha si al principio le decimos que ingrese la fecha de hoy
            #si arriba le pedimos que lo ingrese en una variable nueva y lo modificamos abajo
            conexion.miCursor.execute ("UPDATE MONOPATINES2 SET precio = (precio * 1.23) ")            
            conexion.miConexion.commit()
            print("Precio actualizado")
        except:
            print('Error al actualizar los precios')
        finally:
            conexion.cerrarConexion()
        
    def mostrarRegistros(self):
        conexion = Conexiones() 
        conexion.abrirConexion()
        try:
            #como hago para comparar la fecha "anterior" con la variable fecha ultimo precio
            conexion.miCursor.execute ("SELECT * FROM MONOPATINES2 where fechaUltimoPrecio < fechaAnterior")
            conexion.miConexion.commit()
            print("Los registros fueron mostrados correctamente")
        except:
             print('Error al mostrar los registros anteriores a la fecha ingresada')
        finally:
            conexion.cerrarConexion()

        

class Conexiones:
    def abrirConexion(self):
        self.miConexion = sqlite3.connect("monopatines.db")
        self.miCursor = self.miConexion.cursor()  
    def cerrarConexion(self):
        self.miConexion.close()   


            
programa = ProgramaPrincipal()
programa.crearTablas()
programa.menu()