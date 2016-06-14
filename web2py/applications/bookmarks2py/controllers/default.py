# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    db.t_link.f_tags.searchable = True
    db.t_link.f_url.readable = False
    db.t_link.id.readable = False
    form = SQLFORM.smartgrid(db.t_link,
                             details=False,
                             editable=False,
                             deletable=False,
                             create=False,
                             maxtextlength=40,
                             buttons_placement = 'left',
                             links=[dict(header="URL", body=lambda row: A(row.f_url, _href=row.f_url, _target="_blank"))],
                             links_in_grid=True
                             )
    return dict(form=form)

@auth.requires_login()
def link_manage():
    form = SQLFORM.smartgrid(db.t_link,
                            links=[dict(header="URL", body=lambda row: A("Go", _href=row.f_url, _target="_blank"))])
    return dict(form=form)

@auth.requires_login()
def add():
     # create an insert form from the table
    form = SQLFORM(db.t_link).process()

    # if form correct perform the insert
    if form.accepted:
        response.flash = 'new record inserted'
    return dict(form=form)
