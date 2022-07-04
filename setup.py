import os
from setuptools import find_packages, setup


with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding="utf-8") as readme:
    README = readme.read()

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as req:
    REQUIREMENTS = req.read()

setup(name='metro-network',
      version='0.1.2',
      description='',
      long_description=README,
      url='https://github.com/ho9science/metro-network',
      author='hyeonki.min',
      author_email='noblesswith@gmail.com',
      keywords=['Korea', 'Seoul', 'subway', 'metro', 'open data',
                'line', 'graph', 'network'],
      classifiers=[
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'Operating System :: OS Independent',
          "Programming Language :: Python :: 3",
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: Information Analysis',
          'Topic :: Scientific/Engineering :: Mathematics',
          'License :: OSI Approved :: BSD License',
      ],
      license='3-Clause BSD license',
      packages=find_packages(),
      package_data={'mn': [
          'data/*.csv',
      ]},
      install_requires=REQUIREMENTS)