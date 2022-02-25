class Flatmate:
    """
    Class Flatmate represents the person that live in a flat and pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate):
        weight = self.days_in_house / \
            (self.days_in_house + flatmate.days_in_house)
        return bill.amount * weight
