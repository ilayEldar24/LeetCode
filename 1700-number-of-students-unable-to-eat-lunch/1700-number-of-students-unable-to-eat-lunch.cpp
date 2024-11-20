class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
		int map[] = { 0,0 };
		int res = students.size();

		for(int i = 0; i < students.size() ; i++)
		{
			map[students[i]] += 1;
		}

		for (int i = 0; i < students.size(); i++)
		{
			if (map[sandwiches[i]] != 0) {
				res--;
				map[sandwiches[i]] --;
			}
			else {
				return res;
			}
		}

		return res;
    }
};