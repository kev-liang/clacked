import eel
import winsound
from pynput.keyboard import Listener
from FileHelper import FileHelper
import os

class KeyPress:
  def __init__(self, file_helper):
    self.file_helper = file_helper
    self.sound = "black.wav"
    self.sound_dict = set()

  def on_press_windows(self, key):
    if (key not in self.sound_dict):
      self.sound_dict.add(key)
      sound_path = os.path.join(FileHelper.app_data_sound_dir, self.sound)
      winsound.PlaySound(None, winsound.SND_ASYNC)
      winsound.PlaySound(sound_path, winsound.SND_ASYNC)

  def on_release_windows(self, key):
    if (key in self.sound_dict):
      self.sound_dict.remove(key)

  def listen(self):
    with Listener(on_press=self.on_press_windows, on_release=self.on_release_windows) as listener:
      eel.init('web', allowed_extensions=['.js', '.html'])
      eel.start('index.html', size=(400, 500))
      listener.join() 

  def set_sound(self, sound):
    self.sound = sound