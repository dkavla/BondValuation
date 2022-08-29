from Bond import Bond

def Macaulay_Duration(b: Bond)->float:
    """Returns the Macaulay Duration of the passed in bond object"""

    def weight_of_Cpn(t: int, b_price: float)->float:
        """Calculates the weight of each coupon from period t"""
        if t == b.get_Maturity():
            numer = ( ( (b.get_Coupon_Rate() / 100) * b.get_Face_Val() ) + b.get_Face_Val() ) / pow(1 + (b.get_YTM() / 100), t)
            return numer / b_price

        numer = ((b.get_Coupon_Rate() / 100) * b.get_Face_Val()) / pow(1 + (b.get_YTM() / 100), t)
        return numer / b_price

    total_periods = b.get_Maturity()
    price = b.bond_Price()
    duration = 0
    t = 1
    while t <= total_periods:
        weight_at_t = weight_of_Cpn(t, price)
        duration += (t * weight_at_t)
        t += 1
    return round(duration, 2)

def Modified_Duration(b: Bond)->float:
    """Returns the Modified Duration of the passed in bond object"""
    return round( Macaulay_Duration(b) / (1 + (b.get_YTM() / 100)), 2 )

def Convexity(b: Bond)->float:
    """Measures the convexity of the passed in bond object"""
    pass

def holding_Period_Return(b: Bond)->float:
    """Returns the holding period return of the passed in bond"""
    pass

def yield_To_Call(b: Bond, n: int)->float:
    """Calculates the yield to call of the passed in bond"""
    pass
