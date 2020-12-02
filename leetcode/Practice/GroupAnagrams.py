#Group Anagrams

#High Time Complexity
class Solution(object):
    def groupAnagrams(self, strs):
        res = []
        resfreq = []
        for s in strs:
            freqs = [0]*26
            for l in s:
                freqs[ord(l)-97] += 1
            found = -1
            for i in range(len(resfreq)):
                if resfreq[i] == freqs:
                    found = i
                    break
            if found == -1:
                res.append([s])
                resfreq.append(freqs)
            else:
                res[found] += [s]
        return res

class Solution(object):
    def groupAnagrams(self, strs):
        mp = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in mp:
                mp[key].append(s)
            else:
                mp[key] = [s]
        ans = []
        for key in mp:
            ans.append(mp[key])
        return ans