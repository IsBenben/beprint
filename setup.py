from setuptools import setup, find_packages

setup(
    name='beprint',
    version='0.1.0',
    author='IsBenben',
    description='BePrint -- Make Your Python Print Statements Beautiful',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/IsBenben/beprint',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
    install_requires=[
        'Pygments',
    ],
)
