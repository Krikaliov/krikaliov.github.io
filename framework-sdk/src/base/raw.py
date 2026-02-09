from base import Base

class Raw(Base):
  def __init__(self, content:str):
    super().__init__()
    self.content:str = content
  def get_children(self) -> list[Base]:
    return []
  def __str__(self) -> str:
    return self.content
