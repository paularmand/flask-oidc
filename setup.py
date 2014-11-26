from setuptools import setup
from pip.req import parse_requirements

setup(
    name='flask-oidc',
    description='OpenID Connect extension for Flask',
    url='https://github.com/SteelPangolin/flask-oidc',
    author='Jeremy Ehrhardt',
    author_email='jeremy@bat-country.us',
    version='0.1.1',
    packages=[
        'flask_oidc',
    ],
    install_requires=[str(req.req) for req in parse_requirements('requirements.txt')],
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
