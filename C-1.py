from PIL import Image
import os
# PDF変換
Chiba_Gesui = Image.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image/B-1.png'))
CG1 = Chiba_Gesui.convert("RGB")
pdfPath1 = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pdf/CG1.pdf')
CG1.save(pdfPath1)

Chiba_Doro = Image.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image/B-2.png'))
CG2 = Chiba_Doro.convert("RGB")
pdfPath2 = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pdf/CG2.pdf')
CG2.save(pdfPath2)

Saitama_Gesui = Image.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image/B-3.png'))
CG3 = Saitama_Gesui.convert("RGB")
pdfPath3 = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pdf/CG3.pdf')
CG3.save(pdfPath3)

Saitama_Doro = Image.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image/B-4.png'))
CG4 = Saitama_Doro.convert("RGB")
pdfPath4 = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pdf/CG4.pdf')
CG4.save(pdfPath4)