import uuid
from ..save_data_manager.save_data_manager import SaveDataManager

class GenericTemplate():
  def __init__(self):
    self.name : str = ""

  def init(self, name: str):
    self.name = name

class Saveable():
  def __init__(self):
    self.save_id = str(uuid.uuid4())

  def save(self, data_mgr : SaveDataManager):
    data_mgr.update_save_data(self.save_id, convert_to_dict(self))




def convert_to_dict(thing : Saveable):

  save_dict = {}
  for key, value in thing.__dict__.items():
    if key.startwith('_') == False:
      if isinstance(value,Saveable):
        save_dict[key] = convert_to_dict(value)
      else :
        save_dict[key] = value

  return save_dict