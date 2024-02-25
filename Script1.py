import pymysql 
  
def insertaEnTodas(): 
    conn = pymysql.connect( 
        host='localhost', 
		user='lab', 
		password = "Developer123!", 
		db='lab_ing_software', 
        ) 
      
    cur = conn.cursor() 
      
    cur.execute("insert into usuarios (nombre, apPat, password) values ('Juan', 'apPat', '1234')") 
    cur.execute("insert into peliculas (nombre) values ('Batman')") 

    cur.execute("select idUsuario from usuarios") 
    output = cur.fetchall() 
    idUsuario = output[0][0]

    cur.execute("select idPelicula from peliculas") 
    output = cur.fetchall() 
    idPelicula = output[0][0]

    cur.execute("insert into rentar (idUsuario, idPelicula, fecha_renta) values (" + str(idUsuario) + ", " + str(idPelicula) + ", '2024-02-20')") 

    conn.commit()




    output = cur.fetchall() 
      
    for i in output: 
        print(i) 
      
    conn.close() 


def filtra(cadena): 
    conn = pymysql.connect( 
        host='localhost', 
		user='lab', 
		password = "Developer123!", 
		db='lab_ing_software', 
        ) 
      
    cur = conn.cursor() 
      

    cur.execute("select * from usuarios where apPat like '%" + cadena + "' or apMat like '%" + cadena + "'")
    


    conn.commit()




    output = cur.fetchall() 
      
    for i in output: 
        print(i) 
      
    conn.close() 


def cambiaGenero(pelicula, genero): 
    conn = pymysql.connect( 
        host='localhost', 
		user='lab', 
		password = "Developer123!", 
		db='lab_ing_software', 
        ) 
      
    cur = conn.cursor() 
      


    cur.execute("update peliculas set genero = '" + genero + "' where nombre = '" + pelicula + "'")



    conn.commit()




    output = cur.fetchall() 
      
    for i in output: 
        print(i) 
      
    conn.close() 



def eliminaRenta(): 
    conn = pymysql.connect( 
        host='localhost', 
		user='lab', 
		password = "Developer123!", 
		db='lab_ing_software', 
        ) 
      
    cur = conn.cursor() 
      

    cur.execute("delete from rentar where fecha_renta < now() - interval 4 day")



    conn.commit()




    output = cur.fetchall() 
      
    for i in output: 
        print(i) 
      
    conn.close() 


