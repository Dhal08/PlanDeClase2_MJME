# MJME (Melany Mejía)

# Ultimo ejercicio de Phyton sobre operadores
# ----------------------------------------------------------------

# Datos del estudiante ingresados por el sistema

Nombre_Estudiante = "Carolina Garcia"
Promedio = 90
Matricula_Pagada = True
Activo = False

# Datos institucionales

Estudiante_Registrado = Nombre_Estudiante
Registro_Oficial = Nombre_Estudiante # misma referencia
Alumnos_Autorizados = ["Laura Gomez", "Carlos Mendez", "Ana Ruiz"]

# Validaciones

Promedio_Valido = Promedio >= 75
Estado_Valido = Matricula_Pagada and Activo
Mismo_Registro = Estudiante_Registrado is Registro_Oficial
Autorizado = Nombre_Estudiante in Alumnos_Autorizados

# Mostrar resultados

print("Promedio válido:", Promedio_Valido)
print("Estado de cuenta y activo:", Estado_Valido)
print("¿Es el mismo registro oficial?", Mismo_Registro)
print("¿Está en la lista de autorizados?", Autorizado)

# Validación final combinada

Puede_Presentar_Examen = Promedio_Valido and Estado_Valido and Mismo_Registro and Autorizado
print("¿Puede presentar el examen final?", Puede_Presentar_Examen)
# ----------------------------------------------------------------