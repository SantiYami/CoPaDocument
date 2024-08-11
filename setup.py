from setuptools import setup, find_packages

setup(
    name="CoPaDocument",
    version="0.1",
    description="A document processing application for various file formats",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="SantiYami",
    # author_email="email@example.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "chardet",
        "defusedxml",
        "et-xmlfile",
        "numpy",
        "odfpy",
        "opencv-python",
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
    extras_require={
        "dev": [
            "pytest",
            "sphinx",
            "black",
            "flake8"
        ],
    },
    entry_points={
        "console_scripts": [
            "copadocument = app.main:main",
        ],
    },
    python_requires='>=3.10.7',  # Versión mínima de Python requerida
)
