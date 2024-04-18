# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(largo, ancho):
    area = largo * ancho
    return area

# Función para calcular el área de un triángulo
def calcular_area_triangulo(base, altura):
    area = 0.5 * base * altura
    return area

# Función principal
def main():
    x = 4
    y = 6
    area_rectangulo = calcular_area_rectangulo(x, y)
    print("Área del rectángulo:", area_rectangulo)

    base = 5
    altura = 8
    area_triangulo = calcular_area_triangulo(base, altura)
    print("Área del triángulo:", area_triangulo)

main()