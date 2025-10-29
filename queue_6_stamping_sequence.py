from typing import List

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        stamp_len = len(stamp)
        target_len = len(target)
        target_list = list(target)
        res = []
        visited = [False] * target_len
        total_replaced = 0

        def can_replace(pos):
            for i in range(stamp_len):
                if target_list[pos + i] != '?' and target_list[pos + i] != stamp[i]:
                    return False
            return True

        def do_replace(pos):
            replaced = 0
            for i in range(stamp_len):
                if target_list[pos + i] != '?':
                    target_list[pos + i] = '?'
                    replaced += 1
            return replaced

        while total_replaced < target_len:
            replaced_in_this_round = False
            for i in range(target_len - stamp_len + 1):
                if not visited[i] and can_replace(i):
                    replaced = do_replace(i)
                    if replaced > 0:
                        res.append(i)
                        total_replaced += replaced
                        replaced_in_this_round = True
                    visited[i] = True
            if not replaced_in_this_round:
                return []
        return res[::-1]


if __name__ == "__main__":
    s = Solution()
    print(s.movesToStamp("abc", "ababc")) 
    print(s.movesToStamp("abca", "aabcaca")) 
