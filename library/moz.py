import pandas as pd
from django.contrib.auth.models import User

file = 'students_list.xlsx'
data = pd.read_excel(file, sheet_name='هفتم')
for i in data.dropna().values[1:]:
    User.objects.create_user(username=i[2], password=str(i[1]))

