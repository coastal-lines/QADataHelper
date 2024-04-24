from setuptools import setup, find_packages

setup(
    name='QADataHelper',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'setuptools==69.5.1',
        'beautifulsoup4==4.12.3',
        'requests==2.31.0',
        'tkinterweb==3.23.8',
        'matplotlib==3.8.4',
        'pyral==1.6.0',
        'pandas==2.1.4',
        'seaborn==0.13.1'
    ],
)