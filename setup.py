from setuptools import setup

setup(
    name='clickhook',
    version='0.0',
    author='Joshua English',
    py_modules=['clickhook'],
    install_requires=[
        'Click', 'click-plugins'
    ],
    entry_points='''
        [console_scripts]
        ch = clickhook:main
    ''',
)
