# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

# Read the number of rooms
k = int(input())

# Create a defaultdict to store the number of people in each room
rooms = defaultdict(int)

# Read the list of room numbers
room_numbers = list(map(int, input().split()))

# Count the number of people in each room
for room_number in room_numbers:
    rooms[room_number] += 1

# Find the room with the fewest people
capitain = min(rooms, key=rooms.get)

# Print the room number of the room with the fewest people
print(capitain)
