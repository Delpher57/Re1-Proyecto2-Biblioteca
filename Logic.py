from datetime import datetime, timedelta
import BookGenerator
import Data



#variables de funcionamiento
date = "26/09/2021"
fecha_actual = datetime.strptime(date, "%d/%m/%Y")


#creamos los libros
libros = BookGenerator.generar_libros(50)

#creamos los usuarios de prueba
usuarios = [Data.Usuario(0, "Jonny Paletico", "JonnyP", "jonny123"),
            Data.Usuario(1, "Zavaleta", "Zava", "zava123")]

#aqui vamos a manejar los prestamos
prestamos = []



def select_libros():
    for libro in libros:
        print("> " + libro.print_info_libro())
        

def select_users():
    for user in usuarios:
        print("> " + user.print_info_user())

def select_prestamos():
    for prestamo in prestamos:
         print("> " + prestamo.print_info_prestamo())


def get_fecha_actual():
    return datetime.strftime(fecha_actual, '%d/%m/%Y')

def get_estado_libro(libro):

    for prestamo in prestamos:

        if prestamo.activo == True:

            #verificar si el libro esta siendo prestado o no
            if prestamo.libro == int(libro):
                return "Prestado"
    
    return "Disponible"

def get_prestamos_usuario(id):
    """[obtenemos los prestamos activos de un usuario]

    Args:
        id ([int]): [id del usuario]

    Returns:
        [array]: [lista de los prestamos]
    """    
    user_prestamos = []
    for prestamo in prestamos:

        if prestamo.activo == True and prestamo.usuario == id:
            user_prestamos += [prestamo]
    
    return user_prestamos



def verificar_prestamo(libro,usuario):
    """[hacemos la verificacion de si se puede hacer el prestamo]

    Args:
        libro ([int]): [id del libro a pedir]
        usuario ([int]): [id del usuario que pide el libro]

    Returns:
        [array]: [elemento de dos partes, primero si se puede o no (true - false), y un mensaje de respuesta]
    """    
    if prestamos == []:
        return [True,"No hay ningun prestamo"]
    
    for prestamo in prestamos:

        if prestamo.activo == True:
            
            #verificar si el libro esta siendo prestado o no
            if prestamo.libro == int(libro):
                fecha_devolucion = prestamo.fecha_devolucion
                return [False, "El libro no esta disponible, vuelva el " + fecha_devolucion]
            
            #verificar morosidad
            if prestamo.usuario == usuario:
                fecha_devolucion = prestamo.fecha_devolucion
                fecha_devolucion = datetime.strptime(fecha_devolucion, "%d/%m/%Y")

                if fecha_actual > fecha_devolucion:
                    return [False, "Usted se encuentra con morosidades, por favor proceda a pagarlas!"]
    
    return [True,"Se puede hacer el prestamo"]

    

def hacer_prestamo(libro,usuario):
    """[hacemos un prestamo en el sistema]

    Args:
        libro ([int]): [id de libro a pedir]
        usuario ([int]): [id del usuario]

    Returns:
        [str]: [mensaje de como se realizo la operacion]
    """ 

    global prestamos

    if libro > len(libros)-1:
        return "Ese libro no existe"

    verificacion = verificar_prestamo(libro,usuario)
    if verificacion[0] == False:
        return verificacion[1]
    
    
    _id = len(prestamos)
    fecha_prestamo = datetime.strftime(fecha_actual, '%d/%m/%Y')
    fecha_devolucion = fecha_actual + timedelta(days=7) #1 semana de tiempo en el prestamo
    fecha_devolucion = datetime.strftime(fecha_devolucion, '%d/%m/%Y')

    nuevo_prestamo = Data.PrestamosXUsuario(_id, usuario, libro,fecha_prestamo, fecha_devolucion, True)

    prestamos += [nuevo_prestamo]
    
    return "Prestamo realizado con exito"


def devolver_libro(prestamo, user, pagando=False):
    """[devolvremos un libro]

    Args:
        prestamo ([int]): [id del prestamo]
        user ([int]): [id del usuario]
        pagando (bool, optional): [para saber si estamos devolviendo con un pag, en caso de morosidad]. Defaults to False.

    Returns:
        [type]: [description]
    """
    global prestamos

    if prestamo > len(prestamos)-1:
        return "Ese prestamo no existe"
    if prestamos[prestamo].usuario != user:
        return "Ese prestamo no le pertenece"

    fecha_devolucion = prestamos[prestamo].fecha_devolucion
    fecha_devolucion = datetime.strptime(fecha_devolucion, "%d/%m/%Y")

    if fecha_actual > fecha_devolucion and pagando==False:
        return "Usted se encuentra con morosidades, por favor proceda a pagarlas"

    prestamos[prestamo].activo = False

    return ("Se ha devuelto el libro con exito")


def aumentar_fecha_actual(dias):
    global fecha_actual
    fecha_actual = fecha_actual + timedelta(days=dias) #cantidad de dias que vamos aamentar

