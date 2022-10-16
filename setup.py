import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'LoVolMo',
    version = '0.0.3',
    author = 'Gabriel Wendell Celestino Rocha',
    author_email='gabrielwendell@fisica.ufrn.be',
    description = 'Testing installation of Package',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/GabrielWendell/LoVolMo',
    project_urls = {
        "Bug Tracker": "https://github.com/GabrielWendell/LoVolMo/issues"
    },
    license = 'MIT',
    packages = ['LoVolMo'],
    install_requires = ['requests'],
)