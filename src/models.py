import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id_user = Column(Integer, primary_key=True)
    password = Column(Integer, nullable=False)
    user_name = Column(String(50), nullable=False)
    full_name = Column(String(150), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(Integer, nullable=False)
    relation_favorite = relationship('Favorite', backref='user')

class People(Base):
    __tablename__ = 'people'
    id_people = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    height = Column(String(20), nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(10), nullable=False)
    skin_color = Column(String(20), nullable=False)
    eye_color = Column(String(10), nullable=False)
    birth_year = Column(String(10), nullable=False)
    gender = Column(String(10), nullable=False)
    created = Column(String(100), nullable=False)
    edited = Column(String(100), nullable=False)
    homeworld = Column(String(100), nullable=False)
    url = Column(String(250), nullable=False)
    relation_favorite = relationship('Favorite', backref='people')
    relation_film = relationship('Film', backref='people')
    relation_starship = relationship('Sharship', backref='people')
    relation_specie = relationship('Specie', backref='people')


class Vehicle(Base):
    __tablename__ = 'vehicle'
    id_vehicle = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    vehicle_class = Column(String(50), nullable=False)
    manufacturer = Column(String(100), nullable=False)
    cost_in_credits = Column(Integer, nullable=False)
    length = Column(String(10), nullable=False)
    crew = Column(Integer, nullable=False)
    passengers = Column(Integer, nullable=False)
    max_atmosphering_speed = Column(Integer, nullable=False)
    cargo_capacity = Column(Integer, nullable=False)
    consumables = Column(String(50), nullable=False)
    films = relationship('Relation_film_and_vehicle', backref='vehicle')
    pilots = Column(Integer, ForeignKey('people.id_people'))
    created = Column(String(100), nullable=False)
    edited = Column(String(100), nullable=False)
    url = Column(String(250), nullable=False)
    relation_favorite = relationship('Favorite', backref='vehicle')


class Planet(Base):
    __tablename__ = 'planet'
    id_planet = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    diameter = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    gravity = Column(String(50), nullable=False)
    population = Column(String(50), nullable=False)
    climate = Column(String(50), nullable=False)
    terrain = Column(String(100), nullable=False)
    surface_water = Column(String(100), nullable=False)
    created = Column(String(100), nullable=False)
    edited = Column(String(100), nullable=False)
    url = Column(String(100), nullable=False)
    relation_favorite = relationship('Favorite', backref='planet')
    relation_films = relationship('Films', backref='planet')
    relation_specie = relationship('Specie', backref='planet')

class Sharship(Base):
    __tablename__='sharship'
    id_sharship = Column(Integer, primary_key=True)
    MGLT = Column(String(250), nullable=False)
    cargo_capacity = Column(String(250), nullable=False)
    consumables = Column(String(250), nullable=False)
    cost_in_credits = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    crew = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)
    hyperdrive_rating = Column(String(250), nullable=False)
    length = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    max_atmosphering_speed = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    passengers = Column(String(250), nullable=False)
    pilots = Column(Integer, ForeignKey('people.id_people'))
    starship_class = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    films = relationship('relation_film_and_starship', backref='sharship')
    relation_favorite = relationship('Favorite', backref='sharship')

class Specie(Base):
    __tablename__='specie'
    id_specie = Column(Integer, primary_key=True)
    average_height = Column(Integer, nullable=False)
    average_lifespan = Column(Integer, nullable=False)
    classification = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    designation = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)
    eye_colors = Column(String(250), nullable=False)
    hair_colors = Column(String(250), nullable=False)
    homeworld = Column(Integer, ForeignKey('planet.id_planet'))
    language = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    people = Column(Integer, ForeignKey('people.id_people'))
    films = species = relationship('Relation_film_and_specie', backref='specie')
    skin_colors = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    relation_films = relationship('Films', backref='specie')
    relation_favorite = relationship('Favorite', backref='specie')



class Films(Base):
    __tablename__='films'
    id_films = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    characters = Column(Integer, ForeignKey('people.id_people'))
    created = Column(String(250), nullable=False)
    director = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)
    episode_id = Column(String(250), nullable=False)
    opening_crawl = Column(String(250), nullable=False)
    planets = Column(Integer, ForeignKey('planet.id_planet'))
    producer = Column(String(250), nullable=False)
    release_date = Column(String(250), nullable=False)
    species = relationship('Relation_film_and_specie', backref='films')
    starships = relationship('relation_film_and_starship', backref='films')
    url = Column(String(250), nullable=False)
    vehicles = relationship('Relation_film_and_vehicle', backref='films')
    relation_favorite = relationship('Favorite', backref='films')


class Favorite(Base):
    __tablename__ = 'favorite'
    id_favorite = Column(Integer, primary_key=True)
    user_people = Column(Integer, ForeignKey('user.id_user'))
    relation_people = Column(Integer, ForeignKey('people.id_people'))
    relation_vehicle = Column(Integer, ForeignKey('vehicle.id_vehicle'))
    relation_planet = Column(Integer, ForeignKey('planet.id_planet'))
    relation_sharship = Column(Integer, ForeignKey('sharship.id_sharship'))
    relation_specie = Column(Integer, ForeignKey('specie.id_specie'))
    relation_films = Column(Integer, ForeignKey('films.id_films'))
    
    def to_dict(self):
        return {}

class relation_film_and_starship(Base):
    __tablename__ = 'films_and_starship'
    id = Column(Integer, primary_key=True)
    id_starship = Column(Integer, ForeignKey('sharship.id_sharship'))
    id_film = Column(Integer, ForeignKey('films.id_films'))

class Relation_film_and_vehicle(Base):
    __tablename__ = 'films_and_vehicle'
    id = Column(Integer, primary_key=True)
    id_starship = Column(Integer, ForeignKey('vehicle.id_vehicle'))
    id_film = Column(Integer, ForeignKey('films.id_films'))

class Relation_film_and_specie(Base):
    __tablename__ = 'films_and_specie'
    id = Column(Integer, primary_key=True)
    id_starship = Column(Integer, ForeignKey('specie.id_specie'))
    id_film = Column(Integer, ForeignKey('films.id_films'))

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e