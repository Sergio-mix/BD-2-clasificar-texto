import read
import re

if __name__ == '__main__':
    print("")

datos = read.readExcel(
    url='C:/Users/alejo/IdeaProjects/bd-2-clasificar_Texto/src/resources/docs/fb_emp.xlsx'
)


def returnProduct(text, list):
    for product in list:
        if product["text"] == text:
            return product["return"]


def calcular_Product(text):
    list = [
        {"text": "colegio", "return": "utiles"},
        {"text": "smartphone", "return": "celular"},
        {"text": "disney", "return": "peliculas"},
        {"text": "películas", "return": "películas"},
        {"text": "it", "return": "tecnología"},
        {"text": "desarrolladores", "return": "tecnología"},
        {"text": "navidad", "return": "regalos"}
    ]

    listProducts = ["colegio", "smartphone", "disney", "películas", "it", "desarrolladores", "navidad"]

    patron = re.compile(r'\W+')
    for palabra in patron.split(text):
        if listProducts.count(palabra) == 1:
            return returnProduct(palabra, list)
    return "No se encontro"


for dato in datos:
    if dato["text"] == "":
        datos.remove(dato)
    else:
        dato["product"] = calcular_Product(dato["text"])

print(datos)
