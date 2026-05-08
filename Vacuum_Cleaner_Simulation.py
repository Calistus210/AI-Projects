# Vacuum Cleaner Agent Simulation

# Environment
rooms = {
    'A': 'Dirty',
    'B': 'Dirty'
}

# Vacuum agent location
current_room = 'A'

def clean_room(room):
    global rooms

    if rooms[room] == 'Dirty':
        print(f"Room {room} is Dirty.")
        print(f"Cleaning Room {room}...")
        rooms[room] = 'Clean'
    else:
        print(f"Room {room} is already Clean.")

# Run agent
for room in rooms:

    current_room = room

    print(f"\nVacuum Agent enters Room {room}")

    clean_room(room)

print("\nFinal Room Status:")
print(rooms)