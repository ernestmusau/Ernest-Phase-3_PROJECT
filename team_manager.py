import sqlite3
from db import get_db_connection

class TeamManager:
    def __init__(self):
        self.conn = get_db_connection()

    def create_team(self, name, sport_type, location):
        with self.conn:
            self.conn.execute(
                "INSERT INTO teams (name, sport_type, location) VALUES (?, ?, ?)",
                (name, sport_type, location)
            )
        print(f"Team '{name}' created.")

    def view_teams(self):
        teams = self.conn.execute("SELECT * FROM teams").fetchall()
        if not teams:
            print("No teams available.")
        else:
            for team in teams:
                print(f"ID: {team['id']}, Name: {team['name']}, Sport: {team['sport_type']}, Location: {team['location']}")

    def update_team(self, team_id, name=None, sport_type=None, location=None):
        team = self.conn.execute("SELECT * FROM teams WHERE id = ?", (team_id,)).fetchone()
        if not team:
            print(f"Team with ID '{team_id}' does not exist.")
            return
        name = name if name else team['name']
        sport_type = sport_type if sport_type else team['sport_type']
        location = location if location else team['location']
        with self.conn:
            self.conn.execute(
                "UPDATE teams SET name = ?, sport_type = ?, location = ? WHERE id = ?",
                (name, sport_type, location, team_id)
            )
        print(f"Team '{team_id}' updated.")

    def delete_team(self, team_id):
        with self.conn:
            result = self.conn.execute("DELETE FROM teams WHERE id = ?", (team_id,))
            if result.rowcount == 0:
                print(f"Team with ID '{team_id}' does not exist.")
            else:
                print(f"Team '{team_id}' deleted.")

    def search_team(self, name):
        teams = self.conn.execute("SELECT * FROM teams WHERE name LIKE ?", ('%' + name + '%',)).fetchall()
        if not teams:
            print(f"No teams found with name '{name}'.")
        else:
            for team in teams:
                print(f"ID: {team['id']}, Name: {team['name']}, Sport: {team['sport_type']}, Location: {team['location']}")
