from setuptools import setup, find_packages


setup(
    name="mess",
    version="0.0.0",
    description="A nightmare",


    author="Sam Stern (though I wish it wasn't)",
    author_email="jstern@cs.umass.edu",
    license="I'm not accountable for damage caused by this",
    packages=find_packages(),
    include_package_data=True,
    entry_points={"console_scripts": ["mess = mess.__main__:main"]},
    python_requires=">=3.6",
)
