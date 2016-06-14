### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_link',
    Field('f_url', type='string', notnull=True,
          label=T('Url')),
    Field('f_add_date', type='datetime', notnull=True,
          label=T('Add Date')),
    Field('f_private', type='boolean', default=False,
          label=T('Private')),
    Field('f_tags', type='list:string',
          label=T('Tags')),
    Field('f_title', type='string',
          label=T('Title')),
    Field('f_description', type='text',
          label=T('Description')),
    auth.signature,
    format='%(f_url)s',
    migrate=settings.migrate)
