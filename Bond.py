
class Bond:

    def __init__(self, m, cr, fv, ytm, p):
        self._maturity = m
        self._cpnRate = cr
        self._faceValue = fv
        self._yieldToMaturity = ytm
        self._quotedPrice = p
        self._calculatedPrice = 0

    """Getter Methods
    
    Retrieve the Bond attributes when called on instance"""
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

    

