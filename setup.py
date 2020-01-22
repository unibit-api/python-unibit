import setuptools

try:
    with open("README.md", "r") as fh:
        long_description = fh.read()
except IOError:
    long_description = "Python SDK for the UniBit API"
setuptools.setup(
    name="python-unibit",
    version="2.1.0",
    author="UniBit",
    author_email="support@unibit.ai",
    description="Python SDK for the UniBit API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/unibit-api/python-unibit",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['requests']
)