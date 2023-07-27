# Fixed Variables
old = [
        [1.6110, 0, 250],       # 0 - 250Kwh 1 
        [3.3237, 251, 500],     # 251 - 500Kwh 2
        [3.5737, 501, 750],     # 501 - 750Kwh 3
        [3.8737, 751, 1000],    # 751 - 1000Kwh 4
        [4.6237, 1001],         # 1001+ 5
    ]

new = [
        [1.9332, 0, 250],       # 0 - 250Kwh 1 
        [3.9884, 251, 500],     # 251 - 500Kwh 2
        [4.2884, 501, 750],     # 501 - 750Kwh 3
        [4.6484, 751, 1000],    # 751 - 1000Kwh 4
        [5.5484, 1001],         # 1001+ 5
    ]    

# Get user input
usage = float(input("Enter the amount of kWh: "))

def calculate_electric(kwa,tarif):
    total_output = 0
    r = 4
    while r >= 0:
        if kwa > tarif[r][1]:
            temp = kwa - tarif[r][1]
            kwa -= temp
            total_output += temp * tarif[r][0]
        r -= 1 
    return total_output

# Print red colored output
print("%d Kws will cost you \033[1;31m %d ₺ in OLD Tariff \033[0m." % (usage, calculate_electric(usage,old)))

# Print green colored output
print("%d Kws will cost you \033[1;32m %d ₺ in NEW Tariff \033[0m." % (usage, calculate_electric(usage,new)))