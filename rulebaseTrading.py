import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv("gemini_BTCUSD_1hr.csv")
#data = pd.read_csv("Coinbase_BTCUSD_dailydata.csv")

#converting into list
price = data['Close'].tolist()
date = data['Date'].tolist()
price.reverse()
date.reverse()

price = price[-11000:]

wallet = 0
bucket = 100
threshold = 5
maxValue = bucket
marketPrice = bucket
hiddenFloat = bucket
total = wallet + bucket
listBucket = [bucket]
listTotal = [bucket]
listMax = [maxValue]
listMarket = [bucket]


for i in range(1, len(price)):

    percentChange = (price[i] - price[i-1]) / price[i-1] * 100
    marketPrice += marketPrice * percentChange / 100
    listMarket.append(marketPrice)



    if wallet == 0:     # If wallet is empty

        if percentChange < -threshold:      # If wallet is empty and percentage change is less than the minus threshold
            bucket += bucket * percentChange / 100
            maxValue = bucket
            wallet = bucket
            bucket = 0
            hiddenFloat = wallet
            total = wallet + bucket
            print(i,'====','1')

        elif percentChange > 0:     # If wallet is empty percentage change is greater than the zero
            bucket += bucket * percentChange / 100
            maxValue = max(maxValue, bucket)
            total = bucket
            print(i, '====', '2')

        else:   # If wallet is empty percentage is greater than minimum threshhold but less than 0
            bucket += bucket * percentChange / 100
            percentMax = (bucket - maxValue) / maxValue * 100

            if percentMax >= -threshold:
                maxValue = max(maxValue, bucket)
                total = bucket
                print(i, '====', '3')

            else:
                maxValue = bucket
                wallet = bucket
                bucket = 0
                hiddenFloat = wallet
                total = wallet + bucket
                print(i, '====', '4')



    else:
        hiddenFloat += hiddenFloat * percentChange / 100
        if percentChange <= 0:
            maxValue += maxValue * percentChange / 100
            total = wallet
            print(i, '====', '5')

        else:
            percentMax = (hiddenFloat - maxValue) / maxValue * 100
            print(percentMax)
            if percentMax >= threshold:
               bucket = wallet
               wallet = 0
               total = bucket
               maxValue = bucket
               print(i, '====', '6')

            else:
                total = wallet
                print(i, '====', '7')



    listBucket.append(bucket)
    listTotal.append(total)
    print(maxValue)












# create a new figure for the accuracies
N = np.arange(len(listBucket))
intial_investment = [100] * len(price)

plt.plot(N, listMarket, color='blue', label="Market")
plt.plot(N, listTotal, color='red', label="Your wealth")
plt.plot(N, intial_investment, color='green', label="Initial investment")
plt.title("Bit Coin rule base performance")
plt.xlabel("Time")
plt.ylabel("$$$")
plt.legend(loc="upper left")

plt.show()


