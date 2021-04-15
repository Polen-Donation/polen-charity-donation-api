import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="polen_charity_donation_api",
    version="1.0.0",
    author="polen",
    author_email="fernando@opolen.com.br",
    description="A sua API de doações",
    long_description=open('README.md').read(),
    url="https://polen-donation.github.io/polen-docs/",
    project_urls={
        "Bug Tracker": "https://github.com/Polen-Donation/polen-charity-donation-api",
    },
    keywords=['charity','OSC', 'ODS', 'Ongs', 'Ngos', 'Corporate', 'Donation', 'Doação', 'crowdfunding', 'Funding', 'Impact', 'Social', 'Giving'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=['requests']
)