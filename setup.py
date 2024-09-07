from setuptools import setup, find_packages

setup(
    name="usa-visa-approval-prediction",  
    version="0.1.0",  # Initial version of your package
    author="girupashankar",  
    author_email="girupashankar20@example.com",  
    description="A brief description of your project",  # Describe your project
    long_description=open('README.md').read(),  # Long description from your README.md file
    long_description_content_type="text/markdown",  # Content type for long description
    url="https://github.com/girupashankar/usa-visa-approval-prediction.git",  # project's URL
    packages=find_packages(),  # Automatically finds all the packages and sub-packages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # License for your project
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',  # Python version requirement
    install_requires=[
        "numpy",  # Add required dependencies here
        "pandas",
        "scikit-learn",
    ],
)
