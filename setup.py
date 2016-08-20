from codecs import open
from os import path
from setuptools import find_packages, setup

__version__ = '0.1.2'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if 'git+' not in x]

setup(
    name='docker-event-scripts',
    version=__version__,
    description='Run scripts in response to Docker events.',
    long_description=long_description,
    url='https://github.com/colebrumley/des',
    download_url='https://github.com/colebrumley/des/releases/tag/v' + __version__,
    license='MIT',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3.5',
    ],
    keywords=['docker','event', 'watch', 'monitor', 'script'],
    entry_points={
          'console_scripts': ['des=des.cli:main'],
      },
    packages=find_packages(exclude=['docs', 'tests*', 'contrib']),
    include_package_data=True,
    author='Cole Brumley',
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='cole.brumley@gmail.com'
)
