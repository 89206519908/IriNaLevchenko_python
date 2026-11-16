class Address:
    index = '000000'
    city = 'name'
    strit = 'name'
    house = '00'
    apartment = '000'

    def __init__(self, index, city, strit, house, apartment):
        self.index = index
        self.city = city
        self.strit = strit
        self.house = house
        self.apartment = apartment

    def __str__(self):
        return (
            f"{self.index}, город{self.city}, "
            f"улица{self.strit}, дом{self.house}, "
            f"квартира{self.apartment}"
        )
