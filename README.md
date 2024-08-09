# Computational Biology

This program visualizes the monotonic Boolean functions for a given number of activators and inhibitors in a graphical table format using Tkinter.

## Requirements

- Python 3.x
- Tkinter library (usually included with Python installations)

## How to Run
Run the script in the terminal using the command:  
   ```python computational_biology.py```

## Description

The script defines two main classes:

### ComputationalBiology: Manages the computation and logic for monotonic Boolean functions.  

This the main class it receives the number of activators and inhibitors and creates the desired table.  
First it generates all the possible states.
Then it generates *all* possible boolean interpretations (functions)  
for the received inputs.
Finally, it will use the is monotonic function to mark the monotonic functions.  
How? for each function, we will go through all the inputs that give us 1, and we'll take the state
corresponding to the activators and inhibitors, and we'll check whether a states with more activators
activated or fewer inhibitors activated will give us 1 as well - this will be the monotonicity condition

* Constructor: Initializes activators, inhibitors, states, possible Boolean functions, and monotonic functions.  
* _initialize_states: Generates all possible states given the number of activators and inhibitors.  
* _all_possible_boolean_functions: Generates all possible Boolean functions for the given states.  
* is_monotonic: Checks if a given Boolean function is monotonic.  
* all_monotonic_functions: Filters all possible Boolean functions to find monotonic ones.  
* initialize_table: Populates the table with the computed data.


### GUITable: Manages the graphical representation of the table.

Simple GUI table using tkinter to display the results.

* Constructor: Initializes a grid of labels.
* update_cell: Updates the text or background color of a specific cell.
* update_cell_ultra: A wrapper for update_cell to update the cell text.


## Output
The output is a Tkinter window displaying a table with the following structure:

The first row shows the states in the format activators,inhibitors.
The first column shows the index of the monotonic Boolean functions.
Cells corresponding to active states (value 1 - for the center node) are marked in red.

The program also outputs to the terminal the states, the monotonic functions, 
and the number of monotonic functions found.

for example (0,0,0,0,0,0,1,0,0) means that the gene is activated only when we are at the 6'th state  
which is [2, 0] -> 2 activators and 0 inhibitor,
and we will see it in the tkinter table as a red cell.
