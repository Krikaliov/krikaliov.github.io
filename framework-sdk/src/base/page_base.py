from uuid import uuid4
from object import AbstractClass

# - - - - - - - - - - - - - - - - -
# Page base skeleton abstract class
# - - - - - - - - - - - - - - - - -
# All pages has those attributes and methods.
class PageBase:
  def __init__(self, path:str):
    # Relative path of the page from the app web root
    self.path:str = path

    # Last build UUID registered. Empty when initialized.
    # When the app builder computes references, it generates
    # a random UUID called "build UUID". Every page it computes
    # ahead, it compares this generated UUID with the page's one.
    # If they differs, this means that this page was still not built.
    # Thus, the app builder push this page in the stack of the
    # remaining pages meant to be built and assignes its generated
    # UUID to this attribute to prevent this page from being
    # built more than once.
    self.last_build_uuid:str = ''
  
  # Build function.
  # This write the built data in the file 'index.html'.
  def build(self) -> None:
    raise AbstractClass()
