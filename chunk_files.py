import pandas as pd

# Configurar los datos en el archivo para iterar cada X líneas
reader = pd.read_table(r'./Downloads/BorrarProducts.csv',
                    header=None, sep='\n', chunksize=5000, iterator=True)

# Archivo de guardado iterativo
i = 0
for chunk in reader:
    file_name = 'file_id_chunk_' + str(i) + '.csv'
    print('Guardado {}th archivo ...'.format(i))
    chunk.to_csv(file_name, encoding='utf-8')
    i += 1