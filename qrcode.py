import pyqrcode as pqr
import png
import io

url = pqr.create("Feliz dia da Mulher")
with open('code.png', 'w') as fstream:
    url.png('code.png', scale=5)
url.png('code.png', scale=5)
buffer = io.BytesIO()
url.png(buffer)
print(list(buffer.getvalue()))

