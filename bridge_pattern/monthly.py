from abs_subscription import Subscription
from dateutil.relativedelta import relativedelta


class Monthly(Subscription):

    @property
    def price_base(self):
        return 50.0

    @property
    def expiration(self):
        return self.enrolled + relativedelta(months=1)