response.logo = A(B('Book',SPAN(4),'Cook'),XML('&trade;&nbsp;'),
                  _class="navbar-brand",_href="http://127.0.0.1:8000/cooking_project/default/index",
                  _id="web2py-logo")
response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.description = 'a cool new app'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

response.menu = [
        (T('Overview'),False, URL('default', 'index')),
        (T('My_CookBook'),False,URL('default', 'moka')),
        (T('Upload Recipes '),False,URL('default', 'uploadrecipe')),
        
    ]
if auth.has_membership('manager'):
    response.menu.append((T('Admin'),False,URL('default','manage')))

if "auth" in locals(): auth.wikimenu()
