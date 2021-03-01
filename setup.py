from setuptools import setup, find_packages

setup(
    name="range_dict",
    version="0.1.2",
    description="Store ranges as keys in a dictionary",
    author="Piotr Kardaś",
    author_email="pkardas.it@gmail.com",
    url="https://github.com/pkardas/range-dict",
    packages=find_packages(),
    package_data={
        "range_dict": ["py.typed"]
    },
)
