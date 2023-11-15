import random
from tkinter import StringVar, Label, Tk, Entry

# Create the main window
window = Tk()
window.geometry("400x100")
window.title("Monty Hall Simulation")
window.resizable(0, 0)

# Initialize variables to hold the result counts
same_choice = StringVar()
switched_choice = StringVar()
same_choice.set(0)
switched_choice.set(0)

# Create an Entry widget for user to input number of samples
no_sample = Entry()

# Place labels and Entry widgets in the window
Label(text="Same choice").place(x=80, y=8)
Label(text="Switched choice").place(x=80, y=40)
Label(textvariable=same_choice, font=(15)).place(x=180, y=8)
Label(textvariable=switched_choice, font=(15)).place(x=180, y=40)
no_sample.place(x=100, y=70)

def simulate(event):
    # Initialize result counters
    same_choice_result = 0
    switched_choice_result = 0
    
    # Get the number of samples from the user input
    samples = int(no_sample.get())
    
    # Possible door outcomes
    doors = ["gold", "goat", "bed"]
    
    # Perform simulations
    for _ in range(samples):
        simulated_doors = doors.copy()
        random.shuffle(simulated_doors)
        
        # Initial choice by the player
        first_choice = random.choice(simulated_doors)
        simulated_doors.remove(first_choice)
        
        # Monty opens a door with a goat
        opened_door = simulated_doors[0] if simulated_doors[0] != "gold" else simulated_doors[1]
        simulated_doors.remove(opened_door)
        
        # Switched choice by the player
        switched_second_choice = simulated_doors[0]
        
        # Update result counts based on outcomes
        if first_choice == "gold":
            same_choice_result += 1
            same_choice.set(same_choice_result)
        elif switched_second_choice == "gold":
            switched_choice_result += 1
            switched_choice.set(switched_choice_result)
        else:
            print("That will never happen")  # Typo corrected here

# Bind the Enter key press to the simulation function
no_sample.bind("<Return>", simulate)

# Start the GUI event loop
window.mainloop()
