from sqlalchemy.orm import Session # type: ignore
from models import Team, engine

class TeamManager:
    def __init__(self):
        self.session = Session(bind=engine)

    def create_team(self, name, sport_type, location):
        team = Team(name=name, sport_type=sport_type, location=location)
        self.session.add(team)
        self.session.commit()
        print(f"Team '{name}' created.")

    def view_teams(self):
        teams = self.session.query(Team).all()
        if not teams:
            print("No teams available.")
        else:
            for team in teams:
                print(f"ID: {team.id}, Name: {team.name}, Sport: {team.sport_type}, Location: {team.location}")

    def update_team(self, team_id, name=None, sport_type=None, location=None):
        team = self.session.query(Team).filter(Team.id == team_id).first()
        if not team:
            print(f"Team with ID '{team_id}' does not exist.")
            return
        if name:
            team.name = name
        if sport_type:
            team.sport_type = sport_type
        if location:
            team.location = location
        self.session.commit()
        print(f"Team '{team_id}' updated.")

    def delete_team(self, team_id):
        team = self.session.query(Team).filter(Team.id == team_id).first()
        if not team:
            print(f"Team with ID '{team_id}' does not exist.")
            return
        self.session.delete(team)
        self.session.commit()
        print(f"Team '{team_id}' deleted.")

    def search_team(self, name):
        teams = self.session.query(Team).filter(Team.name.like(f'%{name}%')).all()
        if not teams:
            print(f"No teams found with name '{name}'.")
        else:
            for team in teams:
                print(f"ID: {team.id}, Name: {team.name}, Sport: {team.sport_type}, Location: {team.location}")
