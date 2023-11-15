# Monty Hall Simulation

This Python script simulates the Monty Hall problem, a probability puzzle involving decision-making and switching choices. It demonstrates the tkinter library for creating a simple graphical user interface (GUI) to run the simulation and visualize the results.

## Usage

1. Make sure you have Python and the tkinter library installed.

2. Open the Python script file `MontyHallSimulation.py` in your preferred Python environment.

3. Run the script.

4. A GUI window will appear with labels displaying the counts of successful outcomes for both keeping the initial choice and switching the choice.

5. Enter the desired number of simulation samples in the input field.

6. Press the `Enter` key to run the simulations and update the results.

## Code Explanation

The script uses the tkinter library to create a GUI window for user interaction. Labels and an Entry widget are placed in the window to display the simulation results and input the number of samples.

The `simulate` function performs the Monty Hall simulations based on the user-provided number of samples. It updates the result counts and displays them in the GUI.

The script binds the `Return` key press event to the `simulate` function, allowing the user to trigger simulations by pressing `Enter`.

## Example

After entering the number of samples and pressing `Enter`, the GUI will display the counts of successful outcomes for keeping the initial choice and switching the choice.

Same choice: 329
Switched choice: 671


## Contributing

Contributions to this project are welcome! Feel free to open issues and submit pull requests if you have any improvements or suggestions.
