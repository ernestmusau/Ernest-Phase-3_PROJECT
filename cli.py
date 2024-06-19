from team_manager import TeamManager

class CLI:
    def __init__(self):
        self.team_manager = TeamManager()

    def display_menu(self):
        print("Sports Team Manager")
        print("1. Create a new team")
        print("2. View all teams")
        print("3. Search for a team")
        print("4. Update a team")
        print("5. Delete a team")
        print("6. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Choose an option: ")

            if choice == '1':
                self.create_team()
            elif choice == '2':
                self.view_teams()
            elif choice == '3':
                self.update_team()
            elif choice == '4':
                self.delete_team()
            elif choice == '5':
                self.search_team()
            elif choice == '6':
                print("The program has been exited")
                break
            else:
                print("Invalid choice, please try again.")

    def create_team(self):
        name = input("Enter team name: ")
        sport_type = input("Enter sport type: ")
        location = input("Enter location: ")
        self.team_manager.create_team(name, sport_type, location)

    def view_teams(self):
        self.team_manager.view_teams()

    def update_team(self):
        team_id = int(input("Enter team ID to update: "))
        name = input("Enter new name (leave blank to keep current): ")
        sport_type = input("Enter new sport type (leave blank to keep current): ")
        location = input("Enter new location (leave blank to keep current): ")
        self.team_manager.update_team(team_id, name or None, sport_type or None, location or None)

    def delete_team(self):
        team_id = int(input("Enter team ID to delete: "))
        self.team_manager.delete_team(team_id)

    def search_team(self):
        name = input("Enter team name to search: ")
        self.team_manager.search_team(name)
