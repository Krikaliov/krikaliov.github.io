from .base.base import Base
from .base.page import Page

class App:
  def __init__(self, node:Base):
    # Instantiate home page of the app
    self.home:Page = Page('', node)
    # Parse app tree to retrieve every single page
    pages:list[Page] = self.__parse([], self.home.node, [self.home])
    # Build pages
    for page in pages: page.build()
  def __parse(self, acc:list[Page], cur:Base, remaining:list[Page]) -> list[Page]:
    # Execution can end when all pages were parsed
    if len(remaining) < 1: return acc
    # Accumulate new references from the current item
    acc = cur.new_refs(acc)
    # Get children of the current item
    children:list[Base] = cur.get_children()
    # For each child
    for child in children:
      # Repeat with child as current item
      acc = self.__parse(acc, child, remaining)
    # Every child of this page was consumed from this page
    # Start again with the next page from remaining pages
    return self.__parse(acc, remaining[0].node, remaining[1:])
