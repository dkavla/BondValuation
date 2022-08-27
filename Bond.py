
class Bond:

    def __init__(self, m, cr, fv, ytm, p):
        self.__maturity = m
        self.__cpnRate = cr
        self.__faceValue = fv
        self.__yieldToMaturity = ytm
        self.__quotedPrice = p
        self.__calculatedPrice = 0

    """Getter Methods"""
    def get_Maturity(self)->int:
        return self.__maturity

    def get_CouponRate(self)->float:
        return self.__cpnRate

    def get_Face_Val(self)->float:
        return self.__faceValue

    def get_Price_Quoted(self)->float:
        return self.__quotedPrice

    def get_YTM(self)->float:
        return self.__yieldToMaturity

    def get_Calc_Price(self)->float:
        """If price was not calcualted indicate so to user when calling this method"""
        if self.__calculatedPrice == 0:
            return "Price was not calculated! Perform calculation first!"
        else:
            return self.__calculatedPrice



    def __discount_Cpn(self, t)->float:
        """A helper function for discounting individual coupons at time t"""
        cpn = self.__faceValue * self.__cpnRate

        """Special case: if t is the final payment then we discount the cpn plus face value"""
        if t == self._maturity:
            return (cpn + self._faceValue) / pow(1 + self._yieldToMaturity, t)
        return cpn / pow(1 + self._yieldToMaturity, t)

    def __calc_Price(self)->float:
        """The function that performs the actual bond price calculation
        
        Each coupon payment is discounted from time t to present and the results
        are summed up to give the price"""
        price = 0
        for i in range(1, self._maturity + 1):
            price += self.__discount_Cpn(i)
        return price

    def bond_Price(self):
        """Calculates the bond price and assigns it to the _calculatedPrice attribute
        
        The actual calculation is performed by a separate method"""
        self._calculatedPrice = self.__calc_Price()



    def is_Discount(self)->bool:
        """Determines whether the bond price is selling at a discount"""
        if self.__quotedPrice < self.__calc_Price:
            return True
        return False

    def is_Premium(self)->bool:
        """Determines whether the bond price is selling at a premium"""
        if self.__quotedPrice > self.__calc_Price:
            return True
        return False

    def is_Par(self)->bool:
        """Determines whether the bond prcie is selling at par"""
        if self.__quotedPrice == self.__calc_Price:
            return True
        return False



