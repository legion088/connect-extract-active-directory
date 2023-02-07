from ldap3 import Connection
from conf import configurations


def get_username_department_ad(conf: dict, unique_users: list) -> dict:
    with Connection(**conf) as conn:
        dataframe_users = {'username': [], 'department': []}

        for username in unique_users:
            conn.search(
                search_base='dc=example,dc=domain',
                search_filter=f'(sAMAccountName={username})',
                attributes=['sAMAccountName', 'department']
            )

            for user in conn.entries:
                dataframe_users.get('username').append(user.sAMAccountName.value)
                dataframe_users.get('department').append(user.department.value)

    return dataframe_users


if __name__ == '__main__':
    list_unique_usres = ['petrov_pp']
    dt = get_username_department_ad(configurations, list_unique_usres)

