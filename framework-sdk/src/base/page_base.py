from uuid import uuid4
from object import AbstractClass

class PageBase:
  def __init__(self, path:str):
    self.key:str = f'{uuid4()}'
    self.path:str = path
  def build(self) -> None:
    raise AbstractClass()
  def is_same(self, other:PageBase):
    return self.key == other.key
