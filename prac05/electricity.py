TARIFFS = {"11": 0.244618, "31": 0.136928, "42": 0.111111, "69": 0.314159, "13": 0.666666}

print("Electricity Bill Estimator 2.0\n\nTARIFFS:")
for each in TARIFFS:
    print(each, end=",")
tariff = input("\nWhich tariff?: ")
while tariff not in TARIFFS:
    tariff = input("Which tariff?: ")
tariff = TARIFFS[tariff]
dailyUsage = float(input("Enter daily usage of kWh: "))
billingDays = int(input("Enter number of billing days: "))
print("\nEstimated bill: ${:.2f}".format(tariff*dailyUsage*billingDays))