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
    9.) List bonds in table
    10.) Add current instance to table
    0.) Terminate Program
    """)



if __name__ == "__main__":
    b = None # holds the current instance of bond
    while True:
        print("Enter the necessary bond info")
        issuer = input("Issuer of Bond: ")
        maturity = int(input("Maturity of bond: "))
        cpn_Rate = float(input("Coupon Rate (as decimal): "))
        fv = float(input("Face/Par Value: "))
        ytm = float(input("Yield to Maturity (as decimal): "))
        quoted_price = float(input("Current Quoted Price: "))
        b = Bond(maturity, cpn_Rate, fv, ytm, quoted_price)
        convexity = Convexity(b)
        modDur = Modified_Duration(b)
        macDur = Macaulay_Duration(b)

        print(f"Issuer: {issuer}")
        print(b)
        print("=============================================")
        print(f"Additional Metrics:\nConvexity: {convexity}\nModified Duration: {modDur}\nMacaualay Duration: {macDur}")
        print("=============================================\n")

        choice = input("Continue operations (y/n)? ").lower()
        if choice == 'n':
            break
    
    print("Terminating program...")

