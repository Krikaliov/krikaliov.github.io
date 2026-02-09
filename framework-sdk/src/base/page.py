from os import path, makedirs

from base import Base
from page_base import PageBase

class Page(PageBase):
  def __init__(self, path:str, node:Base):
    super().__init__(path)
    self.node:Base = node
  def build(self) -> None:
    if not(path.exists(f'dist{self.path}')):
      makedirs(f'dist{self.path}')
    with open(f'dist{self.path}index.html', 'w') as buffer:
      buffer.write(str(self.node))
      buffer.close()
