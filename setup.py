from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='allen.catalog.timeline',
      version=version,
      description="TImeline base catalog",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='allen catalog timeline zope3',
      author='Alin Voinea',
      author_email='alin.voinea@gmail.com',
      url='git://github.com/avoinea/allen.catalog.timeline.git',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['allen', 'allen.catalog'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
