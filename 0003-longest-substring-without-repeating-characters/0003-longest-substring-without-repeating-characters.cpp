class Solution {
public:
	int lengthOfLongestSubstring(string s) {
		unordered_set<char> hset;
		if (s.empty())return 0;
		int L = 0, R = 1;
		int curLen = 1, longest = 1;
		hset.insert(s[0]);


		for (R; R < s.size(); R++) {
			if (hset.find(s[R]) == hset.end()) {
				hset.insert(s[R]);
				curLen = (R - L + 1);
				if (curLen > longest) longest = curLen;
			}
			else {
				while (hset.find(s[R]) != hset.end()) {
					hset.erase(s[L]);
					L++;
				}
				hset.insert(s[R]);
				curLen = (R - L + 1);
			}
		}
		return longest;
	}
};