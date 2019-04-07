from datetime import timedelta


class InquiryPeriod:
    def __init__(self, until, days):
        self.days = days
        self.until = until
        self.since = self.__calcrate_since()

    def __calcrate_since(self):
        return (self.until - timedelta(days=self.days)) + timedelta(seconds=1)
