def print_letter(letter):
    # Código de escape ANSI para cambiar el color del texto a verde
    green_color = "\033[92m"

    # Código de escape ANSI para restablecer el color del texto al valor por defecto
    reset_color = "\033[0m"

    # Imprimir la letra en verde
    print(green_color + letter + reset_color)

# Llamar a la función para imprimir la letra 'X' en verde
print_letter('X')