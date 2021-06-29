import setuptools

with open("README.md", "r", encoding="utf8") as readme, open(
        "requirements.txt", "r", encoding="utf8"
) as requirements:
    long_description = readme.read()
    requires = requirements.read().splitlines(keepends=False)

setuptools.setup(
    name="py-tgcalls-wrapper",
    version="1.0.0",
    author="Roj Serbest",
    author_email="rojserbest@icloud.com",
    description="A library to make using PyTgCalls easier.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/callsmusic/pytgcalls-wrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requires,
)
