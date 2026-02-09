from base import Base

class Tag(Base):
  def __init__(self, type:str, args:dict[str,str] = {}):
    super().__init__()
    self.type:str = type
    self.args:dict[str,str] = args
  def get_children(self) -> list[Base]:
    return []
  def __str__(self):
    ws:str = ' ' if len(self.args) > 0 else ''
    args:str = ws.join([f'{k}="{v}"' for k,v in self.args.items()])
    return f'<{self.type}{ws}{args} />'
