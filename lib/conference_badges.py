def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badge_messages = []
    for name in names:
        badge_messages.append(badge_maker(name))
    return badge_messages

def assign_rooms(names):
    room_assignments = []
    for i, speaker in enumerate(names, start=1):
        room_assignments.append(f"Hello, {speaker}! You'll be assigned to room {i}!")
    return room_assignments

def printer(names):
    badge_messages = batch_badge_creator(names)
    room_assignments = assign_rooms(names)
    
    for badge_message in badge_messages:
        print(badge_message)
    
    for room_assignment in room_assignments:
        print(room_assignment)
