from PIL import Image
import os
import PyPDF2

# PDF変換
Chiba_Gesui = Image.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image/B1.png'))
CG1 = Chiba_Gesui.convert("RGB")
pdfPath1 = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pdf/CG.pdf')
CG1.save(pdfPath1)

Chiba_Doro = Image.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image/B2.png'))
CG2 = Chiba_Doro.convert("RGB")
pdfPath2 = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pdf/CD.pdf')
CG2.save(pdfPath2)

# Saitama_Gesui = Image.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image/B3.png'))
# CG3 = Saitama_Gesui.convert("RGB")
# pdfPath3 = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pdf/SG.pdf')
# CG3.save(pdfPath3)

# Saitama_Doro = Image.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image/B4.png'))
# CG4 = Saitama_Doro.convert("RGB")
# pdfPath4 = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pdf/SD.pdf')
# CG4.save(pdfPath4)

merger = PyPDF2.PdfFileMerger()

merger.append(pdfPath1)
merger.append(pdfPath2)
# merger.append(pdfPath3)
# merger.append(pdfPath4)

pdfPath5 = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pdf/info.pdf')

merger.write(pdfPath5)

merger.close()