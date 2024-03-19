from sqlalchemy import Column, Integer, String

from alchemyClasses import db


class Usuario(db.Model):

    __tablename__ = 'usuario'
    id_usuario = Column(Integer, primary_key=True, auto_increment=True)
    nombre = Column(String(200))
    ap_pat = Column(String(200))
    ap_mat = Column(String(200), nullable=True)
    password = Column(String(64))
    email = Column(String(500), nullable=True, unique_key=True)
    profilePicture = Column(longblob, nullable=True)



    def __init__(self, nombre, apPat, password, apMat=None, email = None, profilePicture = None):
        self.nombre = nombre
        self.ap_pat = apPat
        self.ap_mat = apMat
        self.password = password

    def __str__(self):
        return f'Nombre:{self.nombre}\nEmail:{self.nemail}'