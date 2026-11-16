from address import Address
from mailing import Mailing


to_address = Address(150057, "Ярославль", "Московский проспект", 163, 359)
from_address = Address(150014, "Ярославль", "проспект Толбухина", 6, 133)
cost = 250
track = 54888


my_mailing1 = Mailing(to_address, from_address, cost, track)

print(my_mailing1)
