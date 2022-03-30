import read
import re

if __name__ == '__main__':
    print("")

datos = read.readExcel(
    url='C:/Users/alejo/IdeaProjects/bd-2-clasificar_Texto/src/resources/docs/fb_emp.xlsx'
)


def calcular_Categoria(text):
    list = ["mercado"]
    patron = re.compile(r'\W+')
    palabras = patron.split(text)
    print(palabras)
    for palabra in palabras:
        if list.count(palabra):
            return palabra
    return None


print(calcular_Categoria(datos[2]['text']))
