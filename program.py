# Minimizing Loss Problem.

def minimum_loss(prices):

    prices_years = [(prices[i], i + 1) for i in range(len(prices))]
    prices_years.sort()
    min_loss = float('inf')
    result = None

    for i in range(1, len(prices_years)):
        price_b, year_b = prices_years[i]
        price_a, year_a = prices_years[i-1]

        if price_b > price_a and year_b < year_a:
            loss = price_b - price_a
            if loss < min_loss:
                min_loss = loss
                result = (year_b, year_a, min_loss)

    if result:
        return result
    else:
        return "No possible transaction that results in a loss."

price_list=list(map(int, input("Enter the prices for each year separated by space: ").split()))
buy_year, sell_year, loss = minimum_loss(price_list)

print(f"Price List: {price_list}")
print(f"Buy in Year: {buy_year}")
print(f"Sell in Year: {sell_year}")
print(f"Then minimum loss will be: {loss}")