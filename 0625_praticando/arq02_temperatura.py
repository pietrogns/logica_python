def fahrenheit_para_celsius(f):
    """Converte temperatura de Fahrenheit para Celsius"""
    celsius = (f - 32) * 5 / 9
    return celsius

temp = 98
celsius = fahrenheit_para_celsius
print(celsius)

#A função foi definida, mas nada aconteceu ainda
# Precisamos chamá-la

temp_f = 98.6
resultado = fahrenheit_para_celsius(temp_f)
print(f"{temp_f}°F equivalem a {resultado:.2f}°C")

# Também podemos chamar direteamente:
print(fahrenheit_para_celsius(32)) #0.0
print(fahrenheit_para_celsius(212)) #100.0

