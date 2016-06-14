from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'Bookmarks2py'
settings.subtitle = 'powered by web2py'
settings.author = 'jrovegno'
settings.author_email = 'javier.rovegno@gmail.com'
settings.keywords = 'bookmark,tag'
settings.description = 'Another Delicious clone'
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = '123f5371-bfbe-46d9-bff3-1d70711e9919'
settings.email_server = 'localhost'
settings.email_sender = 'you@example.com'
settings.email_login = ''
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = []
