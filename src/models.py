from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    nickname: Mapped[str] = mapped_column(String(100), nullable=False)
    favorites: Mapped[list["Favorites"]] = relationship ("Favorites", back_populates="user")
    


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
            "nickname": self.nickname,
        }


class Planet(db.Model):
    __tablename__ = "planet"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }


class Characters(db.Model):
    __tablename__ = "characters"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    planet_id: Mapped[int] = mapped_column(Integer, ForeignKey("planet.id"))
    planet: Mapped["Planet"] = relationship ("Planet")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }
class Favorites(db.Model):
    __tablename__ = "favorites"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"), nullable=False)
    planet_id: Mapped[int] = mapped_column(Integer, ForeignKey("planet.id"), nullable=True)
    character_id: Mapped[int] = mapped_column(Integer, ForeignKey("character.id"), nullable=True)
    user: Mapped["User"] = relationship ("User", back_populates="user")
    planet: Mapped["Planet"] = relationship ("Planet")
    characters: Mapped["Characters"] = relationship ("Characters")