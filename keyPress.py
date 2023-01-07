import winsound
from pynput.keyboard import Listener
from tkinter import Tk, Label, PhotoImage, Canvas

class KeyPress:
  def __init__(self, mainGui): 
    self.mainGui = mainGui
    
  def on_press_windows(self, key):
    winsound.PlaySound("clack.wav", winsound.SND_ASYNC)

  def listen(self):
    with Listener(on_press=self.on_press_windows) as listener:
      self.mainGui.main_loop()
      listener.join() 



# external_file.py
# from pynput.keyboard import Listener
# import tkinter as tk
# class MyClass:
#     def __init__(self, queue):
#       self.queue = queue

#     def keyboard_listener(self):
#         # Create a keyboard listener
#         def on_press(key):
#             print(f'Key {key} pressed')
#             self.queue.put(key)
#         def on_release(key):
#             print(f'Key {key} released')
#             self.queue.put(key)
#         listener = Listener(on_press=on_press, on_release=on_release)
#         listener.start()
#         print("started listening")
#     def main_loop(self):
#         # Create the main window
#         win = tk.Tk()

#         # Define a function to retrieve keys from the queue
#         def retrieve_keys():
#             while True:
#                 key = self.queue.get()
#                 print(f'Received key {key} from queue')

#         # Run the main loop
#         win.after(1000, retrieve_keys)
#         print("started tk")
#         win.mainloop()