from tkinter import Tk, BOTH, Canvas


class Point:
    def __init__(self, x, y):
        """Initialize a Point with x and y coordinates."""
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1, point2):
        """Initialize a Line with two Point objects."""
        self.point1 = point1
        self.point2 = point2
    
    def draw(self, canvas, fill_color):
        """Draw the line on the given canvas with the specified fill color."""
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, 
            fill=fill_color, width=2
        )


class Window:
    def __init__(self, width, height):
        """Initialize a new Window with specified width and height in pixels."""
        self.__width = width
        self.__height = height
        
        # Create root widget
        self.__root = Tk()
        
        # Set window title
        self.__root.title("Maze Solver")
        
        # Create canvas widget
        self.__canvas = Canvas(self.__root, width=width, height=height)
        
        # Pack the canvas so it's ready to be drawn
        self.__canvas.pack(fill=BOTH, expand=True)
        
        # Initialize running state
        self.__running = False
        
        # Connect close method to window delete event
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        """Redraw all graphics in the window."""
        self.__root.update_idletasks()
        self.__root.update()
    
    def draw_line(self, line, fill_color):
        """Draw a line on the window's canvas with the specified fill color."""
        line.draw(self.__canvas, fill_color)
    
    def wait_for_close(self):
        """Set running state to True and continuously redraw until window is closed."""
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self):
        """Set running state to False to stop the window loop."""
        self.__running = False


def main():
    """Main entrypoint function."""
    win = Window(800, 600)
    
    # Create some points
    point1 = Point(100, 100)
    point2 = Point(700, 100)
    point3 = Point(400, 500)
    point4 = Point(50, 550)
    point5 = Point(750, 550)
    
    # Create some lines
    line1 = Line(point1, point2)  # Horizontal line at top
    line2 = Line(point1, point3)  # Diagonal line from top-left to bottom-center
    line3 = Line(point2, point3)  # Diagonal line from top-right to bottom-center
    line4 = Line(point4, point5)  # Horizontal line at bottom
    line5 = Line(Point(400, 50), Point(400, 550))  # Vertical line through center
    
    # Draw the lines with different colors
    win.draw_line(line1, "black")
    win.draw_line(line2, "red")
    win.draw_line(line3, "blue")
    win.draw_line(line4, "green")
    win.draw_line(line5, "purple")
    
    win.wait_for_close()


if __name__ == "__main__":
    main()
