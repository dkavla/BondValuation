
# Bond Valuation Program
This program takes information about a bond and calculates the bond's price. It provides the methods for doing so with the addition of methods which return a boolean value when called to determine whether the bond is selling at a discount, premium, or at par value. The latter three methods use the calculated price and the quoted price that is passed in along with the other information when creating a new instance of the Bond class.


## Additional Functions
The functions found in the quantMetrics.py file are intended to be used only with the Bond class and provide calculations for determining the bonds duration, of which there are two: **The Macaulay Duration** and **The Modified Duration**. The respective functions for the these two metrics accept a single parameter which is an instance of the Bond class. Additionally, you have a function to measure the **Convexity**, and even a holding period return function to calculate the percentage change in a bond's price.

## Definitions
Theses are some definitions for terms used when discussing bonds. The definitions are from [Investopedia](https://www.investopedia.com):

- **Yield to Maturity**: the expected return on a bond if held to maturity

- **Coupon**: an amount paid to the holder each period (semiannually most of the time) up to maturity.

- **Par Value/Face Value**: this is the amount paid to the holder at the end of the maturity period.

- **Duration**: a measure of how long it will take for the holder of the bond to be repaid. The result of the calculation is in years. It measures the sensitivity of a bond's price to changes in interest rates.

- **Macaualy Duration**: a type of duration measure that represents the weighted average time until all the bond's coupons are paid.

- **Modified Duration**: this measure of duration is not measured in years and instead measures the expected change in bond's price to a 1% change in interest rates

- **Convexity**: a measure of the curvature of the price-yield relationship of a bond. Its a risk management tool for managing a portfolio's exposure to market risk. It also shows how the duration of a bond changes as the interest rate changes.