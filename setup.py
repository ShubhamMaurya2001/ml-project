from setuptools import setup, find_packages
from typing import List

hyphen_e_dot = "-e ."

def get_requirements(file_path:str)->List[str]:
    '''
    function to fetch for requirements
    
    :param file_path: Description
    :type file_path: str
    :return: Description
    :rtype: Any
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n","") for req in requirements]
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)


setup(
    
    name = "mlproject",
    version = "0.0.1",
    author = "Shubham",
    author_email = "shubham2k@outlook.com",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)