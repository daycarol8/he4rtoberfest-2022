def tipo_triangulo(a: float, b: float, c: float) -> str:
    if a >= b + c:
        return 'NAO FORMA TRIANGULO'
    elif a ** 2 == b ** 2 + c ** 2:
        return 'TRIANGULO RETANGULO'
    elif a ** 2 > b ** 2 + c ** 2:
        return 'TRIANGULO OBTUSANGULO'
    elif a ** 2 < b ** 2 + c ** 2:
        return 'TRIANGULO ACUTANGULO'
    elif a == b == c:
        return 'TRIANGULO EQUILATERO'
    elif a == b or c == b:
        return 'TRIANGULO ISOSCELES'

if __name__ == '__main__':
    lados = [float(n) for n in  input().split()]
    lados.sort()
    a, b, c = lados[2], lados[1], lados[0]
    print(tipo_triangulo(a, b, c))