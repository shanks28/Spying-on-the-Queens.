import pygame as p
import tkinter as tk
black = (0, 0, 0)
white = (255, 255, 255)
choice_4_queens_button=None
def choice_window():
    global choice_4_queens_button
    start_window=tk.Tk()
    start_window.geometry("800x300")
    Choice_label=tk.Label(start_window,text="How many Queens do you want to demonstrate,sensei? ")
    Choice_label.config(font=("Arial",20),fg="Green",bg="blacK") # the named parameters fg and bg are case insensitive and they convert to lower in the implementation
    Choice_label.pack()
    start_window.title("This is the first window")
    start_window.config(bg="Black")
    choice_4_queens_button=tk.Button(start_window,text="4 Queens",command=draw_pygame_window)
    choice_4_queens_button.config(fg="cyan",bg="black",font=("arial",15))
    choice_4_queens_button.pack(pady=50)
    start_window.mainloop()
def draw_4_queens(window,square_size):
    for rows in range(0, 4):
        for columns in range(0, 4):
            pos_x = (rows * square_size)
            pos_y = (columns * square_size)

            if ((rows + columns) % 2): # we could also replace this with an inline if statement but that would then require a mandatory else statement.
                p.draw.rect(window, black, (pos_x, pos_y, square_size, square_size))
            else:
                p.draw.rect(window, white, (pos_x, pos_y, square_size, square_size))
def draw_pygame_window():
    choice_4_queens_button.config(state=tk.DISABLED)
    window_dimensions = [800, 800]
    p.init()  # when we call this function we essentially call the lower level p.display.init() function
    flags = p.RESIZABLE | p.HWSURFACE | p.DOUBLEBUF
    window = p.display.set_mode((window_dimensions[0], window_dimensions[1]), flags)
    rows = [1, 2, 3, 4, 5, 6, 7, 8]
    columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    pos_x, pos_y = (0, 0)
    square_size = (window_dimensions[0] / 4)
    clock = p.time.Clock()
    running = True
    while (running):
        for event in p.event.get():
            if (event.type == p.QUIT):
                running = False
        draw_4_queens(window,square_size)
        p.display.flip()
        window.fill(white)
        clock.tick(60)
    p.display.quit()  # this is already handled when the program exits and is harmless to call it again this is to just create an exit point for my function
    choice_4_queens_button['state']='normal'
if(__name__=="__main__"):
    choice_window()

    # moores law....the number of transistors that are packed into a single chip double every 2 years