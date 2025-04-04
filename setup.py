from setuptools import setup, find_packages

setup(
    name="AbhiMusicPlug",
    version="1.0.0",
    author="AbhiShek",
    author_email="abhishekbanshiwal2005@gmail.com",
    description="A Telegram Music Plugin System",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/NotRealAbhi/Plugins",
    packages=find_packages(),
    install_requires=open("requirements.txt").read().splitlines(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.9",
)
