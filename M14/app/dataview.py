from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import read_csv
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Advanced Data Viewer")
        self.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Button to load data file
        self.load_button = Button(self, text="Load Data File", command=self.load_file)
        self.load_button.pack(side=TOP, pady=10)

        # Canvas for matplotlib plot
        self.canvas = Canvas(self, bg='white', width=800, height=600)
        self.canvas.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Treeview for displaying CSV data
        self.tree = Treeview(self)
        self.tree.pack(fill=BOTH, expand=True, padx=10, pady=10)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.data = read_csv(file_path)
            self.display_csv()
            self.plot_data()

    def display_csv(self):
        # Clear previous treeview content
        for i in self.tree.get_children():
            self.tree.delete(i)

        # Set up new treeview columns
        self.tree["columns"] = self.data.columns.tolist()
        self.tree["show"] = "headings"
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)

        # Insert data into treeview
        for index, row in self.data.iterrows():
            self.tree.insert("", "end", values=list(row))

    def plot_data(self):
        fig, ax = plt.subplots(figsize=(10, 8))
        if len(self.data.columns) > 1:
            # Using seaborn for regression plot
            sns.regplot(x=self.data.columns[0], y=self.data.columns[1], data=self.data, ax=ax, color='green')
            ax.set_xlabel(self.data.columns[0])
            ax.set_ylabel(self.data.columns[1])
            ax.set_title("Regression Plot")
            ax.grid(True)

            # Displaying statistics
            fig.text(0.99, 0.01, f'Mean: {np.mean(self.data[self.data.columns[1]]):.2f}\nStd Dev: {np.std(self.data[self.data.columns[1]]):.2f}', horizontalalignment='right')
        
        self.show_plot(fig)

    def show_plot(self, fig):
        # Clear previous canvas
        for widget in self.canvas.winfo_children():
            widget.destroy()

        # Create a new canvas and embed the plot
        canvas = FigureCanvasTkAgg(fig, master=self.canvas)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=BOTH, expand=True)
        canvas.draw()

root = Tk()
app = Application(master=root)
app.mainloop()
