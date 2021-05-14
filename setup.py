import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="VarSomeClinicalAPI",
    version="1.0.0",
    description="A client library for accessing VarSome Clinical API Documentation",
    long_description=long_description,
    scripts=['scripts/varsome_api_run.py', 'scripts/varsome_api_annotate_vcf.py'],
    long_description_content_type="text/markdown",
    package_dir={"varsome_clinical_api": "varsome_clinical_api"},
    python_requires=">=3.6, <4",
    install_requires=["httpx >= 0.15.0, < 0.19.0", "attrs >= 20.1.0, < 22.0.0", "python-dateutil >= 2.8.0, < 3"],
    package_data={"": ["CHANGELOG.md"], "varsome_clinical_api": ["py.typed"]},
)
