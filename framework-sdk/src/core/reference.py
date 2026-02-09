from ..base.page_base import PageBase

class Reference:
  def __init__(self, path:str, external:bool = False):
    self.path:str = path
    self.external:bool = external

class ReferenceManager:
  def __init__(self):
    self.refs:list[PageBase] = list()
