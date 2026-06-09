from setuptools import find_packages, setup

MIN_PY_VERSION = "3.10"
PACKAGES = find_packages()
VERSION = "0.21.3"

setup(
    name="pyplejd",
    packages=PACKAGES,
    version=VERSION,
    description="A python library for communicating with Plejd devices via bluetooth",
    author="Thomas Lovén",
    author_email="thomasloven@gmail.com",
    license="MIT",
    url="https://github.com/kimballen/pyplejd",
    download_url=f"https://github.com/kimballen/pyplejd/archive/v{VERSION}.tar.gz",
    install_requires=["aiohttp", "bleak", "bleak_retry_connector", "pydantic"],
    keywords=["plejd", "bluetooth", "homeassistant"],
    python_requires=f">={MIN_PY_VERSION}",
)
