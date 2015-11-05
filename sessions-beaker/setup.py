from setuptools import setup

requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_beaker'
]

beaker.session.data_dir = %(here)s/data/sessions/data
beaker.session.lock_dir = %(here)s/data/sessions/lock

setup(name='tutorial',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = tutorial:main
      """,
)