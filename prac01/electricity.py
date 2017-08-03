TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity Bill Estimator\n")
tariff = int(input("Which tariff?(11 or 31): "))
if tariff == 11:
    tariff = TARIFF_11
else:
    tariff = TARIFF_31
dailyUsage = float(input("Enter daily usage of kWh: "))
billingDays = int(input("Enter number of billing days: "))
print("\nEstimated bill: ${:.2f}".format(tariff*dailyUsage*billingDays))