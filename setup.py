from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='cenditel.ppm.cynin',
      version=version,
      description="A Integration of Project Portfolio Management Framework NG on Cyn.in 3.1.3.",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Plone',
        'Framework :: Zope2',
        'Framework :: Zope3',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='project portfolio management framework lone plonegov cynin313 cyn.in cenditel',
      author='Oswaldo Lopez',
      author_email='oswaldolo@hotmail.com',
      maintainer='Leonardo J. Caballero G.',
      maintainer_email='leonardocaballero@gmail.com',
      url='http://svn.plone.org/svn/collective/cenditel.ppm.cynin',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['cenditel', 'cenditel.ppm'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'cenditel.ppm',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
