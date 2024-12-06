def USD(a, cc):
    if cc == 'INR':
        print(f"{a}$ = {a * 84.1}₹")
    elif cc == 'EUR':
        print(f"{a}$ = {a * 0.92}€")
    elif cc == 'GBP':
        print(f"{a}$ = {a * 0.82}£")
    elif cc == 'AUD':
        print(f"{a}$ = {a * 1.57}A$")
    elif cc == 'CAD':
        print(f"{a}$ = {a * 1.34}C$")
    elif cc == 'JPY':
        print(f"{a}$ = {a * 149.2}¥")
    elif cc == 'CHF':
        print(f"{a}$ = {a * 0.91}CHF")
    elif cc == 'CNY':
        print(f"{a}$ = {a * 7.3}元")
    elif cc == 'AED':
        print(f"{a}$ = {a * 3.67}د.إ")
    else:
        print("Invalid currency code.")
def EUR(a, cc):
    if cc == 'INR':
        print(f"{a}€ = {a * 90.97}₹")
    elif cc == 'USD':
        print(f"{a}€ = {a / 0.92}$")
    elif cc == 'GBP':
        print(f"{a}€ = {a * 0.89}£")
    elif cc == 'AUD':
        print(f"{a}€ = {a * 1.70}A$")  
    elif cc == 'CAD':
        print(f"{a}€ = {a * 1.46}C$")  
    elif cc == 'JPY':
        print(f"{a}€ = {a * 162.1}¥")  
    elif cc == 'CHF':
        print(f"{a}€ = {a * 0.97}CHF")  
    elif cc == 'CNY':
        print(f"{a}€ = {a * 7.97}元")   
    elif cc == 'AED':
        print(f"{a}€ = {a * 4.16}د.إ")   
    else:
        print("Invalid currency code.")
def INR(a, cc):
    if cc == 'USD':
        print(f"{a}₹ = {a / 84.1}$")
    elif cc == 'EUR':
        print(f"{a}₹ = {a / 90.97}€")
    elif cc == 'GBP':
        print(f"{a}₹ = {a / 102.1}£")
    elif cc == 'AUD':
        print(f"{a}₹ = {a / 54.2}A$")
    elif cc == 'CAD':
        print(f"{a}₹ = {a / 62.0}C$")
    elif cc == 'JPY':
        print(f"{a}₹ = {a / 0.56}¥")
    elif cc == 'CHF':
        print(f"{a}₹ = {a / 91.0}CHF")
    elif cc == 'CNY':
        print(f"{a}₹ = {a / 11.3}¥")
    elif cc == 'AED':
        print(f"{a}₹ = {a / 22.7}د.إ")
    else:
        print("Invalid currency code.")
def GBP(a, cc):
    if cc == 'INR':
        print(f"{a}£ = {a * 102.1}₹")
    elif cc == 'USD':
        print(f"{a}£ = {a * 1.22}$")
    elif cc == 'EUR':
        print(f"{a}£ = {a * 1.12}€")
    elif cc == 'AUD':
        print(f"{a}£ = {a * 1.79}A$")
    elif cc == 'CAD':
        print(f"{a}£ = {a * 1.63}C$")
    elif cc == 'JPY':
        print(f"{a}£ = {a * 180.5}¥")
    elif cc == 'CHF':
        print(f"{a}£ = {a * 1.14}CHF")
    elif cc == 'CNY':
        print(f"{a}£ = {a * 8.90}元")
    elif cc == 'AED':
        print(f"{a}£ = {a * 4.4}د.إ")
    else:
        print("Invalid currency code.")
def AUD(a, cc):
    if cc == 'INR':
        print(f"{a}A$ = {a * 54.2}₹")
    elif cc == 'USD':
        print(f"{a}A$ = {a / 1.57}$")
    elif cc == 'EUR':
        print(f"{a}A$ = {a / 1.70}€")
    elif cc == 'GBP':
        print(f"{a}A$ = {a * 0.58}£")
    elif cc == 'CAD':
        print(f"{a}A$ = {a * 0.87}C$")
    elif cc == 'JPY':
        print(f"{a}A$ = {a * 88.3}¥")
    elif cc == 'CHF':
        print(f"{a}A$ = {a * 0.63}CHF")
    elif cc == 'CNY':
        print(f"{a}A$ = {a * 4.77}元")
    elif cc == 'AED':
        print(f"{a}A$ = {a * 2.77}د.إ")
    else:
        print("Invalid currency code.")
def CAD(a, cc):
    if cc == 'INR':
        print(f"{a}C$ = {a * 62.0}₹")
    elif cc == 'USD':
        print(f"{a}C$ = {a * 0.75}$")
    elif cc == 'EUR':
        print(f"{a}C$ = {a * 0.68}€")
    elif cc == 'GBP':
        print(f"{a}C$ = {a * 0.59}£")
    elif cc == 'AUD':
        print(f"{a}C$ = {a * 1.07}A$")
    elif cc == 'JPY':
        print(f"{a}C$ = {a * 104.0}¥")
    elif cc == 'CHF':
        print(f"{a}C$ = {a * 0.68}CHF")
    elif cc == 'CNY':
        print(f"{a}C$ = {a * 5.22}¥")
    elif cc == 'AED':
        print(f"{a}C$ = {a * 2.80}د.إ")
    else:
        print("Invalid currency code.")
def JPY(a, cc):
    if cc == 'INR':
        print(f"{a}¥ = {a * 0.56}₹")
    elif cc == 'USD':
        print(f"{a}¥ = {a * 0.0067}$")
    elif cc == 'EUR':
        print(f"{a}¥ = {a * 0.0062}€")
    elif cc == 'GBP':
        print(f"{a}¥ = {a * 0.0054}£")
    elif cc == 'AUD':
        print(f"{a}¥ = {a * 0.0096}A$")
    elif cc == 'CAD':
        print(f"{a}¥ = {a * 0.0091}C$")
    elif cc == 'CHF':
        print(f"{a}¥ = {a * 0.0064}CHF")
    elif cc == 'CNY':
        print(f"{a}¥ = {a * 0.050}元")  
    elif cc == 'AED':
        print(f"{a}¥ = {a * 0.024}د.إ")
    else:
        print("Invalid currency code.")
def CHF(a, cc):
    if cc == 'INR':
        print(f"{a}CHF = {a * 91.0}₹")
    elif cc == 'USD':
        print(f"{a}CHF = {a * 1.09}$")
    elif cc == 'EUR':
        print(f"{a}CHF = {a * 0.93}€")
    elif cc == 'GBP':
        print(f"{a}CHF = {a * 0.82}£")
    elif cc == 'AUD':
        print(f"{a}CHF = {a * 1.53}A$")
    elif cc == 'CAD':
        print(f"{a}CHF = {a * 1.46}C$")
    elif cc == 'JPY':
        print(f"{a}CHF = {a * 117.8}¥")
    elif cc == 'CNY':
        print(f"{a}CHF = {a * 7.26}元")
    elif cc == 'AED':
        print(f"{a}CHF = {a * 3.84}د.إ")
    else:
        print("Invalid currency code.")
def AED(a, cc):
    if cc == 'INR':
        print(f"{a} د.إ = {a * 22.7}₹")
    elif cc == 'USD':
        print(f"{a} د.إ = {a * 0.27}$")
    elif cc == 'EUR':
        print(f"{a} د.إ = {a * 0.24}€")
    elif cc == 'GBP':
        print(f"{a} د.إ = {a * 0.21}£")
    elif cc == 'AUD':
        print(f"{a} د.إ = {a * 0.39}A$")
    elif cc == 'CAD':
        print(f"{a} د.إ = {a * 0.36}C$")
    elif cc == 'JPY':
        print(f"{a} د.إ = {a * 41.2}¥")
    elif cc == 'CHF':
        print(f"{a} د.إ = {a * 0.25}CHF")
    elif cc == 'CNY':
        print(f"{a} د.إ = {a * 1.85}元")
    else:
        print("Invalid currency code.")

currency=['USD','INR','EUR','GBP','AUD','CAD','JPY','CHF','CNY','AED']
print(
    "Available Currencies:\n"
    "1.USD (United States Dollar $)\n"
    "2.INR (Indian Rupee ₹)\n"
    "3.EUR (Euro €)\n"
    "4.GBP (British Pound £)\n"
    "5.AUD (Australian Dollar A$)\n"
    "6.CAD (Canadian Dollar C$)\n"
    "7.JPY (Japanese Yen ¥)\n"
    "8.CHF (Swiss Franc CHF)\n"
    "9.CNY (Chinese Yuan ¥ or 元)\n"
    "10.AED (Emirati Dirham د.إ or AED)"
)
am,bi=input("Enter amount (with currency eg:20 INR):").split()
a=int(am)
b=bi.upper()
if b in currency:
    currency.remove(b)
    for i in range(len(currency)):
        print('*',currency[i])
    cc=input("convert to:").upper()
    if cc not in currency:
        print("invalid currency")
    else:
        if(b=='USD'):
            USD(a,cc)
        elif(b=='EUR'):
            EUR(a,cc)
        elif(b=='INR'):
            INR(a,cc)
        elif(b=='GBP'):
            GBP(a,cc)
        elif(b=='AUD'):
            AUD(a,cc)
        elif(b=='CAD'):
            CAD(a,cc)
        elif(b=='JPY'):
            JPY(a,cc)
        elif(b=='CHF'):
            CHF(a,cc)
        elif(b=='CNY'):
            CNY(a,cc)
        elif(b=='AED'):
            AED(a,cc)
        else:
            print("please enter valid currency")
else:
    print("Given currency is not available! please choose in the given set of currencies")
    

