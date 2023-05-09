import pandas as pd


exel_file = pd.ExcelFile('D:\Desktop\Программы Питон\ИТИП_bot\data\BIK2102.xlsx')
df = pd.read_excel(exel_file)
#print(df)
col_names = [
    'day',
    'l_num',
    'l_time',
    'l_room_1',
    'l_type_1',
    'lector_1',
    'discipline_1',
    'discipline_2',
    'lector_2',
    'l_type_2',
    'l_room_2'
]
df.columns = col_names
#print(df)
indexes = list(df.columns)
indexes[:len(col_names)] = col_names
df.columns = indexes
norm_t_table = df[df['l_time'].notna()].copy()
norm_t_table.dropna(
    axis=1,
    how='all',
    inplace=True
)
norm_t_table['day'] = norm_t_table['day'].ffill()
col_to_drop = [col for col in norm_t_table.columns if col not in col_names]
norm_t_table.drop(
    columns=col_to_drop,
    inplace=True
)
norm_t_table.drop(
    norm_t_table[norm_t_table['day'] == 'День недели'].index,
    inplace=True
)
rows = norm_t_table[norm_t_table['l_room_1'].isnull() == True]
rows = rows[norm_t_table['l_room_2'].isnull() == True]
norm_t_table.drop(
    index = rows.index,
    inplace = True
)
print(norm_t_table)