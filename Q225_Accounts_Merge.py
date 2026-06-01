"""
Q225: Accounts Merge (Union-Find)
===================================
Problem: Given list of accounts [name, email1, email2, ...], merge accounts
sharing a common email. Return merged accounts sorted.

Example:
    [["John","j@j.com","j2@j.com"],["John","j3@j.com","j2@j.com"],["Mary","m@m.com"]]
    -> [["John","j@j.com","j2@j.com","j3@j.com"],["Mary","m@m.com"]]
"""
from collections import defaultdict

def accounts_merge(accounts):
    parent = {}
    def find(x):
        if x not in parent: parent[x] = x
        if parent[x] != x: parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        parent[find(x)] = find(y)

    email_to_name = {}
    for acc in accounts:
        name = acc[0]
        for email in acc[1:]:
            email_to_name[email] = name
            union(email, acc[1])

    groups = defaultdict(list)
    for email in email_to_name:
        groups[find(email)].append(email)

    return [[email_to_name[root]] + sorted(emails) for root, emails in groups.items()]

if __name__ == "__main__":
    accounts = [["John","j@j.com","j2@j.com"],["John","j3@j.com","j2@j.com"],["Mary","m@m.com"]]
    for acc in accounts_merge(accounts):
        print(acc)
