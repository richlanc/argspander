from setuptools import setup, find_packages

long_description = open("README.rst", "r").read()

setup(
    name="argspander",
    version="0.1.dev1",
    license="MIT",
    description="Project that provides argument expansion of objects",
    long_description=long_description,
    author="Richard Lancaster",
    author_email="lancasterrich@gmail.com",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "pytest"
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
    keywords="expansion splat argument unpacking"
)
