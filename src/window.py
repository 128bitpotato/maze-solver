from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.root = Tk()
        self.root.title("Maze solver")

        self.canvas = Canvas()
        self.canvas.pack()

        self.running = False
    
    

