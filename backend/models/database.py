from flask_sqlalchemy import SQLAlchemy
from config.settings import DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Enum
from sqlalchemy.orm import relationship
db = SQLAlchemy()

def init_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS
    db.init_app(app)


class User(db.Model):
    __tablename__ = 'users'
    email = Column(String(100), primary_key=True, unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    contact = Column(String(15), nullable=False)
    gender = Column(Enum('Male', 'Female', 'Other'), nullable=False)
    password = Column(String(255), nullable=False)
    
    personal_info = relationship("PersonalInfo", back_populates="user", uselist=False, cascade="all, delete")
    travel_history = relationship("TravelHistory", back_populates="user", cascade="all, delete")

class PersonalInfo(db.Model):
    __tablename__ = 'personal_info'
    email = Column(String(100), ForeignKey('users.email'), primary_key=True)
    home_city = Column(String(100), nullable=False)
    current_city = Column(String(100), nullable=False)
    interests = Column(String(255), nullable=False)  # Comma-separated values
    solo_or_group = Column(Enum('Solo', 'Group'), nullable=False)
    avoidables = Column(String(255), nullable=True)  # Comma-separated values
    
    user = relationship("User", back_populates="personal_info")

class TravelHistory(db.Model):
    __tablename__ = 'travel_history'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), ForeignKey('users.email'), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    place_visited = Column(String(255), nullable=False)
    budget_per_person = Column(Integer, nullable=False)
    companions = Column(Integer, nullable=False)
    
    user = relationship("User", back_populates="travel_history")
