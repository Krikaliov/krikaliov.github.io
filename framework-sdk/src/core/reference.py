from ..base.page_base import PageBase

# - - - - - - - -
# Reference class
# - - - - - - - -
# This object refers either to an existing page
# of the web app or an external link.            
class Reference:
  def __init__(self, path:str, external:bool = False):
    self.path:str = path
    self.external:bool = external

class ReferenceManager:
  def __init__(self):
    self.refs:list[PageBase] = list()
