# 1
import pandas as pd

# 2
sal = pd.read_csv('Salaries.csv', low_memory=False)
# 3
print(sal.head(2))
# 4
print(sal.info())
# 5
# print(sal['BasePay'].mean())
# 6
# print(sal['OvertimePay'].max())
# 7
print(sal.columns)
joseph = sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']
print(joseph['JobTitle'])
# 8
print(float(joseph['TotalPayBenefits']))
# 9
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()][
          ['EmployeeName', 'BasePay', 'OvertimePay', 'OtherPay']])
# sal.iloc[sal['TotalPayBenefits'].argmax()] argmax or argmin Returns the indices of the maximum or minimum values along an axis
# 10
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()][
          ['EmployeeName', 'BasePay', 'OvertimePay', 'OtherPay']])

# 11
# print(sal.groupby('Year').mean()['BasePay'])
# 12
print(sal['JobTitle'].nunique())
# 13
print(sal['JobTitle'].value_counts().head(5))
# 14

# 15
