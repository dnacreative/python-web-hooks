# https://pypi.python.org/pypi?name=WebHooksDemo&version=0.1&:action=display

from setuptools import setup, find_packages
readme = open('README.txt').read()
setup(name='WebHooksDemo',
      version='0.1.1',
      author='Nathan Leiby',
      author_email='nathanleiby@gmail.com',
      license='MIT',
      description='Example package - testing webhooks on github and python build process',
      long_description=readme,
      packages=find_packages())