import os
from uuid import uuid4

class _AbstractClass(Exception):
  pass

class _PageBase:
  def __init__(self, path:str):
    self.key:str = f'{uuid4()}'
    self.path:str = path
  def build(self) -> str:
    raise _AbstractClass()
  def is_same(self, other:_PageBase):
    return self.key == other.key

class _Base:
  def __init__(self):
    self.key:str = f'{uuid4()}'
  def __str__(self) -> str:
    raise _AbstractClass()
  def get_children(self) -> list:
    raise _AbstractClass()
  def is_same(self, other:_Base):
    return self.key == other.key
  def new_refs(self, prev:list[_PageBase]) -> list[_PageBase]:
    # Must return same value by default for most item types
    return prev

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
  def get_children(self) -> list[_Base]:
    return self.children
  def __str__(self):
    ln:str = os.linesep
    markup:str = self.top_markup()
    if (self.size > 0):
      markup += ln.join([f'{x}' for x in self.children])
    markup += self.bottom_markup()
    return markup

class Tag(_Base):
  def __init__(self, type:str, args:dict[str,str] = {}):
    super().__init__()
    self.type:str = type
    self.args:dict[str,str] = args
  def get_children(self) -> list[_Base]:
    return []
  def __str__(self):
    ws:str = ' ' if len(self.args) > 0 else ''
    args:str = ws.join([f'{k}="{v}"' for k,v in self.args.items()])
    return f'<{self.type}{ws}{args} />'

class Raw(_Base):
  def __init__(self, content:str):
    super().__init__()
    self.content:str = content
  def get_children(self) -> list[_Base]:
    return []
  def __str__(self) -> str:
    return self.content

class Link(Item):
  def __init__(self, ref:_PageBase, args:dict[str,str] = {}, children:list[_Base] = []):
    final_args:dict[str,str] = args
    final_args['href'] = ref.path
    super().__init__('a', final_args, children)
    self.ref:_PageBase = ref
  def get_children(self) -> list[_Base]:
    return self.children
  def new_refs(self, prev:list[_PageBase]) -> list[_PageBase]:
    return prev if any([self.ref.key == x.key for x in prev]) else prev + [self.ref]

class Page(_PageBase):
  def __init__(self, path:str, node:_Base):
    super().__init__(path)
    self.node:_Base = node
  def build(self) -> None:
    if not(os.path.exists(f'dist{self.path}')):
      os.makedirs(f'dist{self.path}')
    with open(f'dist{self.path}index.html', 'w') as buffer:
      buffer.write(str(self.node))
      buffer.close()

class App:
  def __init__(self, node:_Base):
    # Instantiate home page of the app
    self.home:_PageBase = Page('', node)
    # Parse app tree to retrieve every single page
    pages:list[Page] = self.__parse([], self.home.node, [self.home])
    # Build pages
    for page in pages: page.build()
  def __parse(self, acc:list[_PageBase], cur:_Base, remaining:list[_PageBase]) -> list[_PageBase]:
    # Execution can end when all pages were parsed
    if len(remaining) < 1: return acc
    # Accumulate new references from the current item
    acc = cur.new_refs(acc)
    # Get children of the current item
    children:list[_Base] = cur.get_children()
    # For each child
    for child in children:
      # Repeat with child as current item
      acc = self.__parse(acc, child, remaining)
    # Every child of this page was consumed from this page
    # Start again with the next page from remaining pages
    return self.__parse(acc, remaining[0].node, remaining[1:])


if __name__ == '__main__':
  raise Exception('This file is not executable!')
