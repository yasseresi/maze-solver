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


class Cell:
    def __init__(self, win):
        """Initialize a Cell with a Window instance."""
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = win
    
    def draw(self, x1, y1, x2, y2):
        """Draw the cell with the given coordinates."""
        # Update internal coordinates
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        
        # Draw left wall if it exists
        if self.has_left_wall:
            left_wall = Line(Point(x1, y1), Point(x1, y2))
            self.__win.draw_line(left_wall, "black")
        
        # Draw right wall if it exists
        if self.has_right_wall:
            right_wall = Line(Point(x2, y1), Point(x2, y2))
            self.__win.draw_line(right_wall, "black")
        
        # Draw top wall if it exists
        if self.has_top_wall:
            top_wall = Line(Point(x1, y1), Point(x2, y1))
            self.__win.draw_line(top_wall, "black")
        
        # Draw bottom wall if it exists
        if self.has_bottom_wall:
            bottom_wall = Line(Point(x1, y2), Point(x2, y2))
            self.__win.draw_line(bottom_wall, "black")


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
    
    # Create and draw different cells with various wall configurations
    
    # Cell 1: All walls (default)
    cell1 = Cell(win)
    cell1.draw(50, 50, 150, 150)
    
    # Cell 2: No left wall
    cell2 = Cell(win)
    cell2.has_left_wall = False
    cell2.draw(200, 50, 300, 150)
    
    # Cell 3: No right wall
    cell3 = Cell(win)
    cell3.has_right_wall = False
    cell3.draw(350, 50, 450, 150)
    
    # Cell 4: No top wall
    cell4 = Cell(win)
    cell4.has_top_wall = False
    cell4.draw(500, 50, 600, 150)
    
    # Cell 5: No bottom wall
    cell5 = Cell(win)
    cell5.has_bottom_wall = False
    cell5.draw(650, 50, 750, 150)
    
    # Cell 6: Only left and right walls (corridor)
    cell6 = Cell(win)
    cell6.has_top_wall = False
    cell6.has_bottom_wall = False
    cell6.draw(50, 200, 150, 300)
    
    # Cell 7: Only top and bottom walls (horizontal corridor)
    cell7 = Cell(win)
    cell7.has_left_wall = False
    cell7.has_right_wall = False
    cell7.draw(200, 200, 300, 300)
    
    # Cell 8: No walls (completely open)
    cell8 = Cell(win)
    cell8.has_left_wall = False
    cell8.has_right_wall = False
    cell8.has_top_wall = False
    cell8.has_bottom_wall = False
    cell8.draw(350, 200, 450, 300)
    
    # Cell 9: Only left wall
    cell9 = Cell(win)
    cell9.has_right_wall = False
    cell9.has_top_wall = False
    cell9.has_bottom_wall = False
    cell9.draw(500, 200, 600, 300)
    
    # Cell 10: Different size cell with all walls
    cell10 = Cell(win)
    cell10.draw(100, 350, 250, 500)
    
    # Cell 11: Large cell with only diagonal walls (top-left and bottom-right)
    cell11 = Cell(win)
    cell11.has_right_wall = False
    cell11.has_bottom_wall = False
    cell11.draw(300, 350, 500, 500)
    
    win.wait_for_close()


if __name__ == "__main__":
    main()
