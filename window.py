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
    
    def draw_move(self, to_cell, undo=False):
        """Draw a line from the center of this cell to the center of another cell."""
        # Calculate center points of both cells
        from_center_x = (self.__x1 + self.__x2) // 2
        from_center_y = (self.__y1 + self.__y2) // 2
        to_center_x = (to_cell.__x1 + to_cell.__x2) // 2
        to_center_y = (to_cell.__y1 + to_cell.__y2) // 2
        
        # Create line from center to center
        move_line = Line(
            Point(from_center_x, from_center_y),
            Point(to_center_x, to_center_y)
        )
        
        # Choose color based on undo flag
        color = "gray" if undo else "red"
        
        # Draw the line
        self.__win.draw_line(move_line, color)


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
    
    # Create cells for testing move drawing
    
    # Create a grid of cells for testing
    cell1 = Cell(win)
    cell1.draw(50, 50, 150, 150)
    
    cell2 = Cell(win)
    cell2.has_right_wall = False  # Open to the right
    cell2.draw(150, 50, 250, 150)
    
    cell3 = Cell(win)
    cell3.has_left_wall = False   # Open to the left
    cell3.has_bottom_wall = False # Open to the bottom
    cell3.draw(250, 50, 350, 150)
    
    cell4 = Cell(win)
    cell4.has_bottom_wall = False # Open to the bottom
    cell4.draw(50, 150, 150, 250)
    
    cell5 = Cell(win)
    cell5.has_top_wall = False    # Open to the top
    cell5.has_right_wall = False  # Open to the right
    cell5.draw(150, 150, 250, 250)
    
    cell6 = Cell(win)
    cell6.has_top_wall = False    # Open to the top
    cell6.has_left_wall = False   # Open to the left
    cell6.draw(250, 150, 350, 250)
    
    cell7 = Cell(win)
    cell7.has_top_wall = False    # Open to the top
    cell7.draw(50, 250, 150, 350)
    
    cell8 = Cell(win)
    cell8.has_right_wall = False  # Open to the right
    cell8.draw(150, 250, 250, 350)
    
    cell9 = Cell(win)
    cell9.has_left_wall = False   # Open to the left
    cell9.draw(250, 250, 350, 350)
    
    # Test different types of moves
    
    # Red moves (normal path)
    cell1.draw_move(cell2)        # Horizontal move right
    cell2.draw_move(cell3)        # Horizontal move right
    cell3.draw_move(cell6)        # Vertical move down
    cell6.draw_move(cell9)        # Vertical move down
    
    # Gray moves (undo/backtrack)
    cell9.draw_move(cell8, undo=True)     # Horizontal move left (backtrack)
    cell8.draw_move(cell5, undo=True)     # Vertical move up (backtrack)
    
    # More red moves (continuing path)
    cell5.draw_move(cell4)        # Horizontal move left
    cell4.draw_move(cell7)        # Vertical move down
    
    # Test diagonal move
    cell7.draw_move(cell9)        # Diagonal move
    
    # Add some standalone cells to show different wall configurations
    standalone1 = Cell(win)
    standalone1.has_left_wall = False
    standalone1.has_top_wall = False
    standalone1.draw(450, 100, 550, 200)
    
    standalone2 = Cell(win)
    standalone2.has_right_wall = False
    standalone2.has_bottom_wall = False
    standalone2.draw(600, 300, 700, 400)
    
    # Test move between standalone cells
    standalone1.draw_move(standalone2)
    
    win.wait_for_close()


if __name__ == "__main__":
    main()
