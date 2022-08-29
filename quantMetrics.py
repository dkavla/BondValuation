from Bond import Bond

def Macaulay_Duration(b: Bond)->float:
    """Returns the Macaulay Duration of the passed in bond object"""

    def weight_of_Cpn(t: int)->float:
        """Calculates the weight of each coupon from period t"""
        numer = b.get_Coupon_Rate() / pow(1 + b.get_YTM(), t)
        denom = b.get_Price_Quoted()
        return numer / denom

    total_periods = b.get_Maturity()
    duration = 0
    for t in range(1, total_periods + 1):
        weight_at_t = weight_of_Cpn(t)
        duration += (t * weight_at_t)
    return round(duration, 2)

def Modified_Duration(b: Bond)->float:
    """Returns the Modified Duration of the passed in bond object"""
    pass

def Convexity(b: Bond)->float:
    """Measures the convexity of the passed in bond object"""
    pass

def holding_Period_Return(b: Bond)->float:
    """Returns the holding period return of the passed in bond"""
    pass

def yield_To_Call(b: Bond, n: int):
    """Calculates the yield to call of the passed in bond"""
    pass

