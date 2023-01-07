from KeyPress import KeyPress
from FileHelper import FileHelper
# from Gui import MainGui

# if __name__ == "__main__":
#   main_gui = MainGui()
#   key_press = KeyPress(main_gui)
#   key_press.listen()
import eel

if __name__ == "__main__":
  file_helper = FileHelper()
  key_press = KeyPress(file_helper)
  key_press.listen()


