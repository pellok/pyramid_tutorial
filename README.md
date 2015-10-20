http://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/

#Environment
>mkdir env
>python -m enve env
>env\Scripts\activate or
>set VENV=c:\projects\quick_tutorial\env
 >%VENV%\Scripts\easy_install "pyramid==1.5.7"

Install
>easy_install "pyramid==1.5.7"
>easy_install nose webtest deform sqlalchemy pyramid_chameleon pyramid_debugtoolbar waitress pyramid_tm zope.sqlalchemy jinja2


Directory Tree
quicktutorial/
  request_response/
    development.ini
    setup.py
    tutorial/
      __init__.py
      home.pt
      tests.py
      views.py