from setuptools import setup, find_packages

setup(
    
    name = "mlproject",
    version = "0.0.1",
    author = "Shubham",
    author_email = "shubham2k@outlook.com",
    packages = find_packages(),
    install_requires = ['pandas','numpy','seaborn']
)