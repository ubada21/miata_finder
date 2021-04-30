
class Car:
    def __init__(self, link):

        self.link = link
        self.car_attrs = str(link.split("<span>"))
        self.car_attributes = []
        for i in self.car_attrs:
            self.car_attributes.append(i.split(':'))
        self.car_attributes = self.car_attributes[1:]
#        self.year = attr['yr']
#        self.transmission = attr['trasnmission']
#        self.odometer = attr['odometer']
#        self.title_status = attr['title status']
