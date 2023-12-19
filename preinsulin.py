import re

# Lee el contenido del archivo
with open('preproinsulin-seq.txt', 'r') as file:
    content = file.read()

# Aplica expresiones regulares para la limpieza
cleaned_content = re.sub(r'ORIGIN|\d|\/\/|\s', '', content)

# Confirma si la longitud es 110 caracteres
if len(cleaned_content) == 110:
    # Guarda el contenido limpio en un nuevo archivo
    with open('preproinsulin-seq-cleaned.txt', 'w') as cleaned_file:
        cleaned_file.write(cleaned_content)
    print("Limpieza exitosa. El contenido limpio se ha guardado en preproinsulin-seq-cleaned.txt.")
else:
    print("El archivo no tiene 110 caracteres después de la limpieza.")
