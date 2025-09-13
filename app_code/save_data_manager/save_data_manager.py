import json

class SaveDataManager():
  def __init__(self):
    self.SAVE_DATA_DB = {}
    self.save_this_turn = False

  def update_save_data(self, key : str, value : any) :
    self.SAVE_DATA_DB[key] = value
    self.save_this_turn = True

  def check_and_save_all_data(self):
    if self.save_this_turn :
      save_data_to_file(self.SAVE_DATA_DB)
      self.save_this_turn = False


def save_presets_to_file(data: dict):
  with open("save_presets.json", "w") as f:
    json.dump(data, f)

def save_data_to_file(data: dict):
  with open("save_data.json", "w") as f:
    json.dump(data, f)

def load_data_from_file():
  with open("save_data.json", "r") as f:
    return json.load(f)