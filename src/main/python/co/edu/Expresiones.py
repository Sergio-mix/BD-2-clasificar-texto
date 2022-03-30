import re

###Expresiones Regulares para preprocesamiento de texto
###Buscar primera palabra del texto que contenga solo caracteres de nuestro alfabeto
text = "300 fueron los combatientes que pasaron a la historia"
result = re.search(r"[a-zA-z]+", text)
print(result.group(0))

###Buscar si el texto termina en 300
if re.search(r"300$", text):
    print("Match found")
else:
    print("Match not found")

###Buscar si el texto termina en 300
text = "los combatientes que pasaron a la historia eran unos 300"
if re.search(r"300$", text):
    print("Match found")
else:
    print("Match not found")

###Buscar la palabra "que" e indicar dende comienza y termina
#Buscar la palabra "que" todas las veces que se repita e imprimirla
patron = re.compile(r'\bque\b')
print(patron.search(text))
print(patron.findall(text))

###Descomponer el texto en palabras e imprimir la cantidad deseada (5 para este ejemplo)
patron = re.compile(r'\W+')
palabras = patron.split(text)
print(palabras[:5])

###Cambiar una palabra (eran) por otra en un texto (fueron)
eran = re.compile(r'\b(e|E)ran\b')
fueron = eran.sub("fueron", text)
print(fueron)

### Ejemplo extraer correos electrónicos con estructura válida - VERBOSE
# comienzo de delimitador de palabra: \b
# usuario: cualquier caracter alfanumerico mas los signos (.%+-): [\w.%+-]+
# seguido de @: @
# dominio: Cualquier caracter alfanumerico mas los signos (.-): [\w.-]+
# seguido de . : \.
# dominio de alto nivel: mínimo 2 a máximo 6 caracteres en minúsculas o mayúsculas: [a-zA-Z]{2,6}
# fin de delimitador de palabra: \b

mail = re.compile(r' \b[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,6}\b', re.X)
mails = "santiago.salazarf@gmail.com, Santiago Salazar Fajardo, buen servicio, gerardopelaez@uniminuto.edu.co, pedro@github.io,https://pedroroso.com.co, https://gerardopelaez.github.io,python@python"
print(mail.findall(mails))