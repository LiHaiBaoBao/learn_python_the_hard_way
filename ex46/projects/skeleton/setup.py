try:
    from setuptools import setup
except:
    from distutils.core import setup

config = {
    'description' : 'My Project',
    'author' : 'My name',
    'url' : 'URL to get it at.',
    'download_url' : 'Where to download it.',
    'author_email' : 'My emain.',
    'version' : '0.1',
    'install_requires' : ['nose'],
    'packages' : ['python_practise'],
    'scripts' : [],
    'name' : 'projectname'
}
setup(**config)
