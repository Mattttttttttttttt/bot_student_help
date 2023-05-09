import urllib.request
import tabula
import pandas as pd
url = 'https://mtuci.ru/upload/iblock/6d5/w1ka4v2osqwpfsoqtymayrfdoqe8r07b/BIK2102.pdf'
urllib.request.urlretrieve(url, 'D:\Desktop\Программы Питон\ИТИП_bot\data\BIK2102.pdf')

df = 'D:\Desktop\Программы Питон\ИТИП_bot\data\BIK21021.pdf'
tabula.convert_into(df, 'D:\Desktop\Программы Питон\ИТИП_bot\data\data1.csv',output_format='csv',stream = True)
#df = pd.read_csv('D:\Desktop\Программы Питон\ИТИП_bot\data\data1.csv')
