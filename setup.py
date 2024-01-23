from setuptools import setup

setup(
    name='sre',
    version='1.0',
    py_modules=['sre'],
    install_requires=[
      'kubernetes',
      'click',
    ],
    entry_points='''
    [console_scripts]
    sre=sre:cli
    ''',
)