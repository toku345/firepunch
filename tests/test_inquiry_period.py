from datetime import datetime
from firepunch.inquiry_period import InquiryPeriod


def test_a_whole_day():
    now = datetime.strptime("2019-03-21T12:39:58Z", "%Y-%m-%dT%H:%M:%SZ")

    inquiry_period = InquiryPeriod(until=now)
    since, until = inquiry_period.a_whole_day()

    expected_since = \
        datetime.strptime("2019-03-20T12:39:59Z", "%Y-%m-%dT%H:%M:%SZ")
    assert expected_since == since
    assert until == now
