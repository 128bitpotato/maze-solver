from graphics import Window, Line, Point

def main():
    win = Window(800, 600)

    point1 = Point(10, 10)
    point2 = Point(50, 50)
    line1 = Line(point1, point2)
    win.draw_line(line1, "red")

    point3 = Point(100, 100)
    point4 = Point(100, 150)
    line2 = Line(point3, point4)
    win.draw_line(line2, "black")

    win.wait_for_close()

if __name__ == "__main__":
    main()