import os
from sdk import Item, Tag, Raw, Page

Page('/', Item('html', {'lang': 'fr'}, [
  Item('head', {}, [
    Item('title', {}, [Raw('Super site')]),
    Tag('meta', {'charset': 'utf-8'})
  ]),
  Item('body', {}, [
    Item('p', {}, [Raw(f'coucou {i}')]) for i in range(1,6)
  ])
])).build()
