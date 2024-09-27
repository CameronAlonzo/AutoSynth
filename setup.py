from setuptools import setup, find_packages
##handle setup
setup(
    name = 'autosynth',
    version = '0.1',
    packages=find_packages(),
    install_requires=['numpy', 'pandas', 'scikit-learn', 'matplotlib'],
)