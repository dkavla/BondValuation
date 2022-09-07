from Bond import Bond
from quantMetrics import *

"""Prints the available operations and actions for user"""
def menu():
    print("""
    Pick a menu option:
    1.) Enter Bond Info.
    2.) Print Bond Info.
    3.) Get Calculated Bond Price 
    4.) Calculate Macaulay Duration
    5.) Calculate Modified Duration
    6.) Calculate Convexity
    7.) Calculate Holding Period Return 
    8.) Bond Pricing (Discount, Premium, or Par)
    0.) Terminate Program
    """)

if __name__ == "__main__":
    b = None # holds the current instance of bond
    while True:
        menu()
        choice = int(input("Pick a menu option: "))
        if choice == 1:
            print("Enter the necessary bond info")
            maturity = int(input("Maturity of bond: "))
            cpn_Rate = float(input("Coupon Rate (without %): "))
            fv = float(input("Face/Par Value: "))
            ytm = float(input("Yield to Maturity (without %): "))
            quoted_price = float(input("Current Quoted Price (as %/ of FV): "))
            b = Bond(maturity, cpn_Rate, fv, ytm, quoted_price)
        elif choice == 2:
            print(b)
        elif choice == 3:
            if b == None:
                print("Must provide bond info first. Complete menu option 1.")
            else:
                print(f"${b.bond_Price()}")
        elif choice == 4:
            if b == None:
                print("Must provide bond info first. Complete menu option 1.")
            else:
                print(f"Macaulay Duration: {Macaulay_Duration(b)}")
        elif choice == 5:
            if b == None:
                print("Must provide bond info first. Complete menu option 1.")
            else:
                print(f"Modified Duration: {Modified_Duration(b)}")
        elif choice == 6:
            if b == None:
                print("Must provide bond info first. Complete menu option 1.")
            else:
                print(f"Convexity of bond: {Convexity(b)}")
        elif choice == 7:
            if b == None:
                print("Must provide bond info first. Complete menu option 1.")
            else:
                current_price = float(input("enter the current price of the bond in dollars: "))
                print(f"HPR: {holding_Period_Return(b, current_price)}%")
        elif choice == 8:
            if b == None:
                print("Must provide bond info first. Complete menu option 1.")
            else:
                if b.is_Discount():
                    print("Bond is selling at a discount based on quoted and calculated price.")
                elif b.is_Premium():
                    print("Bond is selling at a premium based on quoted and calculated price.")
                else:
                    print("Bond is selling at par based on quoted and calculated price.")
        elif choice == 0:
            print("Terminating program....")
            break

