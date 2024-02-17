import re 
from colorama import Fore
import requests

website = 'https://hidrografia2.agpse.gob.ar/Ituzaingo/index.html'

resultado = requests.get(website)
content = resultado.text
print(content)