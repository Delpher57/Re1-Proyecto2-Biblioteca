import Logic
import os
#pip install flask
from flask import Flask, redirect, url_for, render_template, request, session, flash

 
app = Flask(__name__)  # creamos la pagina
# key para tener los datos de inicio de secion encriptados
app.secret_key = "c8gd6qlgK4N2*XtLeHa2ykCj!fQrR(a@R)t4TaLee43c$F9&)2w6"



# ---------------------------------------------- #

#verificamos si hay una sesión iniciada, retornamos true o false
def verificar_sesion():
    if "user" in session and "password" in session: #verificamos que el usuario alla iniciado sesion
        return True
    else:
        return False



# pagina de inicio de sesión
@app.route("/login/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        usuarios = Logic.usuarios #obtenemos los usuarios
        

        for usuario in usuarios:
            if usuario.usuario == username and usuario.password == password:
                session["user"] = username
                session["password"] = password
  
                session["name"] = usuario.nombre
                session["user_id"] = usuario._id

                return redirect(url_for("home"))
        
        flash("Datos incorrectos", "info")
        return render_template("login.html")
    else:
        if "user" in session:
            return redirect(url_for("home"))
        else:
            return render_template("login.html")


 
# pagina de cerrar sesión
@app.route("/logout/")
def logout():
    if "user" in session and "password" in session:
        flash("Se ha cerrado la sesión", "info")
    
    session.pop("user", None)
    session.pop("password", None)
    return redirect(url_for("login"))

# ---------------------------------------------- #
mensaje = "default"
last_devolder = 0 #guardamos la ultima id de prestamo devuelta

#pagina principal
@app.route("/home/", methods=["POST", "GET"])
def home():
    global mensaje
    global last_devolder

    if verificar_sesion():
        if request.method == "POST":

            #hacer un prestamo de un libro
            if "hacer_prestamo" in request.form:
                id_libro = int(request.form["id_libro_prestamo"])
                id_user = int(session["user_id"])
                mensaje = Logic.hacer_prestamo(id_libro,id_user)
                flash(mensaje, "info")
            
            elif "devolver_libro" in request.form:
                id_prestamo = int(request.form["id_prestamo"])
                last_devolder = id_prestamo
                id_user = int(session["user_id"])
                mensaje = Logic.devolver_libro(id_prestamo,id_user)
                flash(mensaje, "info")

            elif "aumentar_fecha" in request.form:
                dias = int(request.form["cantidad_dias"])
                Logic.aumentar_fecha_actual(dias)
                flash("fecha modificada", "info")
                mensaje = "fecha modificada con exito"
            
            elif "pagar_moro" in request.form:
                id_prestamo = last_devolder
                id_user = int(session["user_id"])
                mensaje = Logic.devolver_libro(id_prestamo,id_user,True)
                flash(mensaje, "info")
            
           
            return redirect(url_for('home'))


        return render_template("homepage.html", nombre=session["name"], fecha=Logic.get_fecha_actual(), libros=Logic.libros, prestamos=Logic.get_prestamos_usuario(int(session["user_id"])), mensaje=mensaje)
    else:
        return redirect(url_for("login")) 


@app.route("/")
def inicio():
    return redirect(url_for("home"))


@app.context_processor
def utility_processor():
    def estado_libro(id):
        estado = Logic.get_estado_libro(id)
        return estado
    return dict(estado_libro=estado_libro)

# ejecutamos la pagina
if __name__ == "__main__":
    app.run(debug=True)



'''

def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') #funcion para limpiar la terminal

        print("Bienvenido al sistema de biblioteca, hoy es: " + Logic.get_fecha_actual() + "\n")
        print("ingrese opcion: ")
        print("1: ver libros")
        print("2: ver usuarios")
        print("3: hacer prestamo")
        print("4: ver prestamos")
        print("5: devolver libro")
        print("6: aumentar fecha actual")
        print("7: ver estado de libro")
        print("s: salir")
        print()

        opcion = input("ingrese opcion > ")

        os.system('cls' if os.name == 'nt' else 'clear') #funcion para limpiar la terminal

        if opcion == '1':
            Logic.select_libros()

        elif opcion == '2':
            Logic.select_users()

        elif opcion == '3':
            libro = int(input("Ingrese el Id del libro > "))
            usuario = int(input("Ingrese el Id del usuario > "))
            print (Logic.hacer_prestamo(libro,usuario))
        
        elif opcion == '4':
            Logic.select_prestamos()
        
        elif opcion == '5':
            prestamo = int(input("Ingrese el Id del prestamo > "))
            print(Logic.devolver_libro(prestamo))

        elif opcion == '6':
            dias = int(input("Ingrese los dias por aumentar > "))
            Logic.aumentar_fecha_actual(dias)
        
        elif opcion == '7':
            libro = int(input("Ingrese el Id del libro > "))
            print(Logic.get_estado_libro(libro))

        elif opcion == 's':
            break
        
        input()

menu()



'''