### import useful python ORM tools ###
### importance: ignore             ###
import sqlalchemy as alch
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

### create a database and the base class for our ORMs ###
### importance: ignore                                ###
engine = alch.create_engine("sqlite:///shelters.db", echo=False)
Base = declarative_base()


### define our ORMs  ###
### importance: high ###

## the animal class ##
class Animal(Base):
    # tells our database what it should call this table #
    __tablename__ = "animals"

    # create some columns, where the name column is the main identifier #
    name = alch.Column(alch.String, primary_key=True)
    age = alch.Column(alch.Integer)
    fav_food = alch.Column(alch.String)
    
    # link animal to the shelter it resides in by storing the name of the #
    # shelter, as well as a relationship directly to the shelter object   #
    shelter_name = alch.Column(alch.String, alch.ForeignKey("shelters.name"))
    shelter = relationship("Shelter", back_populates="animals")

    def __repr__(self):
        name, age, fav_food = self.name, self.age, self.fav_food
        return f"Animal(name='{name}', age={age}, fav_food='{fav_food}')"

## the shelter class ##
class Shelter(Base):
    # tells our database what it should call this table #
    __tablename__ = "shelters"

    # create some columns, where the name column is the main identifier #
    name = alch.Column(alch.String, primary_key=True)
    address = alch.Column(alch.String)

    # link shelter to the animals that reside in it; implicitly looks for  #
    # all the animals whose shelter_name property is the same as self.name #
    animals = relationship("Animal", back_populates="shelter")
    
    def __repr__(self):
        name, addr = self.name, self.address
        return f"Shelter(name='{name}', address='{addr}')"


### prepare our database to handle all of our ORMs ###
### importance: ignore                             ###
Base.metadata.create_all(engine)


### create a session that can convert between our ORMs and the database ###
### importance: ignore                                                  ###
Session = sessionmaker(bind=engine)
session = Session()