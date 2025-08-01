def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    number = 1
    room_assignments = []
    for name in names:
        room_assignments.append(f"Hello, {name}! You'll be assigned to room {number}!")
        number += 1
    return room_assignments

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    for room in assign_rooms(names):
        print(room)
