from flask import Blueprint, request, render_template, flash, url_for
from random import randint
import pymysql

usuario_blueprint = Blueprint('usuario', __name__, url_prefix='/usuario')

@usuario_blueprint.route('/') #localhost:5000/usuario/
def ver_usuarios():
    return "select * from usuario"

#responde a localhost:5000/usuario/id/1
@usuario_blueprint.route('/id/<int:id_usuario>/<string:nombre>') #<tipo:nombre_variable>
def ver_usuario_id(id_usuario, nombre):
    return f"Se hace el query con el id {id_usuario} y el nombre {nombre}"


@usuario_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_usuario():
    if request.method == 'GET':
        return render_template('add_user.html')
    else:
        try:
            #Obtengo la información del método post.
            name = request.form['name']
            ap_pat = request.form['ap_pat']
            passwd = request.form['passwd']
            #Creo mi usuario.

            #Lo guardo en la DB
            conn = pymysql.connect( 
            host='localhost', 
		    user='lab', 
		    password = "Developer123!", 
		    db='lab_ing_software', 
            ) 
      
            cur = conn.cursor() 

            cur.execute("insert into usuarios (nombre, apPat, password) values ('" + name  + "', '" + ap_pat + "', '" + passwd + "')") 

        
            conn.commit()
            conn.close() 
          
            return render_template('user_added.html', name=name, ap_pat = ap_pat)

        except:
            return render_template('error.html')


@usuario_blueprint.route('/actualizar', methods=['GET', 'POST'])
def actualizar_usuario():
    if request.method == 'GET':
        return render_template('update_user.html')
    else:
        try:
            #Obtengo la información del método post.
            id = request.form['id']
            col = request.form['col']
            valor = request.form['valor']

            #Lo guardo en la DB
            conn = pymysql.connect( 
            host='localhost', 
		    user='lab', 
		    password = "Developer123!", 
		    db='lab_ing_software', 
            ) 

            cur = conn.cursor() 

            cur.execute("update usuarios set " + col + " = '" + valor + "' where idUsuario = '" + id + "'")

        
            conn.commit()
            conn.close() 
            
            return render_template('user_updated.html', id=id, valor = valor)

        except:
            return render_template('error.html')


@usuario_blueprint.route('/eliminar', methods=['GET', 'POST'])
def eliminar_usuario():
    if request.method == 'GET':
        return render_template('delete_user.html')
    else:

        try:
        #Obtengo la información del método post.
            id = request.form['id']
        

        #Lo guardo en la DB
            conn = pymysql.connect( 
            host='localhost', 
		    user='lab', 
		    password = "Developer123!", 
		    db='lab_ing_software', 
            ) 
      
            cur = conn.cursor() 
      
            cur.execute("delete from usuarios where idUsuario = " + id)

        
            conn.commit()
            conn.close() 
        
            return render_template('user_deleted.html', id=id)

        except:
            return render_template('error_eliminar.html')

@usuario_blueprint.route('/leer', methods=['GET', 'POST'])
def leer_usuario():
    try:
        conn = pymysql.connect( 
        host='localhost', 
    	user='lab', 
        password = "Developer123!", 
	    db='lab_ing_software', 
        ) 
    
        cur = conn.cursor() 

        cur.execute("select * from usuarios") 

        output = cur.fetchall() 


        l = list()
        for i in output: 
            l.append(i)


        
        conn.commit()
        conn.close() 
        
        return render_template('user_read.html', list = l)
    except:
        return render_template('error.html')

 
