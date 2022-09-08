#shopping store
#discount rate = 15%
#ask the regular prise from the user and then get the discounted prise

def main():
    regularPrise = getRegularPrise()
    salePrise = regularPrise-discount(regularPrise)
    print(f"the sale prise is ${salePrise}")
def getRegularPrise():
    prise = float(input("enter the item's regular prise: "))
    return prise
def discount(prise):
    return prise*0.15
main()