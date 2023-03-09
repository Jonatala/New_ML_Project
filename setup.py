from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this fuction will return the list of requirements
    :param file_path:
    :return:
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements



setup(
    name='New_ML_Project',
    version='1.0.0.0',
    author='Jon Atala',
    author_email='olaatala7',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)