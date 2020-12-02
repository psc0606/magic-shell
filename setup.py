from setuptools import setup, find_packages

setup(
    name='modules',
    version='0.1.1',
    author='pengshaocheng',
    author_email='psc0606@163.com',
    url='https://github.com/psc0606',
    # only include the package, not include child
    # packages=['modules'],

    # use this to find all package
    packages=find_packages(),
)
