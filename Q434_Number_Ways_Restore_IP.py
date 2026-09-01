"""
Q434: Restore IP Addresses (Backtracking)
============================================
Problem: Given digit string, return all valid IP address combinations.

Example:
    "25525511135" -> ["255.255.11.135","255.255.111.35"]
    "0000"        -> ["0.0.0.0"]
"""

def restore_ip_addresses(s):
    result = []
    def backtrack(start, parts):
        if len(parts) == 4:
            if start == len(s):
                result.append('.'.join(parts))
            return
        for length in range(1, 4):
            if start + length > len(s): break
            segment = s[start:start+length]
            if (len(segment) > 1 and segment[0] == '0') or int(segment) > 255:
                continue
            parts.append(segment)
            backtrack(start+length, parts)
            parts.pop()
    backtrack(0, [])
    return result

if __name__ == "__main__":
    print(restore_ip_addresses("25525511135"))  # ["255.255.11.135","255.255.111.35"]
    print(restore_ip_addresses("0000"))          # ["0.0.0.0"]
