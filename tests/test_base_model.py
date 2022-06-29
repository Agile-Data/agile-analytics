from analytics.models import Account


def test_find():
    accounts = Account.find_first({'name': 'root'})
    assert accounts is not None