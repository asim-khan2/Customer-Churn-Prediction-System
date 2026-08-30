from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    with open(file_path,'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)


    return requirements



setup(
    name='Customer Churn Prediction System',
    version='0.0.1',
    author="Asim Khan",
    author_email='asimkhan106988@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)


if __name__=="__main__":
    get_requirements('requirements.txt')