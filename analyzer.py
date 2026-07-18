import pandas as pd

# 1. إنشاء بيانات تجريبية
data = {
'IP_Address': ['192.168.1.1', '10.0.0.5', '192.168.1.1', '172.16.0.1'],
'Status': ['Success', 'Failed', 'Failed', 'Success']
}

df = pd.DataFrame(data)

# 2. تصفية البيانات (عرض المحاولات الفاشلة فقط)
failed_attempts = df[df['Status'] == 'Failed']
print("--- المحاولات الفاشلة بالتفصيل ---")
print(failed_attempts)

# 3. تحليل البيانات (حساب عدد المرات لكل IP)
failed_counts = failed_attempts['IP_Address'].value_counts()
print("\n--- إجمالي المحاولات الفاشلة لكل IP ---")
print(failed_counts)
