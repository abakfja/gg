import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gg-abakfja", # Replace with your own username
    version="0.0.1",
    author="Kannav Mehta",
    author_email="kannav.mehta@students.iiit.ac.in",
    description="A framework for creating terminal based games in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abakfja/gg",
    project_urls={
        "Bug Tracker": "https://github.com/abakfja/gg/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "gg"},
    packages=setuptools.find_packages(where="gg"),
    python_requires=">=3.6",
)