"""
Reto 4: ¿Cuántas latas de refresco sobran?

Un acto de graduación es la ceremonia oficial que clausura el curso 
escolar y sirve de reconocimiento a los estudiantes que han completado 
los requisitos académicos de un plan de estudios y, por lo tanto, se 
han hecho merecedores del título académico.

Para organizar una fiesta de graduación del instituto se compran 9 
cajas de refrescos, donde cada caja contiene 24 latas de refrescos. 
Invitamos a 56 personas y queremos que todas y cada una de ellas consuman 
la misma cantidad de refrescos ¿Cuántas latas de refresco sobrarán?

"""
# Datos de entrada

cajas_refresco = 9
refrescos_caja = 24
personas = 56


# Proceso

sobra = (cajas_refresco*refrescos_caja) % personas 

# Salida

print("Sobran", sobra , "refrescos")