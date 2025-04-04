from setuptools import setup, find_packages

def read_requirements():
    with open("requirements.txt", "r") as f:
        return f.read().splitlines()


setup(
    name="AbhiMusicPlug",
    version="1.0",
    packages=find_packages(include=["Abhi", "Abhi.Core", "Config", "cookies"]),
    install_requires=read_requirements(),
    author="Abhi",
    author_email="abhishekbanshiwal2005@gmail.com",
    description="A plugin package for reuse",
    url="https://github.com/NotRealAbhi/Plugins",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
