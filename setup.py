# for distribution of the version of the python we are using this setup.py file and same for this ML project.

from setuptools import find_packages, setup
from typing import List

requirement_file_name = "requirements.txt"
REMOVE_PACKAGE = "-e ."

def get_requirements()->List[str]:
    with open(requirement_file_name) as requirement_file:
        requirement_list = requirement_file.readline()
    requirement_list = [requriment_name.replace("\n","") for requriment_name in requirement_list]

    if REMOVE_PACKAGE in requirement_list:
        requirement_list.remove(REMOVE_PACKAGE)
    return requirement_list

setup(name='Insurance',
      version='0.0.1',
      description='Insurance Industry lavel project',
      author='Vishwajeet Patel',
      author_email='vishwajeet.patel161@gmail.com',
    #   url='https://www.python.org/sigs/distutils-sig/',
      packages=find_packages(),
      install_reqires = get_requirements() 
     )