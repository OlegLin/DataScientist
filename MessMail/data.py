import pandas as pd

adresspeople = pd.read_csv('datafr.csv', usecols=['adress'])



metapeople = pd.read_csv('datafr.csv', usecols=['adress', 'Наименование ППЭ', 'Наименование экзамена', 'Код ОО участника', 'Краткое наименование ОО участника', 'ФИО участника', 'Время прибытия в ОО'])

print(len(metapeople))
