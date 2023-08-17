import json
import requests
from requests.auth import HTTPBasicAuth


class Issue:
    def __init__(self, key, jira, created, summary, assignee, **args):
        self.key = key
        self.created = created
        self.summary = summary
        self.assignee = assignee['emailAddress'] if assignee else None
        self.priority = int(args['priority']['id'])
        self.votes = args['votes']['votes']
        self.comment = args.get('comment', '')
        self.status = args['status']['statusCategory']['id']
        self.project = args['project']['name']
        self.jira = jira
        
    def __http_params(self, suffix, data=None) -> dict:
        print(f'\tIssue {self.key}:', suffix, data)
        return dict(
            url='{}/rest/api/3/issue/{}/{}'.format(
                self.jira.url, self.key, suffix
            ),
            headers={k: 'application/json' for k in ['Accept', 'Content-Type']},
            auth=HTTPBasicAuth(self.jira.user, self.jira.token),
            data=json.dumps(data) if data else None,
        )

    def assign_to_me(self):
        self.assignee = self.jira.user
        return requests.put(
            **self.__http_params('assignee', {'accountId': self.jira.account_id})
        )

    def start(self):
        self.status = 4
        return requests.post(
            **self.__http_params('transitions', {"transition": {"id": 2}})
        )

    def end(self):
        self.status = 3
        return requests.post(
            **self.__http_params('transitions', {"transition": {"id": 3}})
        )

    def add_vote(self):
        self.votes += 1
        return requests.post(
            **self.__http_params('votes')
        )
