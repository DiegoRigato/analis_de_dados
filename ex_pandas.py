import pandas as pd 
'''dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos'],
    'Idade': [23, 31, 19],
    'Cidade': ['SP', 'RJ', 'BH'],
    
}'''


df = pd.read_csv('pessoas.csv')
adultos = (df[df['idade'] > 20])
df['idade_mais_5'] = df['idade'] + 5
print(df.sort_values(by = 'idade'))