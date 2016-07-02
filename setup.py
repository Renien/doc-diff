from setuptools import setup, find_packages

setup(
    name='doc-diff',
    version='1.0.0',
    description='support lib to generate the diff of two CSV files',
    url='https://github.com/Renien/doc-diff',
    author='Renien',
    author_email='renien.john@gmail.com',
    license='MIT',
    download_url = 'https://github.com/Renien/doc-diff/tarball/1.0.0',
    keywords = ['doc-diff', 'DataScience', 'ComparingDocuments', 'ComparingAlgo'],
    packages=find_packages(exclude=['test'])
)