daily_sales = [12,5,6,3,2,8,9,4,2,4,16,9]

total_cups = sum(sale for sale in daily_sales if sale>5)
print(total_cups)