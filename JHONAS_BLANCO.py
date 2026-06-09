total_estudiantes = 0
aprobados = 0
reprobados_nota = 0
reprobados_asistencia = 0

opcion = "S"

while opcion.upper() == "S":

    nombre = input("Ingrese el nombre del estudiante: ")
    clases_programadas = int(input("Ingrese el total de clases programadas: "))
    clases_asistidas = int(input("Ingrese el total de clases asistidas: "))
    nota = float(input("Ingrese la nota final: "))

    asistencia = (clases_asistidas * 100) / clases_programadas

    if asistencia < 80:
        estado = "Reprobado por asistencia"
        reprobados_asistencia = reprobados_asistencia + 1

    else:
        if nota >= 51:
            estado = "Aprobado"
            aprobados = aprobados + 1
        else:
            estado = "Reprobado por nota"
            reprobados_nota = reprobados_nota + 1

    print("\n--- RESULTADO DEL ESTUDIANTE ---")
    print("Nombre:", nombre)
    print("Porcentaje de asistencia:", asistencia, "%")
    print("Nota final:", nota)
    print("Estado:", estado)

    total_estudiantes = total_estudiantes + 1

    opcion = input("\n¿Desea registrar otro estudiante? (S/N): ")

if total_estudiantes > 0:
    porcentaje_aprobados = (aprobados * 100) / total_estudiantes
else:
    porcentaje_aprobados = 0

print("\n===== ESTADISTICAS FINALES =====")
print("Total de estudiantes:", total_estudiantes)
print("Aprobados:", aprobados)
print("Reprobados por nota:", reprobados_nota)
print("Reprobados por asistencia:", reprobados_asistencia)
print("Porcentaje de aprobados:", porcentaje_aprobados, "%")