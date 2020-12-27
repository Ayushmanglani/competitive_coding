class Solution(object):
    def minJumps(self, arr):
        minsteps = {}
        equals = collections.defaultdict(list)
        for i, v in enumerate(arr):
            equals[v].append(i)
            
        queue = []
        cur_step = 0
        for step in range(len(arr)):
            queue.append(step)
            next_queue = []
            while queue:
                idx = queue.pop()
                if idx == len(arr) - 1:
                    return cur_step
                if idx not in minsteps:
                    minsteps[idx] = cur_step
                    if idx > 0 and idx-1 not in minsteps:
                        next_queue.append(idx - 1)
                    if idx < len(arr) - 1:
                        next_queue.append(idx + 1)
                    if arr[idx] in equals:
                        next_queue.extend(equals[arr[idx]])
                        del equals[arr[idx]]
            cur_step += 1
            queue = next_queue
        return cur_step