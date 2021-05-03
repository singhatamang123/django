product_name1, product_price1 = "Book", 1500
product_name2, product_price2 = "shoes", 2500
product_name3, product_price3 = "Jacket", 1500
product_name4, product_price4 = "Football", 5200


company_name = "My bazar"
company_address = "Jorpati"
company_contact = "9841026558"

message = "Thank u. Have a good day"
print("*"*50)

print('\t\t{}'.format(company_name.title()))
print('\t\t{}'.format(company_address.title()))
print('\t\t{}'.format(company_contact.title()))
print('='*50)


print('\t{}\t\t\t${}'.format(product_name1.title(), product_price1))
print('\t{}\t\t\t${}'.format(product_name2.title(), product_price2))
print('\t{}\t\t\t${}'.format(product_name3.title(), product_price3))
print('='*50)

print('\t\t\t\t Total')
Total = product_price1 + product_price2 + product_price3
print('\t\t\t\t$', format(Total))

print('\t', message)
print('*'*50)

