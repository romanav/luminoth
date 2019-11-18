import pytest
import luminoth


# utilizing  dataset: e1c2565b51e9 |   Faster R-CNN w/COCO |    accurate | remote | NOT_DOWNLOADED |





@pytest.fixture
def date_provider():
    import smtplib

    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)


def test_ehlo(smtp_connection):



    response, msg = smtp_connection.ehlo()
    assert response == 250
