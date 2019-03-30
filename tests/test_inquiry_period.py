from datetime import datetime
from firepunch.inquiry_period import InquiryPeriod


def test_1_day():
    now = datetime.strptime("2019-03-21T12:39:58Z", "%Y-%m-%dT%H:%M:%SZ")

    inquiry_period = InquiryPeriod(until=now, days=1)

    expected_since = \
        datetime.strptime("2019-03-20T12:39:59Z", "%Y-%m-%dT%H:%M:%SZ")
    assert expected_since == inquiry_period.since
    assert now == inquiry_period.until


def test_2_days():
    now = datetime.strptime("2019-03-21T12:39:58Z", "%Y-%m-%dT%H:%M:%SZ")

    inquiry_period = InquiryPeriod(until=now, days=2)

    expected_since = \
        datetime.strptime("2019-03-19T12:39:59Z", "%Y-%m-%dT%H:%M:%SZ")
    assert expected_since == inquiry_period.since
    assert now == inquiry_period.until
