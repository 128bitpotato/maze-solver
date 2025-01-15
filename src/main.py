from graphics import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)

    cell1 = Cell(win, x1=10, y1=10)
    cell2 = Cell(win, True, False, True, False, x1=40, y1=10)
    cell3 = Cell(win, False, True, False, True, x1=70, y1=10)
    cell4 = Cell(win, True, False, False, False, x1=100, y1=10)
    cell5 = Cell(win, False, True, False, False, x1=130, y1=10)
    cell6 = Cell(win, False, False, True, False, x1=160, y1=10)
    cell7 = Cell(win, False, False, False, True, x1=190, y1=10)
    cell1.draw()
    cell2.draw()
    cell3.draw()
    cell4.draw()
    cell5.draw()
    cell6.draw()
    cell7.draw()

    win.wait_for_close()

if __name__ == "__main__":
    main()