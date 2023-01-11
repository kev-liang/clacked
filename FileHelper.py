from appdirs import user_data_dir
import os
import shutil
from pathlib import Path
import eel
import json

class FileHelper:
  app_data_path = user_data_dir("Clacked", "Clacked")
  favorites_path = os.path.join(app_data_path, "favorites.json")
  app_data_sound_dir = os.path.join(app_data_path, "sounds")

  def __init__(self):
    self.copy_sound_files("sounds")
    self.init_favorites()

  # original_dir: local path for folder with sounds
  def copy_sound_files(self, original_dir):
    for sound in os.listdir(original_dir):
      app_data_sound_path = os.path.join(FileHelper.app_data_sound_dir, sound)
      if not os.path.isfile(app_data_sound_path):
        Path(FileHelper.app_data_sound_dir).mkdir(parents=True, exist_ok=True)
        original_sound_path = os.path.join(original_dir, sound)
        shutil.copyfile(original_sound_path, app_data_sound_path)

  def init_favorites(self):
    if not os.path.isfile(FileHelper.favorites_path):
      with open(FileHelper.favorites_path, "w+") as f:
        f.write(json.dumps({"favorites": []}))

@eel.expose
def get_sounds():
  return os.listdir(FileHelper.app_data_sound_dir)

# windows-specific 
@eel.expose
def open_sound_folder():
    os.startfile(FileHelper.app_data_sound_dir)

@eel.expose 
def get_favorites():
  with open(FileHelper.favorites_path, "r+") as f:
    data = json.load(f)
    return data["favorites"]

@eel.expose
def toggle_favorite(favorite): 
  with open(FileHelper.favorites_path, "r+") as f:
    data = json.load(f)
    if favorite in data["favorites"]:
      data["favorites"].remove(favorite)
    else:
      data["favorites"].append(favorite)
    f.seek(0)
    f.write(json.dumps(data))
    f.truncate()

@eel.expose
def filter_sounds(filter):
  sounds = {
    "keyboard": ["black.wav", "blue.wav", "brown.wav", "contactless.wav", "kailh optical.wav", "membrane.wav", "red.wav", "v-optical click.wav"],
    "percussion": ["blip.wav", "clack.wav", "pebbles.wav", "snap.wav", "type.wav"]
  }

  
  if (filter == "keyboard"):
    return sounds["keyboard"]
  elif (filter == "percussion"):
    return sounds["percussion"]
  elif (filter == "custom"):
    result = []
    for sound in os.listdir(FileHelper.app_data_sound_dir):
      if sound not in sounds["keyboard"] and sound not in sounds["percussion"]:
        result.append(sound)
    return result
  else: 
    get_sounds()