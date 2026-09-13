"""
Q439: Smallest Sufficient Team (Bitmask DP)
==============================================
Problem: Given required skills and people's skills, find smallest team
covering all required skills.

Example:
    req_skills=["java","nodejs","reactjs"]
    people=[["java"],["nodejs"],["nodejs","reactjs"]]
    -> [0,2]
"""

def smallest_sufficient_team(req_skills, people):
    skill_idx = {s: i for i, s in enumerate(req_skills)}
    n = len(req_skills)
    people_masks = []
    for p in people:
        mask = 0
        for skill in p:
            if skill in skill_idx:
                mask |= 1 << skill_idx[skill]
        people_masks.append(mask)

    dp = {0: []}
    for i, pm in enumerate(people_masks):
        for mask, team in list(dp.items()):
            new_mask = mask | pm
            if new_mask != mask:
                if new_mask not in dp or len(dp[new_mask]) > len(team) + 1:
                    dp[new_mask] = team + [i]

    return dp[(1 << n) - 1]

if __name__ == "__main__":
    req = ["java","nodejs","reactjs"]
    people = [["java"],["nodejs"],["nodejs","reactjs"]]
    print(smallest_sufficient_team(req, people))  # [0,2]
