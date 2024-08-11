import tkinter as tk
from tkinter import ttk
from tkinterdnd2 import DND_FILES, TkinterDnD
from .utils.file_utils import get_file_info
from .utils.format_utils import format_size

def run_app():
    root = TkinterDnD.Tk()
    root.title("CoPaDocument - Document Info Viewer")
    root.geometry("800x400")
    
    # Configurar estilo para Treeview
    style = ttk.Style()
    style.theme_use('vista')
    style.configure("Treeview",
                    highlightthickness=0,
                    bd=0,)
    style.configure("Treeview.Heading",)
    style.configure("Treeview", rowheight=30)
    style.map('Treeview', background=[('selected', 'lightblue')])

    # Frame para la tabla y la barra de desplazamiento
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    columns = ("path", "pages", "size")
    table = ttk.Treeview(frame, columns=columns, show="headings", selectmode="browse")
    table.heading("path", text="Path")
    table.heading("pages", text="Pages")
    table.heading("size", text="Size")

    table.column("path", width=400, anchor="w")
    table.column("pages", width=100, anchor="center")
    table.column("size", width=100, anchor="center")

    # Crear barras de desplazamiento
    vsb = ttk.Scrollbar(table, orient="vertical", command=table.yview)
    hsb = ttk.Scrollbar(table, orient="horizontal", command=table.xview)
    table.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    
    table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    vsb.pack(side=tk.RIGHT, fill="y")
    hsb.pack(side=tk.BOTTOM, fill="x")

    # Área de texto para el mensaje "Drag and Drop"
    drop_label = tk.Label(root, text="Drag and Drop Folder or File Here", pady=10, padx=20, bg="lightgray")
    drop_label.pack(fill=tk.X, side=tk.TOP)

    def update_table(files_info):
        document_info, total_size, file_count = files_info

        for item in table.get_children():
            table.delete(item)

        for info in document_info:
            table.insert("", "end", values=(info["path"], info.get("pages", "-"), info["format_size"]))

        # Display totals
        table.insert("", "end", values=("Total", file_count, f"{format_size(total_size)}"))

    def on_drop(event):
        directory = event.data.strip('{}')
        files_info = get_file_info(directory)
        update_table(files_info)

    root.drop_target_register(DND_FILES)
    root.dnd_bind('<<Drop>>', on_drop)

    root.mainloop()
