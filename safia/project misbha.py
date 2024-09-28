# Initialize an empty list to store the cultural exchange programs
cultural_exchange_programs = []

# Function to create a new program (C - Create)
def create_program(program_name, country, duration, participants):
    program = {
        'program_name': program_name,
        'country': country,
        'duration': duration,  # in weeks
        'participants': participants  # list of participant names
    }
    cultural_exchange_programs.append(program)
    print(f"Program '{program_name}' created successfully!")

# Function to read/display all programs (R - Read)
def display_programs():
    if not cultural_exchange_programs:
        print("No programs available.")
    else:
        for i, program in enumerate(cultural_exchange_programs, start=1):
            print(f"\nProgram {i}:")
            print(f"Name: {program['program_name']}")
            print(f"Country: {program['country']}")
            print(f"Duration: {program['duration']} weeks")
            print(f"Participants: {', '.join(program['participants'])}")

# Function to update a program's details (U - Update)
def update_program(program_name, key_to_update, new_value):
    for program in cultural_exchange_programs:
        if program['program_name'] == program_name:
            if key_to_update in program:
                program[key_to_update] = new_value
                print(f"Program '{program_name}' updated successfully!")
            else:
                print(f"Invalid key '{key_to_update}'")
            return
    print(f"Program '{program_name}' not found.")

# Function to delete a program (D - Delete)
def delete_program(program_name):
    for program in cultural_exchange_programs:
        if program['program_name'] == program_name:
            cultural_exchange_programs.remove(program)
            print(f"Program '{program_name}' deleted successfully!")
            return
    print(f"Program '{program_name}' not found.")

# Sample interaction
# Creating a program
create_program("Youth Cultural Exchange", "Japan", 4, ["Alice", "Bob", "Charlie"])
create_program("Educational Exchange Program", "France", 6, ["David", "Eva", "Frank"])

# Displaying all programs
display_programs()

# Updating a program
update_program("Youth Cultural Exchange", "duration", 5)

# Display programs again to see updates
display_programs()

# Deleting a program
delete_program("Educational Exchange Program")

# Display programs after deletion
display_programs()
