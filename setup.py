from setuptools import setup, find_packages

setup(
    name="hello_world_python",
    version="0.0.2",
    description="Test github actions",
    url="https://github.com/garimaarorashuttl/hello-world-python.git",
    author="garimaarora",
    author_email="garimaarora786@gmail.com",
    license="MIT",
    packages=find_packages(),
    classifiers=["Programming Language :: Python :: 3.7"],
    install_requires=["requests"],
    extras_require={
        "test": ["pytest", "pytest-runner", "pytest-cov", "pytest-pep8", "responses"],
        "dev": ["flake8"],
    },
)
