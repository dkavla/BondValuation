
from math import pow

class Bond:

    """Constructor -- Creates instances of Bond class"""
    def __init__(self, fv, cpn, n, ytm, m):
        self.__faveValue = fv
        self.__cpnRate = cpn
        self.__yearsUntilMaturity = n
        self.__yieldToMaturity = ytm
        self.__paymentsPerYear = m

    """Accessor Functions"""
    def getFaceValue(self) -> float:
        return self.__faveValue
    
    def getCpnRate(self) -> float:
        return self.__cpnRate
    
    def getYearsUntilMaturity(self) -> int:
        return self.__yearsUntilMaturity
    
    def getYieldToMaturity(self) -> float:
        return self.__yieldToMaturity
    
    def getPaymentsPerYear(self) -> str:
        return self.__paymentsPerYear
    
    """Modifier Functions"""
    def setFaceValue(self, fv: float):
        self.__faceValue = fv

    def setCpnRate(self, cpn: float):
        self.__cpnRate = cpn

    def setYearsUntilMaturity(self, n: int):
        self.__yearsUntilMaturity = n

    def setYieldToMaturity(self, ytm: float):
        self.__yieldToMaturity = ytm

    def setPaymentsPerYear(self, m: str):
        self.__paymentsPerYear = m

    """
        Calculates the bonds price by discounting the coupon payments
        and sums up the discounted cash flows to get the price of the
        bond.
    """
    def calculateBondPrice(self) -> float:
        coupon = self.__faceValue * self.__cpnRate # calculate the cash flow paid per period
        payments = self.__calculatePaymentsPerYear() # get payments per year
        totalPeriods = payments * self.__maturity # calculate the number of periods

        bondPrice = 0 # represents the price of the bond

        for t in range(1, totalPeriods + 1):
            # calculate the current discount factor for period t
            discountFactor = self.__getDiscountFactor(t, payments)

            if t == totalPeriods:
                pvOfCashFlow = (coupon + self.__faceValue) * discountFactor
                bondPrice += pvOfCashFlow
            else:
                pvOfCashFlow = coupon * discountFactor
                bondPrice += pvOfCashFlow

        return round(bondPrice, 2)

    def __calculatePaymentsPerYear(self) -> int:
        # determine how many payments per year there are
        if self.__paymentsPerYear == 'A':
            return 1 # annual
        elif self.__paymentsPerYear == 'S':
            return 2 # semiannual
        else:
            return 4 # quarterly

    # returns the discount factor for period t with a m 
    def __getDiscountFactor(self, t: int, m: int):
        return 1 / pow((1+ (self.__yieldToMaturity / m)), t)