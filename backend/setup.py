from setuptools import setup, find_packages
from codecs import open
from os import path, makedirs
import shutil

def clean_directory(directory):
    """Clean a directory by removing it if it exists and then recreating it."""
    if path.exists(directory):
        shutil.rmtree(directory)
        print(f"Removed directory: {directory}")
    makedirs(directory)
    print(f"Recreated directory: {directory}")

clean_directory('./dist')
shutil.copy('../shared/data.json', 'hushigi_grammar/data.json')

__version__ = '0.0.6'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')]

setup(
    name='hushigi_grammar',
    version=__version__,
    description='Assistant for aiding conversational fluency for Japanese language.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hushigidea/hushigi-grammar',
    download_url='https://github.com/hushigidea/hushigi-grammar/tarball/' + __version__,
    license='BSD',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],
    keywords='',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    package_data={
        'hushigi_grammar': ['data.json'],
    },
    author='Wei Jiang',
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='jiangjay818@gmail.com'
)
