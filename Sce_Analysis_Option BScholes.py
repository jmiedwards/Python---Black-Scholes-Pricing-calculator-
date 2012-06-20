#-------------------------------------------------------------------------------
# Name:        Scenario Analysis Black Scholes
# Purpose:
#
# Author:      Jamie
#
# Created:     20/06/2012
# Copyright:   (c) Jamie 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def black_scholes (cp, s, k, t, v, rf, div):
        """ Price an option using the Black-Scholes model.
        s: initial stock price
        k: strike price
        t: expiration time
        v: volatility
        rf: risk-free rate
        div: dividend
        cp: +1/-1 for call/put
        """

        d1 = (math.log(s/k)+(rf-div+0.5*math.pow(v,2))*t)/(v*math.sqrt(t))
        d2 = d1 - v*math.sqrt(t)

        optprice = (cp*s*math.exp(-div*t)*stats.norm.cdf(cp*d1)) - (cp*k*math.exp(-rf*t)*stats.norm.cdf(cp*d2))
        return optprice

y = [(+1,71.95, 72, 0.002968, 0.37, 0.0025, 0), (+1,73.95, 72, 0.002968, 0.37, 0.0025, 0), (+1,72.50, 72, 0.002968, 0.37, 0.0025, 0), (+1,74.50, 72, 0.002968, 0.37, 0.0025, 0)]

for i in y:
    map(black_scholes r, (*r, y))
    print i


