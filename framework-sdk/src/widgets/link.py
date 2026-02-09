from ..base.page_base import PageBase
from ..base.base import Base
from ..base.item import Item

class Link(Item):
  def __init__(self, ref:PageBase, args:dict[str,str] = {}, children:list[Base] = []):
    final_args:dict[str,str] = args
    final_args['href'] = ref.path
    super().__init__('a', final_args, children)
    self.ref:PageBase = ref
  def get_children(self) -> list[Base]:
    return self.children
  def new_refs(self, prev:list[PageBase]) -> list[PageBase]:
    return prev if any([self.ref.key == x.key for x in prev]) else prev + [self.ref]
