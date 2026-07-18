import pandas as pd

# قراءة البيانات من ملف خارجي
df = pd.read_csv('logs.csv')

# تحليل المحاولات الفاشلة
failed_attempts = df[df['Status'] == 'Failed']

print("--- تقرير المحاولات الفاشلة ---")
print(failed_attempts)

print("\n--- تكرار المحاولات لكل عنوان IP ---")
print(failed_attempts['IP_Address'].value_counts())
