from os import linesep as ln

from base import Base

class Item(Base):
  def __init__(self, type:str, args:dict[str,str] = {}, children:list[Base] = []):
    super().__init__()
    self.type:str = type
    self.args:dict[str,str] = args
    self.children:list = children
    self.size:int = len(children)
  def top_markup(self) -> str:
    ws:str = ' ' if len(self.args) > 0 else ''
    args:str = ws.join([f'{k}="{v}"' for k,v in self.args.items()])
    return f'<{self.type}{ws}{args}>'
  def bottom_markup(self) -> str:
    return f'</{self.type}>'
  def get_children(self) -> list[Base]:
    return self.children
  def __str__(self):
    markup:str = self.top_markup()
    if (self.size > 0):
      markup += ln.join([f'{x}' for x in self.children])
    markup += self.bottom_markup()
    return markup
