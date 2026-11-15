class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        owner = {}

        def find(email: str) -> None:
            while parent[email] != email:
                parent[email] = parent[parent[email]]
                email = parent[email]
            return email

        def union(email: str, name: str) -> None:
            parent[find(email)] = find(name)    

        for account in accounts:
            name, emails = account[0], account[1:]
            for email in emails:
                parent.setdefault(email, email)
                owner[email] = name
                union(email, emails[0])

        groups = defaultdict(list)

        for email in parent:
            groups[find(email)].append(email) 

        return [[owner[root]] + sorted(emails) for root, emails in groups.items()]

            

