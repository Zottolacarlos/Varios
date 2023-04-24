uniqueorderID = []
order_values = []
total_orders = 0
prom_orders = 0
orders_for_2021 = 0
customer_most_spend = {}
ordercost = 0
customer = 0

csvlist = list(csvreader)

for list_int in csvlist[1:]:
    Order_id = list_int[1]
    if Order_id not in uniqueorderID:
        uniqueorderID.append(list_int[1])

for list_int in csvlist[1:]:
    if list_int[1] in uniqueorderID:
        order_value = float(list_int[3])
        total_orders = total_orders + order_value

        order_values.append(order_value)
        if list_int[2] != '':

            order_date = datetime.strptime((list_int[2]), '%Y-%m-%d %H:%M:%S.%f')
            if order_date.year == 2021:
                if order_date.month == 10:
                    orders_for_2021 += 1
                ordercost = float(list_int[5])

                customer = list_int[0]
                if customer in customer_most_spend:
                    customer_most_spend[customer] = customer_most_spend[customer] + ordercost
                else:
                    customer_most_spend[customer] = ordercost

customer = max(customer_most_spend, key=customer_most_spend.get)

print(f'Q1: There are {len(uniqueorderID)} unique Orders')
print(f'Q2: The Average Number of items per Orders is: {round((total_orders / 16672), 2)}')
print(f'Q3: The Max number of items per Order: {max(order_values)}')
print(f'Q4: The numbers of Orders for October of 2021 were: {orders_for_2021}')
print(f'Q5: The Customer who spent the most amount of money in 2021 was: {customer}')