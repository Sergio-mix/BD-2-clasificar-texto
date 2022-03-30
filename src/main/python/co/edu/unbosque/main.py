import read
import re

if __name__ == '__main__':
    print("")

datos = read.readExcel(
    url='C:/Users/bmore/PycharmProjects/bd-2-clasificar_Texto/src/resources/docs/fb_emp.xlsx'
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


def list_likes(datos):
    list = []
    for dato in datos:
        list.append(dato['likes'])
    return list


def list_comentarios(datos):
    list = []
    for dato in datos:
        list.append(dato['comments'])
    return list


def list_share(datos):
    list = []
    for dato in datos:
        list.append(dato['shares'])
    return list


def calcular_valor(dato):
    max_likes = max(list_likes(datos))
    min_likes = min(list_likes(datos))

    max_comentarios = max(list_comentarios(datos))
    min_comentarios = min(list_comentarios(datos))

    max_shares = max(list_share(datos))
    min_shares = min(list_share(datos))

    maxTotal = (max_likes + max_comentarios + max_shares) / 3

    minTotal = (min_likes + min_comentarios + min_shares) / 3

    medioTotal = (maxTotal + minTotal) / 2
    medioMinimo = medioTotal / 2
    promedio = dato['likes'] + dato['comments'] + dato['shares']
    promedio = promedio / 3
    if promedio > medioTotal:
        return "Bueno"
    elif promedio < medioMinimo:
        return "Malo"
    else:
        return "Regular"

totalBuenos = 0
totalMalos = 0
totalRegular = 0
for dato in datos:

    value = calcular_valor(dato)
    dato["value"] = value
    if (value) == "Bueno":
        totalBuenos += 1
    elif value == "Malo":
        totalMalos += 1
    elif value == "Regular":
        totalRegular += 1


print(datos)
print("Total Buenos: " + str(totalBuenos))
print("Total Malos: " + str(totalMalos))
print("Total Regular: " + str(totalRegular))

