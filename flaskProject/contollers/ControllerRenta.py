from flask import Blueprint, request, render_template, flash, url_for
from random import randint
import pymysql

renta_blueprint = Blueprint('renta', __name__, url_prefix='/renta')

@renta_blueprint.route('/') #localhost:5000/renta/
def ver_rentar():
    return "select * from renta"

#responde a localhost:5000/renta/id/1
@renta_blueprint.route('/id/<int:id_renta>/<string:nombre>') #<tipo:nombre_variable>
def ver_renta_id(id_renta, nombre):
    return f"Se hace el query con el id {id_renta} y el nombre {nombre}"


@renta_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_renta():
    if request.method == 'GET':
        return render_template('add_rent.html')
    else:
        try:
            #Obtengo la información del método post.
            user = request.form['user']
            movie = request.form['movie']

            #Lo guardo en la DB
            conn = pymysql.connect( 
            host='localhost', 
		    user='lab', 
		    password = "Developer123!", 
		    db='lab_ing_software', 
            ) 
      
            cur = conn.cursor() 

            cur.execute("insert into rentar (idUsuario, idPelicula, fecha_renta) values ('" + user  + "', '" + movie + "', '2024-03-18')") 

        
            conn.commit()
            conn.close() 
          
            return render_template('rent_added.html', user=user, movie = movie)

        except:
            return render_template('error.html')




@renta_blueprint.route('/actualizar', methods=['GET', 'POST'])
def actualizar_renta():
    if request.method == 'GET':
        return render_template('update_rent.html')
    else:
            #Obtengo la información del método post.
            id = request.form['id']
            status = request.form['status']
    

            #Lo guardo en la DB
            conn = pymysql.connect( 
            host='localhost', 
		    user='lab', 
		    password = "Developer123!", 
		    db='lab_ing_software', 
            ) 

            cur = conn.cursor() 

            cur.execute("update rentar set estatus = '" + status + "' where idRentar = '" + id + "'")

        
            conn.commit()
            conn.close() 
            
            return render_template('rent_updated.html', id=id, status = status)






@renta_blueprint.route('/leer', methods=['GET', 'POST'])
def leer_renta():
    try:
        conn = pymysql.connect( 
        host='localhost', 
    	user='lab', 
        password = "Developer123!", 
	    db='lab_ing_software', 
        ) 
    
        cur = conn.cursor() 

        cur.execute("select * from rentar") 

        output = cur.fetchall() 


        l = list()
        for i in output: 
            l.append(i)

        vencidas = list()
        cur.execute("select * from rentar where fecha_renta < now() - interval (dias_de_renta + 1) day") 
        output = cur.fetchall() 

        for i in output: 
            vencidas.append(i)
            l.remove(i)





        
        conn.commit()
        conn.close() 
        
        return render_template('rent_read.html', l = l, vencidas = vencidas)
    except:
        return render_template('error.html')

 
