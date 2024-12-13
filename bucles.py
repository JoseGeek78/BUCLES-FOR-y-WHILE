colores = ['Red', 'Blue', 'Green', 'Yellow']

print('---COLOR LIST---')

for color in colores:
    if color == 'Blue' or color == 'Green' or color == 'Red':
        print('Se ha saltado este valor.')
        continue
    print(f'-Color {color}.')



# colores = ['Rojo', 'Azul', 'Blanco', 'Amarillo', 'Verde']
# print('---LISTADO DE COLORES---')

# for color in colores:
#    print(f'-{color}.')

# for i in range(5,-24,-3):
#    print(f'El valor del bucle es: {i}.')
    
# print('Fin del bucle.')    