
class Bond:

    def __init__(self, m, cr, fv, ytm=None):
        self.maturity = m
        self.cpnRate = cr
        self.faceValue = fv
        self.yieldToMaturity = ytm

    def setYTM(self, ytm):
        self.yieldToMaturity = ytm

