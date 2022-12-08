import json
import requests
from requests.auth import HTTPBasicAuth


class Issue:
    def __init__(self, key, created, summary, assignee, **args):
        self.key = key
        self.created = created
        self.summary = summary
        self.assignee = assignee['emailAddress'] if assignee else None
        self.priority = int(args['priority']['id'])
        self.votes = args['votes']['votes']
        self.comment = args.get('comment', '')
        self.status = args['status']['statusCategory']['id']
        self.project = args['project']['name']
        
    def __http_params(self, jira, suffix, data=None):
        return dict(
            url='{}/rest/api/3/issue/{}/{}'.format(
                jira.url, self.key, suffix
            ),
            headers={k: 'application/json' for k in ['Accept', 'Content-Type']},
            auth=HTTPBasicAuth(jira.user, jira.token),
            data=json.dumps(data) if data else None,
        )

    def assign_to_me(self, jira):
        self.assignee = jira.user
        return requests.put(
            **self.__http_params(jira, 'assignee', {'accountId': jira.account_id})
        )

    def start(self, jira):
        self.status = 4
        return requests.post(
            **self.__http_params(jira, 'transitions', {"transition": {"id": 2}})
        )

    def end(self, jira):
        self.status = 3
        return requests.post(
            **self.__http_params(jira, 'transitions', {"transition": {"id": 3}})
        )

    def add_vote(self, jira):
        self.votes += 1
        return requests.post(
            **self.__http_params(jira, 'votes')
        )
