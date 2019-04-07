from datetime import timedelta
from tzlocal import get_localzone


class InquiryPeriod:
    def __init__(self, until, days):
        self.days = days
        self.until = until
        self.since = self.__calcrate_since()

        local_tz = get_localzone()
        self.since_local = local_tz.localize(self.since)
        self.until_local = local_tz.localize(self.until)

    def __calcrate_since(self):
        return (self.until - timedelta(days=self.days)) + timedelta(seconds=1)
