from Bond import Bond
from math import pow

def MacaulayDuration(b: Bond) -> float:
    coupon = b.getCpnRate() * b.getFaceValue()
    compounding = getCompounding(b)
    totalPeriods = compounding * b.getYearsUntilMaturity()

    duration = 0
    price = b.calculateBondPrice()

    for t in range(1, totalPeriods + 1):
        discountFactor = getDiscountFactor(t, compounding, b.getYieldToMaturity())

        if t == totalPeriods:
            pvOfCashFlow = ( (coupon / compounding) + b.getFaceValue()) * discountFactor
            duration += (t * pvOfCashFlow) / price
        else:
            pvOfCashFlow = (coupon / compounding) * discountFactor
            duration += (t * pvOfCashFlow) / price

    return duration

def ModifiedDuration(b: Bond) -> float:
    compunding = getCompounding(b)
    return MacaulayDuration(b) / (1 + (b.getYieldToMaturity() / compunding))


""" Helper Function for the above methods """
def getCompounding(b: Bond) -> int:
    if b.getPaymentsPerYear() == 'A':
        return 1
    elif b.getPaymentsPerYear() == 'S':
        return 2
    else:
        return 4

def getDiscountFactor(t: int, m: int, ytm: float) -> float:
    return 1 / pow( (1 + (ytm / m)), t)










