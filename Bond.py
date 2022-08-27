
class Bond:

    def __init__(self, m, cr, fv, ytm, p):
        self._maturity = m
        self._cpnRate = cr
        self._faceValue = fv
        self._yieldToMaturity = ytm
        self._quotedPrice = p
        self._calculatedPrice = 0

    """Getter Methods"""
    def getMaturity(self):
        return self.maturity

    def getCouponRate(self):
        return self.cpnRate

    def getFaceVal(self):
        return self.faceValue

    def getPriceQuoted(self):
        return self.quotedPrice

    def getYTM(self):
        return self.yieldToMaturity

    def getCalcPrice(self):
        """If price was not calcualted indicate so to user when calling this method"""
        if self._calculatedPrice == 0:
            return "Price was not calculated! Perform calculation first!"
        else:
            return self._calculatedPrice



    def _discountCpn(self, t):
        """A helper function for discounting individual coupons at time t"""
        cpn = self._faceValue * self._cpnRate

        """Special case: if t is the final payment then we discount the cpn plus face value"""
        if t == self._maturity:
            return (cpn + self._faceValue) / pow(1 + self._yieldToMaturity, t)
        return cpn / pow(1 + self._yieldToMaturity, t)

    def _calcPrice(self):
        """The function that performs the actual bond price calculation
        
        Each coupon payment is discounted from time t to present and the results
        are summed up to give the price"""
        price = 0
        for i in range(1, self._maturity + 1):
            price += self._discountCpn(i)
        return price

    def bondPrice(self):
        """Calculates the bond price and assigns it to the _calculatedPrice attribute
        
        The actual calculation is performed by a separate method"""
        self._calculatedPrice = self._calcPrice()



    def isDiscount(self):
        """Determines whether the bond price is selling at a discount"""
        if self._quotedPrice < self._calcPrice:
            return True
        return False

    def isPremium(self):
        """Determines whether the bond price is selling at a premium"""
        if self._quotedPrice > self._calcPrice:
            return True
        return False

    def isPar(self):
        """Determines whether the bond prcie is selling at par"""
        if self._quotedPrice == self._calcPrice:
            return True
        return False

