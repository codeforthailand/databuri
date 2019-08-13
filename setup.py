import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    dependencies = list(map(lambda x: x.strip(), fh.readlines()))

setuptools.setup(
    name="databuri",
    version="0.0.1",
    author="Pattarawat Chormai and friends",
    author_email="author@example.com",
    install_requires=dependencies,
    # @todo #1 ...
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url"https://github.com/codeforthailand/databuri",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        # @todo #1 add license
        # "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)