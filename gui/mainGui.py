from tkinter import Tk, Label, PhotoImage, Canvas
# import constants 
import os
class MainGui:
  def create_background(self, canvas):
    bg_img = PhotoImage(file = "background.png")
    canvas.create_image(200, 250, image=bg_img)

  def create_title(self, canvas, title):
    canvas.create_text(200, 100, text=title, fill="white", font=("Poppins Medium", 50))

  def main_loop(self):
    # Creating the GUI window.
    win = Tk()
    canvas = Canvas(win, width=400, height=500, bd=0, highlightthickness=0, relief='ridge')
    win.title("Clacked") 
    win.geometry("400x500")
    self.create_background(canvas);
    self.create_title(canvas, "Clacked")

    canvas.pack()
    win.resizable(False, False)
    win.mainloop()