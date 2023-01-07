from KeyPress import KeyPress
from Gui import MainGui

if __name__ == "__main__":
  main_gui = MainGui()
  key_press = KeyPress(main_gui)
  key_press.listen()