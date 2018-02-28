from setuptools import setup, find_packages

setup(
    name='cbp',
    version='0.2.0',
    description='Unofficial Python Wrapper for Coinbase Pricing APIs',
    url='https://github.com/uilyam/coinbase-pricing-python',
    author='William Fleming',
    author_email='uilyam@github.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'requests >= 2.18.4',
        ],
        zip_safe=False
)