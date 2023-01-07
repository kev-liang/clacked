from tkinter import Tk, OptionMenu, PhotoImage, Canvas, StringVar
# import constants 
import os
class MainGui:
  def create_title(self, canvas, title):
    canvas.create_text(200, 100, text=title, fill="white", font=("Poppins Medium", 50))

  def create_menu(self, win):
    # Create the list of options
    options_list = ["Option 1", "Option 2", "Option 3", "Option 4"]
      
    # Variable to keep track of the option
    # selected in OptionMenu
    value_inside = StringVar(win)
      
    # Set the default value of the variable
    value_inside.set("Select an Option")
      
    # Create the optionmenu widget and passing 
    # the options_list and value_inside to it.
    question_menu = OptionMenu(win, value_inside, *options_list)
    question_menu.pack()

  def main_loop(self):
    # Creating the GUI window.
    win = Tk()
    canvas = Canvas(win, width=400, height=500, bd=0, highlightthickness=0, relief='ridge')
    win.title("Clacked") 
    win.geometry("400x500")
    bg_img = PhotoImage(file = "background.png")
    canvas.create_image(200, 250, image=bg_img)
    self.create_title(canvas, "Clacked")
    self.create_menu(win)
    canvas.pack()
    win.resizable(False, False)
    win.mainloop()