# -*- coding: utf-8 -*-
# Testing
from fileutils import abspath
from languages import read_possible_languages

possible_languages = read_possible_languages(abspath('applications', app))
#NOTE! app - is an application based router's parameter with name of an
#            application. E.g.'welcome'

routers = {
    app: dict(
        default_language = possible_languages['default'][0],
        languages = [lang for lang in possible_languages
                           if lang != 'default']
    )
}

#NOTE! To change language in your application using these rules add this line
#in one of your models files:
#   if request.uri_language: T.force(request.uri_language)
