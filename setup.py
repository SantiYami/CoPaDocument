from setuptools import setup, find_packages

setup(
    name="CoPaDocument",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "chardet",
        "defusedxml",
        "et-xmlfile",
        "numpy",
        "odfpy",
        "openpyxl",
        "pandas",
        "PyPDF2",
        "python-dateutil",
        "pytz",
        "pyxlsb",
        "six",
        "tkinterdnd2",
        "tzdata",
        "xlrd"
    ],
    entry_points={
        "console_scripts": [
            "copadocument = app.main:main",
        ],
    },
    python_requires='>=3.10.7',  # Versión mínima de Python requerida
)
