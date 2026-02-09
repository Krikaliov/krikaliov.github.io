from uuid import uuid4
from object import AbstractClass

from page_base import PageBase

class Base:
  def __init__(self):
    self.key:str = f'{uuid4()}'
  def __str__(self) -> str:
    raise AbstractClass()
  def get_children(self) -> list:
    raise AbstractClass()
  def is_same(self, other:Base):
    return self.key == other.key
  def new_refs(self, prev:list[PageBase]) -> list[PageBase]:
    # Must return same value by default for most item types
    return prev
