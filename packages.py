#package: container for multiple modules
#how to import from a package

#bad:
# import ecommerce.shipping
# ecommerce.shipping.calc_shipping()


#good:
from ecommerce.shipping import calc_shipping
calc_shipping()