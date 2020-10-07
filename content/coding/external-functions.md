Title: Distinguish external functions (especially in Python)
Category: Coding
Date: 2017-05-26
Summary: One should clearly distinguish which functions are external by keeping namespaces/modules or at least by using prefixes when the language does support import of whole modules 


My basic rule is to always use some module-name when calling a function from
an external module. Compare following samples

    from egg.utils import (utilA, utilB, utilX, utilD
                           utilE, utilF, utilG, utilH)

    def utilC(x):
        pass

    resA = utilB()
    resB = utilC(utilH(resA))

Obviously one has to look at the top every time they want to distinguish local
from external function. Not mentioning that the import might get very nasty.

    from egg import utils as egg_utils  # use 'as' in case of name clash

    def utilC(x):
        pass

    resA = egg_utils.utilB()
    resB = utilC(egg_utils.utilH(resA))

Please keep calls to external functions explicit. Always.