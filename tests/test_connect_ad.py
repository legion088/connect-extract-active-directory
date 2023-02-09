import pytest
from my_pack.connect_ad import get_username_department_ad
from my_pack.conf import configurations

users = ['petrov_pp']
type_error_args = ['', 10, [], (), {}]


def test_connect_db():
    global users
    result = {'username': ['petrov_pp'], 'department': ['marketing']}
    assert get_username_department_ad(configurations, users) == result


def test_connect_db_empty_list_users():
    list_users = []
    result = {'username': [], 'department': []}
    assert get_username_department_ad(configurations, list_users) == result


@pytest.mark.parametrize('exception, arg1, arg2', ([TypeError, tp, users] for tp in type_error_args))
def test_exceptions(exception, arg1, arg2):
    with pytest.raises(exception):
        get_username_department_ad(arg1, arg2)
