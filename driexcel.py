from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from openpyxl import Workbook

# Autenticación en Google Drive
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

# Crear un archivo de Excel
wb = Workbook()
ws = wb.active
ws.title = "Enlaces PDF"

# Obtener archivos de Google Drive
folder_id = 'https://drive.google.com/drive/folders/1tMYTpfzpF3jpRUmaKGn6KJbg_mzXt-fZ?usp=drive_link'  # Reemplaza esto con el ID de tu carpeta de Google Drive
file_list = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()

# Agregar enlaces de archivos PDF a la hoja de Excel
row = 1
for file in file_list:
    if file['mimeType'] == 'application/pdf':
        pdf_link = f"https://drive.google.com/uc?id={file['id']}"
        ws.cell(row=row, column=1, value=pdf_link)
        row += 1

# Guardar el archivo de Excel
wb.save("enlaces_pdf.xlsx")
print("Enlaces guardados en enlaces_pdf.xlsx")
