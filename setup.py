from setuptools import setup
setup(
    name="mypackage",
    version="0.0.1",
    license="GPL-3.0-or-later",
    author="Carmen Bianca Bakker",
    author_email="carmenbianca@fsfe.org",
    description="Test package.",
    long_description="",
    package_dir={"": "src"},
    packages=["mypackage"],
    include_package_data=True,
    tests_require=["pytest"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: "
        "GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
