"""
Marginalia Notes application
----------

Web application for Note-taking and managing.

"""

from setuptools import setup, find_packages

setup(
    name='Marginalia',
    version='1.0',
    author='Stanislav Sokolov aka ratso87',
    author_email='sokolst@gmail.com',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask>=0.10.1',
        'Flask-SQLAlchemy',
        'SQLAlchemy>=0.9.9',
        'Flask-Babel',
        'Flask-Migrate',
        'flask-restful>=0.3.2',
        'itsdangerous',
        'Flask-Passlib'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers, Users',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: JavaScript',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)