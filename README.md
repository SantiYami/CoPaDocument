
# CoPaDocument - Document Info Viewer

CoPaDocument es una aplicación de escritorio ligera para visualizar información básica sobre archivos PDF y Excel. Con esta aplicación, puedes obtener detalles como la ruta, el tamaño del archivo y la cantidad de páginas en el caso de PDFs, así como el tamaño y la cantidad de archivos Excel en una carpeta. La aplicación está diseñada para ser extensible, lo que permite agregar fácilmente soporte para nuevos tipos de documentos.

## Características

- **Arrastrar y soltar:** Simplemente arrastra y suelta carpetas o archivos en la interfaz para ver la información.

- **Visualización de información:** Muestra la ruta, tamaño y cantidad de páginas para archivos PDF; tamaño, cantidad de archivos y detalles para archivos Excel; y detalles de las imágenes como dimensiones y número de canales.

- **Extensible:** Diseñada para que sea fácil agregar soporte para nuevos tipos de documentos.

- **Interfaz gráfica amigable:** Interfaz de usuario simple y limpia construida con `Tkinter` y `TkinterDnD`.

## Requisitos

- **Python 3.8 o superior**
- **Dependencias**:
  - `chardet` (para detectar el encoding de archivos CSV)
  - `defusedxml` (para la seguridad en el procesamiento de XML)
  - `et-xmlfile` (para leer archivos XML)
  - `numpy` (para operaciones matemáticas eficientes)
  - `odfpy` (para manejar archivos ODS)
  - `opencv-python` (para manejar imágenes)
  - `openpyxl` (para manejar archivos XLSX)
  - `pandas` (para manejo avanzado de datos)
  - `PyPDF2` (para manejar archivos PDF)
  - `python-dateutil` (para el manejo de fechas)
  - `pytz` (para manejo de zonas horarias)
  - `pyxlsb` (para leer archivos XLSB)
  - `six` (para compatibilidad entre Python 2 y 3)
  - `tkinterdnd2` (para funcionalidad de arrastrar y soltar)
  - `tzdata` (para datos de zona horaria)
  - `xlrd` (para leer archivos XLS)

## Instalación en local

1. Clona el repositorio:

```bash
git clone https://github.com/SantiYami/CoPaDocument.git
cd CoPaDocument
```

2. Crea un entorno virtual (opcional pero recomendado):

```bash
python -m venv .venv
source .venv/bin/activate  # En Windows usa: .venv\Scripts\activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Instala la aplicación (opcional, para ejecutar desde cualquier lugar):

```bash
pip install .
```

## Uso

### Ejecución desde la línea de comandos

Después de instalar la aplicación, puedes ejecutarla desde cualquier lugar con el siguiente comando:

```bash
copadocument
```

### Ejecución desde el código fuente

Si prefieres ejecutar la aplicación directamente desde el código fuente, usa el siguiente comando:

```bash
python -m app.main
```

### Características adicionales

- **Agregar soporte para nuevos tipos de documentos:** Para añadir un nuevo tipo de documento, solo necesitas crear un nuevo manejador que implemente la interfaz `DocumentHandler` y añadirlo a la fábrica (`DocumentHandlerFactory`) en `app/handlers/base/document_handler_factory.py`.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue los pasos de instalación y asegúrate de que todo funcione correctamente antes de enviar un Pull Request.

## Licencia

Este proyecto está licenciado bajo la [MIT License](https://github.com/SantiYami/CoPaDocument?tab=MIT-1-ov-file).
