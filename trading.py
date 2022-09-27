def maxProfit(price, n):
	profit = [0]*n
	max_price = price[n-1]
	for i in range(n-2, 0, -1):
		if price[i] > max_price:
			max_price = price[i]
		profit[i] = max(profit[i+1], max_price - price[i])
	min_price = price[0]
	for i in range(1, n):
		if price[i] < min_price:
			min_price = price[i]
		profit[i] = max(profit[i-1], profit[i]+(price[i]-min_price))
	result = profit[n-1]
	return result
input_string = input('Enter elements of a list separated by space ')
print("\n")
price_list = input_string.split()
print('price = ', price_list)
for i in range(len(price_list)):
    price_list[i] = int(price_list[i])
print ("Maximum profit is", maxProfit(price_list, len(price_list)))
