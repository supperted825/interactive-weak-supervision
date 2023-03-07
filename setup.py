from setuptools import find_packages, setup
setup(
    name='iws',
    packages=find_packages(include=['iws']),
    version='0.2.1',
    description='PIP Installable Interactive Weak Supervision',
    author='Jonathan',
    license='MIT',
    install_requires=[         
        'pandas',         
        'python-dotenv',
        'scipy',
        'numpy',
        'spacy',
        'ipywidgets',
        'snorkel',
        'sklearn',
        'ipywidgets',
        'torch',
        'notebook',
        'beautifulsoup4',
        'matplotlib'
    ],
)
