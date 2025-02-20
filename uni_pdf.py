import PyPDF2
import os 

merge = PyPDF2.PdfMerger()

listar_arquivos = os.listdir("arquivos")
listar_arquivos.sort()

for arquivo in listar_arquivos:
    if(".pdf" in arquivo):
        merge.append(f"arquivos/{arquivo}")

merge.write("JUNÇÃO.PDF")