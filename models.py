import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, Enum, ForeignKey # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore
from sqlalchemy.orm import relationship, sessionmaker # type: ignore

Base = declarative_base()

class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    sport_type = Column(String, nullable=False)
    location = Column(String, nullable=False)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(Enum('admin', 'manager', name='user_roles'), default='manager')

class UserTeamRelationship(Base):
    __tablename__ = 'user_team_relationship'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    team_id = Column(Integer, ForeignKey('teams.id'), primary_key=True)
    access_level = Column(Enum('view', 'update', 'delete', name='access_levels'), default='view')
    user = relationship(User, back_populates="teams")
    team = relationship(Team, back_populates="users")

User.teams = relationship('UserTeamRelationship', back_populates='user')
Team.users = relationship('UserTeamRelationship', back_populates='team')

def setup_database():
    engine = create_engine('sqlite:///sports_manager.db')
    Base.metadata.create_all(engine)
    return engine

engine = setup_database()
Session = sessionmaker(bind=engine)
