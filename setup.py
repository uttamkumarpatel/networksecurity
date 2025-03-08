# Import necessary modules
from setuptools import find_packages, setup  # Used for packaging Python projects
from typing import List  # Used for type hinting

# Function to read and retrieve package dependencies from requirements.txt
def get_requirements() -> List[str]:
    requirement_lst: List[str] = []  # Initialize an empty list to store requirements
    
    try:
        # Open and read the requirements.txt file
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()  # Read all lines from the file
            
            for line in lines:
                requirement = line.strip()  # Remove leading/trailing whitespace or newline characters
                
                # Exclude empty lines and 'p' which is used for editable installations
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)  # Add valid requirements to the list
                    
    except:
        print("requirements.txt file not found")  # Handle file not found error gracefully

    return requirement_lst  # Return the list of dependencies

# Setup function to configure the package
setup(
    name="NetworkSecurity",  # Name of the package
    version="0.0.1",  # Version number of the package
    author="Uttam Kumar",  # Author name
    author_email="uk2242004@gmail.com",  # Author email
    packages=find_packages(),  # Automatically find and include all Python packages in the project
    install_requires=get_requirements()  # Get the list of dependencies from requirements.txt
)
