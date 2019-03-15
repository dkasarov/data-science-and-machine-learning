import pandas as pd

ecom = pd.read_csv('Ecommerce_Purchases')

print(ecom)

print(ecom.head(3))

print('columns: %s; rows: %s' % (len(ecom.columns), len(ecom)))

print(ecom['Purchase Price'].mean())

print('highest: {}; lowest: {}'.format(ecom['Purchase Price'].max(), ecom['Purchase Price'].min()))

print(len(ecom[ecom['Language'] == 'en']))

print(len(ecom[ecom['Job'] == 'Lawyer']))

print('am count: {}; pm count: {}'.format(len(ecom[ecom['AM or PM'] == 'AM']), len(ecom[ecom['AM or PM'] == 'PM'])))

print(ecom['Job'].value_counts().head(5))

print(ecom[ecom['Lot'] == '90 WT']['Purchase Price'])

print(len(ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)]))


# 07/25
def exp(exp_date):
    res = exp_date.split('/')
    if int(res[1]) == 25:
        return True
    else:
        return False


print(len(ecom[ecom['CC Exp Date'].apply(lambda x: exp(x))]))


def get_email_provider(mail):
    res = mail.split('@')
    return res[1]


print(ecom['Email'].apply(lambda x: get_email_provider(x)).value_counts().head(5))
