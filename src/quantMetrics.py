from Bond import Bond

def Macaulay_Duration(b: Bond)->float:
    """Returns the Macaulay Duration of the passed in bond object"""

    def weight_of_Cpn(t: int, b_price: float)->float:
        """Calculates the weight of each coupon from period t"""
        if t == b.get_Maturity():
            numer = ( ( b.get_Coupon_Rate() * b.get_Face_Val() ) + b.get_Face_Val() ) / pow(1 + b.get_YTM(), t)
            return numer / b_price

        numer = (b.get_Coupon_Rate() * b.get_Face_Val()) / pow(1 + b.get_YTM(), t)
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
    return round( Macaulay_Duration(b) / (1 + b.get_YTM()), 2 )

def Convexity(b: Bond)->float:
    """Measures the convexity of the passed in bond object"""
    def second_factor():
        
        """Helper function for calculating the second factor"""
        def discount(pmt, y, t):
            """Helper function for discounting coupons"""
            return pmt / pow((1 + y), t)

        cpn = b.get_Coupon_Rate()
        ytm = b.get_YTM()
        total = 0

        for i in range(1, b.get_Maturity() + 1):
            total += discount(cpn, ytm, i) * (pow(i, 2) + i)

        return round(total, 2)

    first_factor = 1 / (b.bond_Price() * pow(1 + b.get_YTM(), 2))
    return round(first_factor * second_factor(), 2)

def holding_Period_Return(b: Bond, current_price)->float:
    """Returns the holding period return of the passed in bond"""
    initial_price = b.bond_Price()
    cpn = b.get_Coupon_Rate() * b.get_Face_Val()
    return round((cpn + (current_price - initial_price)) / initial_price, 2)
