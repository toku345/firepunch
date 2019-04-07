from datetime import datetime
from pytz import timezone

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


def test_since_local(mocker):
    local_tz = timezone('Asia/Tokyo')
    mocker.patch("tzlocal.get_localzone", local_tz)

    now = datetime.strptime("2019-03-21T12:39:58Z", "%Y-%m-%dT%H:%M:%SZ")
    inquiry_period = InquiryPeriod(until=now, days=1)

    expected_since_local = \
        local_tz.localize(
            datetime.strptime("2019-03-20T12:39:59Z", "%Y-%m-%dT%H:%M:%SZ"))

    assert inquiry_period.since_local == expected_since_local


def test_until_local(mocker):
    local_tz = timezone('Asia/Tokyo')
    mocker.patch("tzlocal.get_localzone", local_tz)

    now = datetime.strptime("2019-03-21T12:39:58Z", "%Y-%m-%dT%H:%M:%SZ")
    inquiry_period = InquiryPeriod(until=now, days=1)

    expected_until_local = local_tz.localize(now)

    assert inquiry_period.until_local == expected_until_local
