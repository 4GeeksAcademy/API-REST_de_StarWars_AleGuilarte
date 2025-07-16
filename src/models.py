from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = "usuario"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(80), nullable=False)
    nickname: Mapped[str] = mapped_column(String(100), nullable=False)

    favoritos: Mapped[list["Favorito"]] = relationship("Favorito", back_populates="usuario")


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
            "nickname" : self.nickname
        }
    
class Planeta(db.Model):
    __tablename__ = "planeta"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rotation: Mapped[int] = mapped_column(Integer(10))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "rotation": self.rotation
        }
    
class Personaje(db.Model):
    __tablename__ = "personaje"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    planeta_id: Mapped[int] = mapped_column(Integer, ForeignKey("planeta.id"))

    planeta: Mapped["Planeta"] = relationship("Planeta")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }
    
class Favorite(db.Model):
    __tablename__= "favorite"
    id: Mapped[int] = mapped_column(primary_key=True)
    usuario_id: Mapped[int] = mapped_column(Integer, ForeignKey("usuario.id") nullable=False)
    planeta_id: Mapped[int] = mapped_column(Integer, ForeignKey("planeta.id") nullable=True)
    personaje_id: Mapped[int] = mapped_column(Integer, ForeignKey("personaje.id") nullable=True)

    usuario: Mapped["Usuario"] = relationship("Usuario", back_populates="favoritos")
    planeta: Mapped["Planeta"] = relationship("Planeta")
    personaje: Mapped["Personaje"] = relationship("Personaje")
    
