import pandas as pd
df = pd.read_excel(r"C:\Users\eshwar\Downloads\Hackathon_Timesheet.xlsx")
print(df.groupby(['Team','Project Name'])['Hours'].mean().rename('Mean').to_frame())
Employee_with_low_efficiency=df.sort_values(['Hours'],ascending=[False]).head()
print(Employee_with_low_efficiency)

