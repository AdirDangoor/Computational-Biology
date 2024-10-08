import tkinter as tk


class GUITable:
    def __init__(self, master, rows, columns):
        self.cells = []
        for i in range(rows):
            row = []
            for j in range(columns):
                cell = tk.Label(master, text=".", width=10, height=1, borderwidth="1", relief="solid")
                cell.grid(row=i, column=j)
                row.append(cell)
            self.cells.append(row)

    def update_cell(self, row, column, value=None):
        if 0 <= row < len(self.cells) and 0 <= column < len(self.cells[0]):
            # If a value is provided, update the text; otherwise, change the background to red.
            if value:
                self.cells[row][column].config(text=value)
            else:
                self.cells[row][column].config(bg='red')

    def update_cell_ultra(self, row, column, value):
        self.update_cell(row, column, value)


class ComputationalBiology:
    def __init__(self, activators_count, inhibitors_count, master=None):
        self.activators_count = activators_count
        self.inhibitors_count = inhibitors_count

        self.states = self._initialize_states()
        self.all_functions = self._all_possible_boolean_functions()

        self.monotonic_functions = self.all_monotonic_functions()
        self.table = GUITable(master, len(self.monotonic_functions)+1, len(self.states)+1)

    def _initialize_states(self):
        """
        Initialize all possible states for the given number of activators and inhibitors
        the format of the states is [active_activators, active_inhibitors]
        """
        states = []  # List of [active_activators, active_inhibitors]
        for i in range(self.activators_count + 1):
            for j in range(self.inhibitors_count + 1):
                states.append([i, j])

        print("states are in format of [active_activators, active_inhibitors], "
              "for example [0, 1] means 0 activators and 1 inhibitors are active")
        print(f"states: {states}")
        return states

    def _all_possible_boolean_functions(self):
        """
        Generate all possible boolean functions for the given number of activators and inhibitors
        """
        from itertools import product
        # Number of states is (activators_count + 1) * (inhibitors_count + 1)
        num_states = (self.activators_count + 1) * (self.inhibitors_count + 1)
        # Generate all possible boolean functions for the given number of states
        boolean_functions = list(product([0, 1], repeat=num_states))
        return boolean_functions

    def is_monotonic(self, function):
        """
        for each function, we will go through all the inputs that give us 1, and we'll take the state
        corresponding to the activators and inhibitors, and we'll check whether a states with more activators
        activated or fewer inhibitors activated will give us 1 as well - this will be the increasing monotonicity
        """
        for i in range(len(function)):
            if function[i] == 1:
                # get the state corresponding to the index i
                state = self.states[i]
                activators = state[0]
                inhibitors = state[1]
                for state in self.states:
                    if (state[0] == activators and state[1] <= inhibitors) or (state[0] >= activators and state[1] == inhibitors):
                        if function[self.states.index(state)] != 1:
                            return False
        return True

    def all_monotonic_functions(self):
        """
        Get all monotonic functions from the list of all possible functions
        The monotonic function format is a list of 0s and 1s, where 1 means that the state do activate the gene
        The state are in the order of the self.states list
        """
        print("\nMonotonic function is a list of 0s and 1s, where 1 means that the state do activate the gene\n"
              "for example (0,0,0,0,0,0,1,0,0) means that the gene is activated only when we are at the 6'th state\n"
              "which is [2, 0] -> 2 activators and 0 inhibitors\n")
        all_mono_functions = []
        for function in self.all_functions:
            if self.is_monotonic(function):
                all_mono_functions.append(function)

        # remove the constant functions for the generic case
        all_mono_functions = [function for function in all_mono_functions if 1 in function]
        all_mono_functions = [function for function in all_mono_functions if 0 in function]

        for i in range(len(all_mono_functions)):
            print(f"Monotonic function number {i}: {all_mono_functions[i]}")
        print("Monotonic functions length: ", len(all_mono_functions))
        return all_mono_functions

    def initialize_table(self):
        for state in self.states:
            self.table.update_cell_ultra(0, self.states.index(state)+1, f"{state[0]},{state[1]}")

        for i in range(len(self.monotonic_functions)):
            self.table.update_cell_ultra(i+1, 0, f"{i}")

        for i in range(len(self.monotonic_functions)):
            for j in range(len(self.states)):
                if self.monotonic_functions[i][j] == 1:
                    self.table.update_cell(i+1, j+1)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Computational Biology Table")
    cb = ComputationalBiology(2, 2, root)
    cb.initialize_table()
    root.mainloop()
