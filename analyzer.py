import pandas as pd

# 1. إنشاء بيانات تجريبية لمحاكاة سجل دخول (Logs)
data = {
'IP_Address': ['192.168.1.1', '10.0.0.5', '192.168.1.1', '172.16.0.1'],
'Status': ['Success', 'Failed', 'Failed', 'Success']
}

df = pd.DataFrame(data)

# 2. تحليل البيانات: كم مرة فشل الدخول (محاكاة لهجوم)
failed_attempts = df[df['Status'] == 'Failed']

print("محاولات الدخول الفاشلة:")
print(failed_attempts)
