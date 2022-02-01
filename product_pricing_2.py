from currency_converter import CurrencyConverter
c = CurrencyConverter()

name_of_whiskey = input("What's this bottle called? ")


whiskey_cost = float(input('Enter cost of whiskey: '))
bottle_size = int(input('Enter the bottle size (ml): '))
abv = float(input('Enter the ABV (%): '))
distillery_fees = float(input('Enter any distillery fees: '))
label_fees = float(input('Enter the cost of labels: '))
bottle_cost = float(input('Enter the cost of the bottle & cork: '))
packaging_cost = float(input('Enter the cost of the tube and / or box: '))
bottling_fees = float(input('Enter any bottling fees: '))

excise = 42.57*(abv/100)*(bottle_size/1000)

total_cost = [whiskey_cost, excise, distillery_fees, label_fees, bottle_cost, packaging_cost, bottling_fees]
cogs = round(sum(total_cost), 2)

msrp = float(input('Enter the MSRP in USD: '))


def margin_finder(cogs):
    
    case_price_usd = round(msrp * 6, 2)

    retailer_cost = round(case_price_usd * .7, 2)

    local_shipping_per_case = float(input('Enter the local shipping per case in USD: '))
    local_taxes_per_case = float(input('Enter local taxes per case in USD: '))

    distributor_cost = round((retailer_cost - local_shipping_per_case - local_taxes_per_case) * .65, 2)

    global_shipping_per_case = 10.00
    fet_per_case = 3.05
    customs_per_case = 2.30
    whse_tax_per_case = 6.00

    pre_shipping = round((distributor_cost - global_shipping_per_case - fet_per_case - customs_per_case - whse_tax_per_case), 2)

    case_euros = c.convert(pre_shipping, 'USD', 'EUR')

    price_per_bottle = round(case_euros / 6, 2)

    our_margin = round((price_per_bottle - cogs) / price_per_bottle, 2)*100


    return price_per_bottle, our_margin

price, margin = margin_finder(cogs)

print("********************************")
print('Whiskey: ', name_of_whiskey)
print('MSRP: ', str(round(msrp,2)))
print('Cost of Goods: ', str(round(cogs, 2)))
print('Price Per Bottle: ', str(price))
print('Our Margin: ', str(margin), '%')
print("********************************")