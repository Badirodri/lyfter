# 5. Dada `n` cantidad de notas de un estudiante, calcular:
#     1. Cuantas notas tiene aprobadas (mayor a 70).
#     2. Cuantas notas tiene desaprobadas (menor a 70).
#     3. El promedio de todas.
#     4. El promedio de las aprobadas.
#     5. El promedio de las desaprobadas.

total_notas = int(input("Digite cuantas notas desea agregar: "))
nota = 0
contador = 0
promedio = 0
aprobadas = 0
reprobadas = 0
promedio_aprobadas = 0
promedio_reprobadas = 0


while (contador < total_notas):
    nota = int(input("Digite la nota: "))
    if (nota >= 70):
        aprobadas = aprobadas + 1
        promedio_aprobadas = promedio_aprobadas + nota
        promedio = promedio + nota
        contador = contador + 1
    else:
        reprobadas = reprobadas + 1
        promedio_reprobadas = promedio_reprobadas + nota
        promedio = promedio + nota
        contador = contador + 1

promedio_reprobadas = promedio_reprobadas // reprobadas
promedio_aprobadas = promedio_aprobadas // aprobadas
promedio = promedio // total_notas

print (f"""
El estudiante tiene:
    Aprobadas: {aprobadas}
    Reprobadas: {reprobadas}
    Promedio Total: {promedio}
    Promedio Aprobadas: {promedio_aprobadas}
    Promedio Reprobadas: {promedio_reprobadas}
""")