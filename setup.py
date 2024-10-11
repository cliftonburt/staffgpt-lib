from setuptools import setup, find_packages

# Read the content of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="staffgpt-lib",  # Name of the package
    version="0.1.0",  # Initial version
    author="Clifton Burt",  
    author_email="cliftonburt@gmail.com",  
    description="A library for AI role management and workflow automation with integrations.",
    long_description=long_description,
    long_description_content_type="text/markdown",  # README is in markdown
    url="https://github.com/cliftonburt/staffgpt-lib",  
    license="MIT",  # License type
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude=["tests*", "docs*", "examples*"]),  # Automatically discover packages
    install_requires=[
        # Add your project dependencies here
        "requests",  # Example dependencies, adjust as needed
        "openai",
        "notion-client",
        "google-api-python-client",
    ],
    python_requires=">=3.7",  # Specify minimum Python version
    entry_points={
        "console_scripts": [
            # You can add any CLI tools you want to expose here
        ],
    },
    include_package_data=True,  # Include data specified in MANIFEST.in
    zip_safe=False,  # Package is not safe to run directly from a zip file
)
