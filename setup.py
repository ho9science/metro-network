import os
from setuptools import find_packages, setup


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as req:
    REQUIREMENTS = req.read()

setup(name='subwaylinegraph',
      version='0.0.1',
      description='',
      long_description=README,
      url='https://github.com/ho9science/subwaygraphinSeoul',
      author='hyeonki.samdasu',
      author_email='noblesswith@gmail.com',
      keywords=['Korea', 'Subway',
                'line', 'graph', 'relation'],
      classifiers=[
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: Mathematics',
          'License :: OSI Approved :: BSD License',
      ],
      license='3-Clause BSD license',
      packages=find_packages(),
      package_data={'sslg': [
          'data/*.csv',
      ]},
      install_requires=REQUIREMENTS)