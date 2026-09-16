import pandas as pd
import json

df = pd.read_excel('MAPACHE.xlsx', sheet_name=0)
headers = df.iloc[2].values[:len(df.columns)]
data_df = df.iloc[3:].copy()
data_df.columns = [str(h).strip() for h in headers]
data_df['id_colegio'] = pd.to_numeric(data_df['id_colegio'], errors='coerce')
valid_schools = data_df[(data_df['id_colegio'] >= 1) & (data_df['id_colegio'] <= 146)].copy()

js_schools = []
for idx, row in valid_schools.iterrows():
    # Creamos un diccionario limpio por cada colegio
    school_dict = {
        "id_colegio": int(row['id_colegio']) if pd.notna(row['id_colegio']) else 0,
        "departamento": str(row['departamento']) if pd.notna(row['departamento']) else '',
        "ugel": str(row['ugel']) if pd.notna(row['ugel']) else '',
        "distrito": str(row['distrito']) if pd.notna(row['distrito']) else '',
        "nombre_colegio": str(row['nombre_colegio']) if pd.notna(row['nombre_colegio']) else '',
        "gestion": str(row['gestion']) if pd.notna(row['gestion']) else '',
        "red_educativa": str(row['red_educativa']) if pd.notna(row['red_educativa']) else '',
        "niveles": str(row['niveles']) if pd.notna(row['niveles']) else '',
        "TURNOS": str(row['TURNOS']) if pd.notna(row['TURNOS']) else '',
        "latitud": float(row['latitud']) if pd.notna(row['latitud']) else 0.0,
        "longitud": float(row['longitud']) if pd.notna(row['longitud']) else 0.0,
        "direccion": str(row['direccion']).replace('\n', ' ') if pd.notna(row['direccion']) else '',
        "enlace_web_o_whatsapp": str(row['enlace_web_o_whatsapp']) if pd.notna(row['enlace_web_o_whatsapp']) else '',
        "vacante_inicial": str(row['vacante_inicial']) if pd.notna(row['vacante_inicial']) else '',
        "vacante_primaria": str(row['vacante_primaria']) if pd.notna(row['vacante_primaria']) else '',
        "vacante_secundaria": str(row['vacante_secundaria']) if pd.notna(row['vacante_secundaria']) else '',
        "requisitos_de_matricula": str(row['requisitos_de_matricula']).replace('\n', ' ') if pd.notna(row['requisitos_de_matricula']) else '',
        "password_director": str(row['password_director']) if pd.notna(row['password_director']) else '',
        "ultima_modificacion": str(row['ultima_modificacion']) if pd.notna(row['ultima_modificacion']) else '',
        "estado_vigencia": str(row['estado_vigencia']) if pd.notna(row['estado_vigencia']) else '',
        "estado_sello_aliado": str(row['estado_sello_aliado']) if pd.notna(row['estado_sello_aliado']) else '',
        "fecha_aporte_aliado": str(row['fecha_aporte_aliado']) if pd.notna(row['fecha_aporte_aliado']) else '',
        "membresia_particular": str(row['membresia_particular']) if pd.notna(row['membresia_particular']) else '',
        "inicio_membresia": str(row['inicio_membresia']) if pd.notna(row['inicio_membresia']) else '',
        "vencimiento_membresia": str(row['vencimiento_membresia']) if pd.notna(row['vencimiento_membresia']) else ''
    }
    js_schools.append(school_dict)

# Convertimos la lista de Python a un archivo JavaScript válido usando formato JSON seguro
json_data = json.dumps(js_schools, ensure_ascii=False, indent=2)

with open('colegios.js', 'w', encoding='utf-8') as f:
    f.write('const colegios = ')
    json.dump(js_schools, f, ensure_ascii=False)
    f.write(';')

print("¡Archivo colegios.js generado a prueba de errores con JSON!")