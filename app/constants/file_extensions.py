# Extensiones de archivos
PDF_EXTENSION = '.pdf'
XLSX_EXTENSION = '.xlsx'
XLS_EXTENSION = '.xls'
ODS_EXTENSION = '.ods'
CSV_EXTENSION = '.csv'

IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

# Propiedades de los archivos
PAGES = 'pages'
SHEETS = 'sheets'
ROWS = 'rows'
COLUMNS = 'columns'
WIDTH = 'width'
HEIGHT = 'height'
CHANNELS = 'channels'

FILE_PROPERTIES = {
    PDF_EXTENSION: [PAGES],
    XLSX_EXTENSION: [SHEETS],
    XLS_EXTENSION: [SHEETS],
    ODS_EXTENSION: [SHEETS],
    CSV_EXTENSION: [ROWS, COLUMNS],
}

# Agregar propiedades de las imágenes utilizando comprensión de listas
FILE_PROPERTIES.update({ext: [WIDTH, HEIGHT, CHANNELS] for ext in IMAGE_EXTENSIONS})
