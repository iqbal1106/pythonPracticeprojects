with open("currency", "r") as f:
    lines= f.readlines()


var = {}

for line in lines:
        parsed= line.split("\t")
        var[parsed[0]]=parsed[1]
        #print(var)
print("Enter the amount")
amount=int(input())
print("entr the currency to be converted to")
currency=input()
print(f"amount {amount} is equal to the currency: {amount*float(var[currency])}")

