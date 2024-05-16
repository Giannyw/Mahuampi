from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
import base64


app = Flask(__name__)
app.secret_key='12345678'
# Configurar la conexión
dbCaracterizacion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="caracterizacion"
)

app = Flask(__name__)
app.secret_key='12345678'
# Configurar la conexión
dbUsuario = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="usuario"
)



cursorCaracterizacion = dbCaracterizacion.cursor()
cursorUsuario = dbUsuario.cursor()
##--------Validacion contraseña--------###
@app.route('/password/<passwordencrip>')
def encriptarpassword (passwordencrip):
    #generar un hash de la contraseña
    # encriptar= bcrypt.hashpw(Passwordencrip.encode('utf-8'), bcrypt.gestsalt())
    encriptar = generate_password_hash(passwordencrip)
    valor= check_password_hash(encriptar, passwordencrip)
   # return "Encriptado: {0} | coincide:{1}".format(encriptar, valor)
    return valor


##--------LOGIN USUARIOS--------##

@app.route('/ingreso', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        #VERIFICAR LAS CREDENCIALES DEL USUARIO
        usuario = request.form.get('Usuario')
        contraseña = request.form.get('Contraseña')
        
        cursor = db.cursor(dictionary=True)
        sql="SELECT Usuario, Contraseña, Cargo from personas WHERE usuarios= %s,%s,%s"
        cursor.execute(sql,(usuario))
        resultado = cursor.fetchone()
        
        if resultado and check_password_hash(resultado['Contraseña'], contraseña): 
                session['usuario'] = resultado['Usuario']
                session['rol']= resultado['rol']
                
                #de acuerdo al rol asignamnos las url 
                if resultado['roles'] == 'administrador':
                    return redirect(url_for('registroadm'))
                else:  
            
                    return redirect(url_for('vicepresidente'))
                    
        else:  
                return redirect(url_for('tesoreria'))
            
    else:
            return redirect(url_for('voluntario'))
        
        
print('Usuario no encontrado') 
       
##--------REGISTRAR USUARIO--------###

@app.route('/usuarios', methods=['GET', 'POST'])
def registrar_usuario():
    if request.method == 'POST':
        Tipo_Documento = request.form.get('tipo_dc')
        documento = request.form.get('documento')
        Nombres = request.form.get('nombre')
        Apellidos = request.form.get('apellido')
        Cargo = request.form.get('cargo')
        Direccion = request.form.get('direccion')
        Telefono1 = request.form.get('telefono1')
        Telefono2 = request.form.get('telefono2')
        Usuario = request.form.get('usuario')
        Password = request.form.get('contraseña')
        Roles = request.form.get('roles')
       
        Passwordencrip= generate_password_hash(Password)

         # Insertar datos a la tabla de mysql
        cursorUsuario.execute("INSERT INTO usuarios(Tipo_Doc,Num_Doc,Nombres,Apellidos,Cargo,Direccion,Telefono_prin,Telefono_sec,Usuario, Contraseña,Roles) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
        (Tipo_Documento, documento, Nombres, Apellidos, Cargo, Direccion, Telefono1, Telefono2, Usuario, Passwordencrip,Roles))
        dbUsuario.commit()

        print ("Usuario no registrado")     
        return redirect(url_for('registrar_usuario'))  # Redirigir a la página principal
    return render_template("usuarios.html")


##------------LISTA DE USUARIOS-----------------------------------------------##

@app.route('/lista', methods=['GET', 'POST'])  # Crear ruta
def mostrar_usuarios():
    cursor = db.cursor()
    cursor.execute("SELECT Num_Doc,Tipo_Doc,Nombres,Apellidos,Cargo,Direccion,Telefono_prin,Telefono_sec,Usuario, Contraseña,Rol FROM usuarios")
    usuarios = cursor.fetchall()
    if usuarios:
    #crear lista para almacenar canciones
         
            usuarioslist = []
            for usuarios in usuarios:                 
            #agg los datos de la cancion a la lista
                 usuarioslist.append({
                        'num_doc': usuarios[0],
                        'tipo_doc': usuarios[1],
                        'nombres': usuarios[2],
                        'apellidos': usuarios[3],
                        'cargo': usuarios[4],
                        'direccion':usuarios[5],
                        'telefono1':usuarios[7],
                        'telefono2':usuarios[8],
                        'nom_usu':usuarios[9],
                        'contraseña':usuarios[10],
                        'rol':usuarios[11]
                        })
            
            return render_template("lista_adm.html", usuarios=usuarioslist)
            print(usuarioslist.tipo_doc)
    else: 
        return print ("lista_adm.html")

##-------------------------------------------------------------------------------------------------##

@app.route('/registro_adm', methods=['GET', 'POST'])
def caracterizacion_adm():
    if request.method == 'POST':
        Num_doc = request.form.get('num_doc')
        Tipo_Doc = request.form.get('tipo_documento')
        Vigencia_doc = request.form.get('vig_doc')
        Nombres = request.form.get('nombres')
        Apellidos = request.form.get('apellidos')
        Fecha_Nacimiento = request.form.get('fecha_nac')
        Sexo = request.form.get('sexo')
        Edad = request.form.get('edad')
        Pasaporte = request.form.get('pasaporte')
        Vigencia_pas = request.form.get('vig_pasaporte')
        Num_pas = request.form.get('num_pas')
        Seg_Doc = request.form.get('seg_doc')
        Num_seg_doc = request.form.get('numseg_doc')
        Ter_Doc = request.form.get('ter_doc')
        Num_ter_doc = request.form.get('numter_doc')
      
      ## segunda tabla##
        Direccion_Residencia = request.form.get('dir_res')
        Localidad = request.form.get('localidad')
        Trabajo = request.form.get('trabajo')
        Direccion_Trabajo = request.form.get('dir_trab')
        Correo = request.form.get('correo')
        Telefono_1 = request.form.get('num_1')
        Telefono_2 = request.form.get('num_2')
        Cuar_Doc = request.form.get('cuar_doc')
        Num_cuar_doc = request.form.get('num_cuardoc')
        Grado_Instruccion = request.form.get('instruccion')
        Area_instruccion = request.form.get('area')
        Situacion_Migratoria = request.form.get('est_mig')
       
        cursorCaracterizacion.execute("INSERT INTO familiares(Num_doc_ref,)")
         # Insertar datos a la tabla de mysql
        cursorCaracterizacion.execute("INSERT INTO personas(Num_Doc	,Tipo_Doc,Vigencia_doc,Nombres,Apellidos,Fecha_Nacimiento,Sexo,Edad,Pasaporte,Vigencia_pas,Num_pas,Seg_Doc,Num_seg_doc,Ter_Doc,Num_ter_doc)VALUES(%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)",
        (Num_doc,Tipo_Doc,Vigencia_doc,Nombres,Apellidos,Fecha_Nacimiento,Sexo,Edad,Pasaporte,Vigencia_pas,Num_pas,Seg_Doc,Num_seg_doc,Ter_Doc,Num_ter_doc))
        dbCaracterizacion.commit()

        print (Sexo)
        print ("Usuario no registrado")   
          
        return redirect(url_for('caracterizacion_adm'))  # Redirigir a la página principal
    return render_template("form_adm.html")












# Ejecutar app
if __name__ == '__main__':
    app.add_url_rule('/',view_func=registrar_usuario)
    app.run(debug=True, port=5005) 
    # Debug para que salgan los errores en consola