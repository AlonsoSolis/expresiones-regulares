import re
import pandas as pd


# Función para modificar el texto
def modify_text(text):
    # Anular el espacio después de "NG45Y"
    text = re.sub(r'NG45Y\s', 'NG45Y', text)
    # Cambiar "." por "/" en las fechas (formato: 2024.XX.XX)
    text = re.sub(r'(\d{4})\.(\d{2})\.(\d{2})', r'\1/\2/\3', text)
    # Cambiar "." por ":" en los tiempos (formato: XX.XX.XX)
    text = re.sub(r'(\d{2})\.(\d{2})\.(\d{2})$', r'\1:\2:\3', text)
    # Suplantar el "." entre fecha y hora con un espacio (formato: 2024/XX/XX.HH:MM:SS)
    text = re.sub(r'(\d{4}/\d{2}/\d{2})\.(\d{2}:\d{2}:\d{2})', r'\1 \2', text)
    # Mantener un espacio después de "Gate"
    text = re.sub(r'Gate(\d)', r'Gate \1', text)
    # Mantener un espacio antes y después de "at"
    text = re.sub(r'(\d)at(\d)', r'\1 at \2', text)
    return text

# Leer el archivo original
file_path = "C:/Users/Pandora/OneDrive/Documentos/2.Curso semiconductores/1.Electronica Avanzada/CellGate_with_timestamps_250.txt"
data = pd.read_csv(file_path, sep='\t', header=None)

# Aplicar las modificaciones a cada línea
modified_lines = data.applymap(modify_text)

# Guardar las modificaciones en un nuevo archivo
modified_file_path = "C:/Users/Pandora/OneDrive/Documentos/2.Curso semiconductores/1.Electronica Avanzada/CellGate_with_timestamps_250_modified_v2.txt"
modified_lines.to_csv(modified_file_path, sep='\t', index=False, header=False)

# Mostrar las primeras filas modificadas
print(modified_lines.head())

# GitHub gigsfile code
#<script src="https://gist.github.com/AlonsoSolis/8d1dfccc908ff57c63a05f9287164a31.js"></script>