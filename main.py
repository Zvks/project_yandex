import pandas as pd


df = pd.read_csv('C:\projects\project_yandex\.venv\Scripts\jupiter_notebooks\upload.csv', sep=',', na_values=['NA', 'NULL', ' '])
df.columns = df.columns.str.lower().str.replace(' ', '_')
grouped_df = df.groupby(['покупательская_активность'])
print(pd.DataFrame(grouped_df["разность_выручки_тек_прошлый_месяц"].describe()))