from vendor import Vendor
from customer import Customer


class VendorAdapter(Vendor, Customer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def address(self):
        return f"{self.number} {self.street}"
