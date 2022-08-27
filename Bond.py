
class Bond:

    def __init__(self, m, cr, fv, ytm, p):
        self._maturity = m
        self._cpnRate = cr
        self._faceValue = fv
        self._yieldToMaturity = ytm
        self._quotedPrice = p
        self._calculatedPrice = 0

    """Getter Methods"""
    def get_Maturity(self):
        return self.maturity

    def get_CouponRate(self):
        return self.cpnRate

    def get_Face_Val(self):
        return self.faceValue

    def get_Price_Quoted(self):
        return self.quotedPrice

    def get_YTM(self):
        return self.yieldToMaturity

    def get_Calc_Price(self):
        """If price was not calcualted indicate so to user when calling this method"""
        if self._calculatedPrice == 0:
            return "Price was not calculated! Perform calculation first!"
        else:
            return self._calculatedPrice



    def _discount_Cpn(self, t):
        """A helper function for discounting individual coupons at time t"""
        cpn = self._faceValue * self._cpnRate

        """Special case: if t is the final payment then we discount the cpn plus face value"""
        if t == self._maturity:
            return (cpn + self._faceValue) / pow(1 + self._yieldToMaturity, t)
        return cpn / pow(1 + self._yieldToMaturity, t)

    def _calc_Price(self):
        """The function that performs the actual bond price calculation
        
        Each coupon payment is discounted from time t to present and the results
        are summed up to give the price"""
        price = 0
        for i in range(1, self._maturity + 1):
            price += self._discount_Cpn(i)
        return price

    def bond_Price(self):
        """Calculates the bond price and assigns it to the _calculatedPrice attribute
        
        The actual calculation is performed by a separate method"""
        self._calculatedPrice = self._calc_Price()



    def is_Discount(self):
        """Determines whether the bond price is selling at a discount"""
        if self._quotedPrice < self._calcPrice:
            return True
        return False

    def is_Premium(self):
        """Determines whether the bond price is selling at a premium"""
        if self._quotedPrice > self._calcPrice:
            return True
        return False

    def is_Par(self):
        """Determines whether the bond prcie is selling at par"""
        if self._quotedPrice == self._calcPrice:
            return True
        return False

