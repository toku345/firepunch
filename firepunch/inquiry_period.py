from datetime import timedelta


class InquiryPeriod:
    def __init__(self, until):
        self.until = until

    def a_whole_day(self):
        since = (self.until - timedelta(days=1)) + timedelta(seconds=1)
        return (since, self.until)
