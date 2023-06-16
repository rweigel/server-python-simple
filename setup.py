from setuptools import setup, find_packages

install_requires = ["fastapi", "starlette", "uvicorn"]

setup(
  name='hapi-server',
  version='0.0.1',
  author='Bob Weigel',
  author_email='rweigel@gmu.edu',
  packages=find_packages(),
  description='',
  install_requires=install_requires, extras_require={'dev': ['pytest', 'httpx']}
)
