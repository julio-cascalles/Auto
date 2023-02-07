import requests
from requests.auth import HTTPBasicAuth
from issue import Issue

JIRA_PROPERTIES = ['url', 'user', 'token']


class Jira:
    def __init__(self, **args):
        self.url, self.user, self.token = [
            args[k] for k in JIRA_PROPERTIES
        ]
        self.__account_id = ''
        # -------------------------------
        data = requests.get(
            url='{}/rest/api/3/search'.format(self.url),
            headers={'Accept': 'application/json'},
            params={'jql': '{} {}'.format(
                ' AND '.join(
                    f'{k} = {v}'
                    for k, v in args.items()
                    if v and k not in JIRA_PROPERTIES
                ),
                'ORDER BY priority, created',
            )},
            auth=HTTPBasicAuth(self.user, self.token)
        ).json()
        # -------------------------------
        self.issues = [
            Issue(x['key'], self, **x['fields']) 
            for x in data.get('issues', [])
        ]

    @property        
    def account_id(self):
        if not self.__account_id:
            self.__account_id = requests.get(
                url='{}/rest/api/3/myself'.format(self.url),
                headers={'Accept': 'application/json'},
                auth=HTTPBasicAuth(self.user, self.token)
            ).json()['accountId']
        return self.__account_id
