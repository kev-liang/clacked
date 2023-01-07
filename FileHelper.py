from appdirs import user_data_dir
import os
import shutil
from pathlib import Path
import eel

@eel.expose
def get_sounds():
  result = []
  for file in os.listdir(FileHelper.app_data_path):
    result.append(file)
  return result
  
class FileHelper:
  app_data_path = user_data_dir("clacked", "clacked")

  def __init__(self):
    self.copy_sound_files("sounds")

  def copy_sound_files(self, original_dir):
    for file in os.listdir(original_dir):
      app_data_sound_path = os.path.join(FileHelper.app_data_path, file)
      if not os.path.isfile(app_data_sound_path):
        Path(FileHelper.app_data_path).mkdir(parents=True, exist_ok=True)
        original_sound_path = os.path.join(original_dir, file)
        shutil.copyfile(original_sound_path, app_data_sound_path)

  def get_app_dat_path(self):
    return self.app_data_path

