http://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/

#Environment
https://virtualenv.pypa.io/en/latest/installation.html
for python 2.7
pip install virtualenv
virtualenv env

for python .30
pip install env
python -m enve env


env\Scripts\activate
set VENV=D:\pyproject\env 
%VENV%\Scripts\easy_install "pyramid==1.5.7"

Install
easy_install "pyramid==1.5.7"
easy_install nose webtest deform sqlalchemy pyramid_chameleon pyramid_debugtoolbar waitress pyramid_tm zope.sqlalchemy jinja2 scaffolds

pcreate -t alchemy D:\pyproject
env\Scripts\pcreate -s alchemy -t alchemy D:\pyproject\ads

python setup.py develop

python.exe setup.py test -q

pserve development.ini

pserve development.ini --reload

python setup.py sdist
