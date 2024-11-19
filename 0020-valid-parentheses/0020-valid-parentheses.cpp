class Solution {
public:
    bool isLeft(char c)
    {
        if (c == '(' || c == '{' || c == '[') return true;
        return false;
    }
    
    bool isMatch(char right, char left) {
        if((left == '(' && right == ')') || (left == '{' && right == '}') || (left == '[' && right == ']')) return true;
        return false;
    }
    
    bool isValid(string s) {
        stack<char> stack;
        int size = s.length();
        char cur,popped;
        for (int i = 0; i < size; i++)
        {
            cur = s[i];
            if (isLeft(cur)) stack.push(cur);
            else {
                if (stack.empty()) {
                    return false;
                }
                popped = stack.top();
                stack.pop();
                if (!isMatch(cur, popped)) return false;
            }
        }
        if (stack.empty()) return true;
        return false;



    }
};