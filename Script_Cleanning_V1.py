import pandas as pd
import re

def clean_description(description, df_pv_es, df_pv_es_sys, df_pv_abr, df_pv_comp, df_pv_marit, df_pv_marca, df_pv_merca, df_pv_in, df_pv_in_sys, df_vp_valid):
    print('... Executing Cleaning ...')
    try:
        words = description.split()
        print('Remove Non-Alfanumeric Characters & Numbers: ', words)
        words_cleaned = [re.sub(r'[^a-zA-Z\s]', '', word) for word in words]
        print('Remove Single Digit Numbers: ', words_cleaned)
        words_cleaned = [re.sub(r'\b\d\b', '', word) for word in words_cleaned]

        print('Keeps 3 Digit Characters In WhiteList: ', words_cleaned)
        words_3_chars = [word for word in words_cleaned if len(word) == 3]
        words_cleaned = [
                        word for word in words_cleaned
                        if len(word) != 3 or (len(word) == 3 and
                        (word in set(df_vp_valid[(df_vp_valid['bstatus'] == 0) &
                        (df_vp_valid['des'].isin(words_3_chars))]['des'])))
                        ]

        print('Remove Single Letter Words: ', words_cleaned)
        words_cleaned = [word for word in words_cleaned if len(word) > 1]

        print('Remove From Black Lists: ', words_cleaned)
        words_to_remove_pv_es = set(df_pv_es[df_pv_es['bstatus'] == 0]['des'])
        words_cleaned = [word for word in words_cleaned if word not in words_to_remove_pv_es]

        words_to_remove_pv_es_sys = set(df_pv_es_sys[df_pv_es_sys['bstatus'] == 0]['des'])
        words_cleaned = [word for word in words_cleaned if word not in words_to_remove_pv_es_sys]

        words_to_remove_pv_abr = set(df_pv_abr[df_pv_abr['bstatus'] == 0]['des'])
        words_cleaned = [word for word in words_cleaned if word not in words_to_remove_pv_abr]

        words_to_remove_pv_comp = set(df_pv_comp[df_pv_comp['bstatus'] == 0]['des'])
        words_cleaned = [word for word in words_cleaned if word not in words_to_remove_pv_comp]

        words_to_remove_pv_marit = set(df_pv_marit[df_pv_marit['bstatus'] == 0]['des'])
        words_cleaned = [word for word in words_cleaned if word not in words_to_remove_pv_marit]

        words_to_remove_pv_marca = set(df_pv_marca[df_pv_marca['bstatus'] == 0]['des'])
        words_cleaned = [word for word in words_cleaned if word not in words_to_remove_pv_marca]

        words_to_remove_pv_merca = set(df_pv_merca[df_pv_merca['bstatus'] == 0]['des'])
        words_cleaned = [word for word in words_cleaned if word not in words_to_remove_pv_merca]

        words_to_remove_pv_in = set(df_pv_in[df_pv_in['bstatus'] == 0]['des'])
        words_cleaned = [word for word in words_cleaned if word not in words_to_remove_pv_in]

        words_to_remove_pv_in_sys = set(df_pv_in_sys[df_pv_in_sys['bstatus'] == 0]['des'])
        words_cleaned = [word for word in words_cleaned if word not in words_to_remove_pv_in_sys]

        print('Remove Duplicated Words: ', words_cleaned)
        words_cleaned = list(dict.fromkeys(words_cleaned))

        print('Remove Duplicated Spaces', words_cleaned)
        cleaned_description = ' '.join(words_cleaned).strip()
        print(' ||| Result ||| ', words_cleaned)
        return cleaned_description

    except AttributeError:
        print('¡¡¡ Failed Load !!!')
        return ''

df = pd.read_excel('LIMPIEZA.xlsx', sheet_name='list')
df_pv_es = pd.read_excel('PV_ES.xlsx', sheet_name='black1')
df_pv_es_sys = pd.read_excel('PV_ES_SYS.xlsx', sheet_name='black2')
df_pv_abr = pd.read_excel('PV_ABREVIATURAS.xlsx', sheet_name='black3')
df_pv_comp = pd.read_excel('PV_COMPUESTAS.xlsx', sheet_name='black4')
df_pv_marit = pd.read_excel('PV_MARITIMO.xlsx', sheet_name='black5')
df_pv_marca = pd.read_excel('PV_MARCAS.xlsx', sheet_name='black6')
df_pv_merca = pd.read_excel('PV_MERCANCIAS.xlsx', sheet_name='black7')
df_pv_in = pd.read_excel('PV_IN.xlsx', sheet_name='black8')
df_pv_in_sys = pd.read_excel('PV_IN_SYS.xlsx', sheet_name='black9')
df_vp_valid = pd.read_excel('VP_VALID.xlsx', sheet_name='white1')

df['MERC_DESCRIPCION'] = df['MERC_DESCRIPCION'].astype(str)
#df.dropna(subset = ['MERC_DESCRIPTION'], inplace=True)
df['MERC_DESCRIPCION'] = df['MERC_DESCRIPCION'].fillna('')

df['CLEANED_DESCRIPTION'] = df['MERC_DESCRIPCION'].apply(lambda x: clean_description(x, df_pv_es, df_pv_es_sys, df_pv_abr, df_pv_comp, df_pv_marit, df_pv_marca, df_pv_merca, df_pv_in, df_pv_in_sys, df_vp_valid))

df.to_excel('merchandise_cleaned_file.xlsx', index=False)