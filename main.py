from itertools import combinations
import tkinter as tk
#
# class Table:
#     def __init__(self, rows, columns):
#         self.rows = rows
#         self.columns = columns
#         self.table = [["." for _ in range(columns)] for _ in range(rows)]
#
#     def update_cell(self, row, column):
#         if 0 <= row < self.rows and 0 <= column < self.columns:
#             self.table[row][column] = "X"
#         else:
#             print("Invalid row or column index")
#
#     def update_cell_ultra(self, row, column, value):
#         if 0 <= row < self.rows and 0 <= column < self.columns:
#             self.table[row][column] = value
#         else:
#             print("Invalid row or column index")
#
#     def display(self):
#         for row in self.table:
#             print("|" + "|".join(row) + "|")


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
        self.states = self.initialize_states()
        self.regulations = self.generate_regulations()
        self.table = GUITable(master, len(self.regulations)+1, len(self.states)+1)

    def initialize_states(self):
        states = []  # List of [active_activators, active_inhibitors]
        for i in range(self.activators_count + 1):
            for j in range(self.inhibitors_count + 1):
                states.append([i, j])

        print(states)
        return states


    def generate_regulations(self):
        """
        each regulation is a tuple of 2 elements, each element is a list of 2 elements
        the first list contains [max_activators, max_inhibitors]
        the second list contains the monotonicity of the regulation [activators, inhibitors]
        example: [ [2, 1], [1, 1] ] allows 0 to 2 activators OR 0 to 1 inhibitor,
        and the [1,1] allows 1 activator and 1 inhibitor simultaneously
        """
        regulations = []
        for i in range(self.activators_count + 1):
            for j in range(self.inhibitors_count + 1):
                for k in range(i + 1):
                    for l in range(j + 1):
                        if k == 0 and l == 0:
                            regulations.append([[i, j], [k, l]])
                        if k == 0 or l == 0:
                            continue
                        regulations.append([[i, j], [k, l]])
        print("Regulations length: ", len(regulations))
        return regulations

    def run_regulation_on_states(self):
        for state in self.states:
            self.table.update_cell_ultra(0, self.states.index(state)+1, f"{state[0]},{state[1]}")

        for i in range(len(self.regulations)):
            self.table.update_cell_ultra(i+1, 0, f"{i}")

        for __state in self.states:
            state = [self.activators_count-__state[0], __state[1]]

            for regulation in self.regulations:
                if state[0] == self.activators_count and state[1] == self.inhibitors_count:
                    continue
                if state[0] == 0 or state[1] == 0:
                    if regulation[0][0] >= state[0] and regulation[0][1] >= state[1]:
                        self.table.update_cell(self.regulations.index(regulation)+1, self.states.index(__state)+1)
                        # print(f"True 1 : {__state}, {regulation}")

                else:
                    if regulation[1][0] >= state[0] and regulation[1][1] >= state[1]:
                        self.table.update_cell(self.regulations.index(regulation)+1, self.states.index(__state)+1)
                        # print(f"True 2 : {__state}, {regulation}")





if __name__ == "__main__":
    root = tk.Tk()
    root.title("Computational Biology Table")
    cb_gui = ComputationalBiology(3, 2, root)
    cb_gui.run_regulation_on_states()
    root.mainloop()