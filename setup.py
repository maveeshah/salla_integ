from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in salla_integ/__init__.py
from salla_integ import __version__ as version

setup(
	name="salla_integ",
	version=version,
	description="Integrate O & C",
	author="Home",
	author_email="hcbdshb@bjhk",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
