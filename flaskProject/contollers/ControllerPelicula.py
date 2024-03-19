from flask import Blueprint, request, render_template, flash, url_for
from random import randint
import pymysql

pelicula_blueprint = Blueprint('pelicula', __name__, url_prefix='/pelicula')

@pelicula_blueprint.route('/') #localhost:5000/pelicula/
def ver_peliculas():
    return "select * from pelicula"

#responde a localhost:5000/pelicula/id/1
@pelicula_blueprint.route('/id/<int:id_pelicula>/<string:nombre>') #<tipo:nombre_variable>
def ver_pelicula_id(id_pelicula, nombre):
    return f"Se hace el query con el id {id_pelicula} y el nombre {nombre}"


@pelicula_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_pelicula():
    try:
        if request.method == 'GET':
            return render_template('add_movie.html')
        else:
        
                #Obtengo la información del método post.
                name = request.form['name']

                #Lo guardo en la DB
                conn = pymysql.connect( 
                host='localhost', 
	    	    user='lab', 
		        password = "Developer123!", 
		        db='lab_ing_software', 
                ) 
      
                cur = conn.cursor() 

                cur.execute("insert into peliculas (nombre) values ('" + name  + "')") 

        
                conn.commit()
                conn.close() 
           
                return render_template('movie_added.html', name=name)

    except:
        return render_template('error.html')

        


@pelicula_blueprint.route('/actualizar', methods=['GET', 'POST'])
def actualizar_pelicula():
    if request.method == 'GET':
        return render_template('update_movie.html')
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

            cur.execute("update peliculas set " + col + " = '" + valor + "' where idpelicula = '" + id + "'")

        
            conn.commit()
            conn.close() 
            
            return render_template('movie_updated.html', id=id, valor = valor)

        except:
            return render_template('error.html')


@pelicula_blueprint.route('/eliminar', methods=['GET', 'POST'])
def eliminar_pelicula():
    if request.method == 'GET':
        return render_template('delete_movie.html')
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
      
            cur.execute("delete from peliculas where idpelicula = " + id)

        
            conn.commit()
            conn.close() 
       
            return render_template('movie_deleted.html', id=id)

        except:
            return render_template('error_eliminar.html')

@pelicula_blueprint.route('/leer', methods=['GET', 'POST'])
def leer_pelicula():
    try:
        conn = pymysql.connect( 
        host='localhost', 
    	user='lab', 
        password = "Developer123!", 
	    db='lab_ing_software', 
        ) 
    
        cur = conn.cursor() 

        cur.execute("select * from peliculas") 

        output = cur.fetchall() 


        l = list()
        for i in output: 
            l.append(i)


        
        conn.commit()
        conn.close() 
            
        return render_template('movie_read.html', list = l)
    except:
        return render_template('error.html')

 
