def index():
    if auth.is_logged_in():
        response.flash = T("Hello")
        '''return dict(message=T('Welcome to Book4Cook!'))'''
        """return auth.wiki()"""
        if len(request.args):
            page=int(request.args[0])
        else: 
            page=0
        items_per_page=3
        limitby=(page*items_per_page,(page+1)*items_per_page+1)
        rows=db(db.page.id>0).select(limitby=limitby)
        return dict(message=T('Welcome to Book4Cook!'),rows=rows,page=page,items_per_page=items_per_page)
    else:
        redirect(URL('user'))

def moka():
    if auth.is_logged_in():
        response.flash = T("Hello")
        '''return dict(message=T('Welcome to Cookery Book!'))'''
        """return auth.wiki()"""
        if len(request.args):
            page=int(request.args[0])
        else:
            page=0
        items_per_page=3
        limitby=(page*items_per_page,(page+1)*items_per_page+1)
        rows=db((db.page.id>0)&(auth.user.email==db.page.email)).select(limitby=limitby)
        return dict(message=T('Welcome to Cookery Book!'),rows=rows,page=page,items_per_page=items_per_page)
    else:
        redirect(URL('user'))

def user():
  
    return dict(form=auth())


@cache.action()
def download():
   
    return response.download(request, db)

def show():
    page = db.page(request.args(0,cast=int)) or redirect(URL('index'))
    db.post.recipe.default = page.id
    form = SQLFORM(db.post)
    return dict(page=page,form=form)

def edit_post():
    id=request.args(0,cast=int)
    form=SQLFORM(db.page,id,deletable=True).process(next='show/[id]')
    return locals()

def user():

    return dict(form=auth())

def mycookbook():
    form= SQLFORM.grid(db.page.id>0)
    return dict(form=form)
@auth.requires_login()
def uploadrecipe():
    form = SQLFORM(db.page).process()
    if form.accepted:
        response.flash="Recipe added to your cookbook"
        redirect(URL('moka'))
    return dict(form=form)
    '''return locals()'''

@auth.requires_membership('manager')
def manage():
    grid = SQLFORM.grid(db.page)
    return locals()
