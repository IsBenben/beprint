from setuptools import setup, find_packages

# python setup.py bdist_wheel --universal
# twine upload dist/*

setup(
    name='beprint',
    version='0.1.1',
    author='IsBenben',
    description='BePrint -- Make Your Python Print Statements Beautiful',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/IsBenben/beprint',
    packages=find_packages(),
    license='Apache License',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
    ],
    python_requires='>=3.11',
    install_requires=[
        'Pygments',
        'mistune'
    ],
)
