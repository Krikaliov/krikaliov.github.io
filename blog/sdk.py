import os
from uuid import uuid4

class _AbstractClass(Exception):
  pass

class _Base:
  def __init__(self):
    self.key:str = f'{uuid4()}'
  def __str__(self) -> str:
    raise _AbstractClass()

class Item(_Base):
  def __init__(self, type:str, args:dict[str,str] = {}, children:list[_Base] = []):
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
  def __str__(self):
    ln:str = os.linesep
    markup:str = self.top_markup() + ln
    if (self.size > 0):
      markup += ln.join([f'{x}' for x in self.children]) + ln
    markup += self.bottom_markup()
    return markup

class Tag(_Base):
  def __init__(self, type:str, args:dict[str,str] = {}):
    super().__init__()
    self.type:str = type
    self.args:dict[str,str] = args
  def __str__(self):
    ws:str = ' ' if len(self.args) > 0 else ''
    args:str = ws.join([f'{k}="{v}"' for k,v in self.args.items()])
    return f'<{self.type}{ws}{args} />'

class Raw(_Base):
  def __init__(self, content:str):
    super().__init__()
    self.content:str = content
  def __str__(self) -> str:
    return self.content

class _PageBase:
  def __init__(self):
    self.key:str = f'{uuid4()}'
  def build(self) -> str:
    raise _AbstractClass()

class Page(_PageBase):
  def __init__(self, path:str, dependencies:list[_PageBase], node:_Base):
    self.path:str = path
    self.dependencies:list[str] = dependencies
    self.node:_Base = node
  def build(self) -> None:
    for dependency in self.dependencies:
      dependency.build()
    with open(f'dist{self.path}index.html', 'w') as buffer:
      buffer.write(str(self.node))
      buffer.close()

if __name__ == '__main__':
  raise Exception('This file is not executable!')
