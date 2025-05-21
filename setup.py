from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path):
    """
    This function returns a list of requirements from the given file path.
    """
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()  #read lines in requirements.txt
        requirements = [req.replace('\n', '') for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .') #remove -e . if present       
    return requirements

setup( 
    name='ml_project',
    version='0.1',
    author='Poojitha',
    author_email='n.poojitha75@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt'),
)