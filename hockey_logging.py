import tkinter as tk
import csv

def create_team():
    team_name = team_name_entry.get()
    team_name_label.config(text=f"Team: {team_name}")
    team_name_entry.delete(0, tk.END)

def add_player():
    name = player_name_entry.get()
    goals = int(goals_entry.get())
    assists = int(assists_entry.get())
    player = {
        'Name': name,
        'Goals': goals,
        'Assists': assists
    }
    players.append(player)
    player_listbox.insert(tk.END, f"Name: {name}\tGoals: {goals}\tAssists: {assists}")
    player_name_entry.delete(0, tk.END)
    goals_entry.delete(0, tk.END)
    assists_entry.delete(0, tk.END)

def save_team():
    if team_name_label["text"] != "Team: ":
        filename = team_name_label["text"][6:].lower().replace(" ", "_") + ".csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Name', 'Goals', 'Assists'])
            writer.writeheader()
            writer.writerows(players)
        print("Team statistics saved successfully.")
    else:
        print("Please create a team first.")

def load_team():
    filename = team_name_label["tar heels"][6:].lower().replace(" ", "_") + ".csv"
    players.clear()
    player_listbox.delete(0, tk.END)
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                players.append(row)
                player_listbox.insert(tk.END, f"Name: {row['Name']}\tGoals: {row['Goals']}\tAssists: {row['Assists']}")
        print("Team statistics loaded successfully.")
    except FileNotFoundError:
        print("Team file not found.")

def change_stats():
    selected_player = player_listbox.curselection()
    if selected_player:
        selected_player = selected_player[0]
        player = players[selected_player]
        new_goals = int(goals_entry.get())
        new_assists = int(assists_entry.get())
        player['Goals'] = new_goals
        player['Assists'] = new_assists
        player_listbox.delete(selected_player)
        player_listbox.insert(selected_player, f"Name: {player['Name']}\tGoals: {new_goals}\tAssists: {new_assists}")
        goals_entry.delete(0, tk.END)
        assists_entry.delete(0, tk.END)
        print("Player statistics updated successfully.")
    else:
        print("Please select a player.")

def display_team():
    if players:
        print("\nTeam Statistics:")
        for player in players:
            print(f"Name: {player['Name']}\tGoals: {player['Goals']}\tAssists: {player['Assists']}")
        print()
    else:
        print("No team statistics available.")

# Create the main window
window = tk.Tk()
window.title("Hockey Team Statistics Tracker")

# Create team section
team_frame = tk.Frame(window)
team_frame.pack(pady=10)

team_label = tk.Label(team_frame, text="Team Name:")
team_label.grid(row=0, column=0)

team_name_entry = tk.Entry(team_frame)
team_name_entry.grid(row=0, column=1)

create_team_button = tk.Button(team_frame, text="Create Team", command=create_team)
create_team_button.grid(row=0, column=2)

team_name_label = tk.Label(window, text="Team: ")
team_name_label.pack()

# Create player section
player_frame = tk.Frame(window)
player_frame.pack(pady=10)

player_name_label = tk.Label(player_frame, text="Player Name:")
player_name_label.grid(row=0, column=0)

goals_label = tk.Label(player_frame, text="Goals:")
goals_label.grid(row=0, column=1)

assists_label = tk.Label(player_frame, text="Assists:")
assists_label.grid(row=0, column=2)

player_name_entry = tk.Entry(player_frame)
player_name_entry.grid(row=1, column=0)

goals_entry = tk.Entry(player_frame)
goals_entry.grid(row=1, column=1)

assists_entry = tk.Entry(player_frame)
assists_entry.grid(row=1, column=2)

add_player_button = tk.Button(player_frame, text="Add Player", command=add_player)
add_player_button.grid(row=1, column=3)

# Create player listbox
player_listbox = tk.Listbox(window, width=50)
player_listbox.pack()

# Create action buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

save_button = tk.Button(button_frame, text="Save Team", command=save_team)
save_button.grid(row=0, column=0, padx=10)

load_button = tk.Button(button_frame, text="Load Team", command=load_team)
load_button.grid(row=0, column=1, padx=10)

change_button = tk.Button(button_frame, text="Change Stats", command=change_stats)
change_button.grid(row=0, column=2, padx=10)

display_button = tk.Button(button_frame, text="Display Team", command=display_team)
display_button.grid(row=0, column=3, padx=10)

# Initialize team statistics
players = []

# Run the main window loop
window.mainloop()