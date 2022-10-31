# https://coderbyte.com/algorithm/stock-maximum-profit

# https://pythontutor.com/render.html#code=def%20StockPicker%28arr%29%3A%0A%0A%20%20max_profit%20%3D%20-1%20%23%20set%20this%20to%20negative%201%20assuming%20no%20profit%20%0A%20%20buy_price%20%3D%200%20%20%20%23%20set%20the%20value%20to%200%20to%20assign%20value%20later%20%0A%20%20sell_price%20%3D%200%20%20%23%20set%20the%20value%20to%200%20to%20assign%20value%20later%20%0A%0A%20%20%23%20true%20until%20a%20cheap%20stock%20price%20is%20found%0A%20%20is_change_buy_index%20%3D%20True%0A%0A%20%20%23%20loop%20through%20list%20of%20stock%20prices%20with%20a%20counter%0A%20%20counter%20%3D%200%20%0A%20%20%23%20only%20go%20through%200%20through%201%20less%20than%20total%20length%20for%20index%0A%20%20for%20idx%20in%20range%28len%28arr%29%20-%201%29%3A%0A%20%20%20%20%20%20%23%20if%20the%20current%20position%20is%20less%20than%20the%20previous%20%0A%20%20%20%20%20%20if%20arr%5Bidx%5D%20%3C%20arr%5Bidx%20-%201%5D%3A%0A%20%20%20%20%20%20%20%20print%28f%22We%20are%20at%20stock%20price%20%7Barr%5Bidx%5D%7D%20and%20seeing%20if%20less%20than%20yesterdays%20price%20of%20%7Barr%5Bidx%20-%201%5D%7D%22%29%0A%20%20%20%20%20%20%23%20increment%20the%20counter%20if%20current%20price%20is%20less%20than%20previous%20%0A%20%20%20%20%20%20%20%20counter%20%2B%3D%201%0A%20%20%20%20%20%20%23%20selling%20price%20is%20the%20next%20element%20in%20list%20%0A%20%20%20%20%20%20%20%20sell_price%20%3D%20arr%5Bidx%2B1%5D%3B%0A%0A%20%20%20%20%23%20if%20we%20have%20not%20found%20a%20suitable%20cheap%20buying%20price%20yet%0A%20%20%20%20%23%20we%20set%20the%20buying%20price%20equal%20to%20the%20current%20element%20in%20array%0A%20%20%20%20%20%20%20%20if%20is_change_buy_index%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20buy_price%20%3D%20arr%5Bidx%5D%0A%0A%20%20%20%20%23%20if%20the%20selling%20price%20is%20less%20than%20the%20buying%20price%0A%20%20%20%20%23%20we%20know%20we%20cannot%20make%20a%20profit%20so%20we%20continue%20to%20the%0A%20%20%20%20%23%20continue%20to%20the%20next%20element%20in%20the%20list%20%0A%20%20%20%20%23%20which%20will%20be%20the%20new%20buying%20price%0A%20%20%20%20%20%20%20%20if%20sell_price%20%3C%20buy_price%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20is_change_buy_index%20%3D%20True%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20continue%0A%20%20%20%20%23%20if%20the%20temp%20profit%20is%20greater%20than%20the%20sell%20minus%20buy%20price%20%0A%20%20%20%20%23%20we%20check%20to%20see%20if%20these%20two%20indices%20give%20us%20a%20better%0A%20%20%20%20%23%20profit%20then%20what%20we%20currently%20have%0A%20%20%20%20%23%20and%20we%20set%20max_profit%20to%20be%20the%20temp%20profit%20as%20it%20is%20larger%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20temp_profit%20%3D%20sell_price%20-%20buy_price%0A%20%20%20%20%20%20%20%20if%20temp_profit%20%3E%20max_profit%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20max_profit%20%3D%20temp_profit%0A%20%20%20%20%20%20%20%20is_change_buy_index%20%3D%20False%0A%0A%20%20return%20max_profit%0A%0Aprint%28StockPicker%28%5B10,12,4,5,9%5D%29%29%3B%0Aprint%28StockPicker%28%5B44,%2030,%2024,%2032,%2035,%2030,%2040,%2038,%2015%5D%29%29%3B&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false


def stock_picker(arr):
    """
        Take a list of stocks
        You will be given a list of stock prices for a given day
        Your goal is to return the maximum profit that could have been made by
            buying a stock at the given price
            and then selling the stock later on.

        Return an integer of how much money was made or -1 for no profit

    :param arr: list
    :return: int

    For example if the input is: [45, 24, 35, 31, 40, 38, 11]
    then your program should return 16 because if you bought the stock at $24 and sold it at $40,
    a profit of $16 was made.
    and this is the largest profit that could be made.
    If no profit could have been made, return -1.

    >>> stock_picker([44, 30, 24, 32, 35, 30, 40, 38, 15])
    16
    """
    max_profit = -1  # set this to negative 1 assuming no profit
    buy_price = 0  # set the value to 0 to assign value later
    sell_price = 0  # set the value to 0 to assign value later

    # true until a cheap stock price is found
    is_change_buy_index = True

    # loop through list of stock prices with a counter
    counter = 0
    # only go through 0 through 1 less than total length for index
    for idx in range(len(arr) - 1):
        # if the current position is less than the previous
        if arr[idx] < arr[idx - 1]:
            # Debugging
            # print(f"We are at stock price {arr[idx]}
            # and seeing if less than yesterdays price of {arr[idx - 1]}")
            # increment the counter if current price is less than previous
            counter += 1
            # selling price is the next element in list
            sell_price = arr[idx + 1]

            # if we have not found a suitable cheap buying price yet
            # if the change buy index is True
            # we set the buying price equal to the current element in array
            if is_change_buy_index:
                buy_price = arr[idx]

            # if the selling price is less than the buying price
            # we know we cannot make a profit so we
            # continue to the next element in the list
            # which will be the next day buying price
            if sell_price < buy_price:
                is_change_buy_index = True
                continue
            # Else the temp profit is greater than the sell minus buy price
            # we check to see if these two values give us a better
            # max profit then what we currently have
            # and we set max_profit to be the temp profit as it is larger
            # otherwise the change_buy_index is False - sell price is not larger than buy price
            else:
                temp_profit = sell_price - buy_price
            if temp_profit > max_profit:
                max_profit = temp_profit
            is_change_buy_index = False

    return max_profit
    # return (f"We made a profit of {max_profit} on our stocks today")


print(stock_picker([44, 30, 24, 32, 35, 30, 40, 38, 15]))
print(stock_picker([10, 12, 4, 5, 9]))


# import doctest
# doctest.run_docstring_examples(stock_picker("str"), globals(), verbose=True, name="stock_picker")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
