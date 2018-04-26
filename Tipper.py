notaxbill = float(input("Enter amount of bill: "))

tax = 0.06625

taxbill = notaxbill + tax

tip1 = taxbill * .18
tip2 = taxbill * 0.2

totalbill1 = taxbill + tip1
totalbill2 = taxbill + tip2

print("Initial Food Charge: $" + format(notaxbill, ",.2f"), "Total with Tax: $" +\
      format(taxbill, ",.2f" ), "Total with 18% Tip: $" + format(totalbill1, ",.2f"), \
      "Total with 20% Tip: $" + format(totalbill2, ",.2f"),)


