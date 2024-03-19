from alchemyClasses import db
from flask import Column, Integer, ForeignKey, DateTime
from datetime import date

class Inscripcion(db.Model):

    __tablename__ = 'inscripcion'
    id_inscripcion = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))
    id_clase = Column(Integer, ForeignKey('clase.id_clase'))
    fecha = Column(DateTime, nullable=True)

    def __init__(self, id_usuario, id_clase, fecha=date.today()):
        self.id_usuario = id_usuario
        self.id_clase = id_clase
        self.fecha = fecha

    def __str__(self):
        #Que regrese el nombre del usuario y que regrese el nombre de la clase.
        return f"usuario: {}\nClase: {}\nFecha: {self.fecha}"