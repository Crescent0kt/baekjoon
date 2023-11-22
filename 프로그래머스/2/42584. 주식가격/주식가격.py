def solution(prices):
    answer = [0] * len(prices)
    price_arr = []
    
    for i in range(len(prices)):
        while i != 0 and len(price_arr)!= 0:
            price = price_arr[-1]
            if price[0] <= prices[i]:
                break
            else:
                price_arr.pop()
                answer[price[1]] = i-price[1]
        price_arr.append([prices[i],i])
    else:
        while len(price_arr)!=0:
            price = price_arr.pop()
            answer[price[1]] = len(prices)-1-price[1]
    return answer