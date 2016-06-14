response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
(T('Links'),URL('default','index')==URL(),URL('default','index'),[]),
(T('Manage'),URL('default','link_manage')==URL(),URL('default','link_manage'),[]),
(T('Add'),URL('default','add')==URL(),URL('default','add'),[])
]
