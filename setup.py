from setuptools import setup, find_packages

setup(
    name="frappe_theme",
    version="0.0.1",
    description="Frappe 15 Theme",
    author="Prismatic Soft",
    author_email="info@prismaticsoft.com",
    license="MIT",
    packages=find_packages(include=["frappe_theme", "frappe_theme.*"]),
    include_package_data=True,
    install_requires=[],
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.10",
)