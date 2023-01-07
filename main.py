from keyPress import KeyPress
from gui.mainGui import MainGui

if __name__ == "__main__":
  main_gui = MainGui()
  key_press = KeyPress(main_gui)
  key_press.listen()