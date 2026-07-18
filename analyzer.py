import pandas as pd

# قراءة البيانات من ملف خارجي
df = pd.read_csv('logs.csv')

# التحليل
failed_attempts = df[df['Status'] == 'Failed']
print(failed_attempts['IP_Address'].value_counts())
