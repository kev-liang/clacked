from KeyPress import KeyPress
from FileHelper import FileHelper
import eel

if __name__ == "__main__":
  file_helper = FileHelper()
  key_press = KeyPress(file_helper)

  @eel.expose
  def set_sound(sound):
    key_press.set_sound(sound)

  key_press.listen()

  

