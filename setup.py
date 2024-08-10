from setuptools import setup, find_packages

setup(
    name="CoPaDocument",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "PyPDF2",
        "tkinterdnd2",
    ],
    entry_points={
        "console_scripts": [
            "copadocument = app.main:main",
        ],
    },
    python_requires='>=3.10.7',  # Versión mínima de Python requerida
)
