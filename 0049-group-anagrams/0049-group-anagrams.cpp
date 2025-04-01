class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> ans;
        vector<string> res;
        int n = strs.size();
        int end=0;
        for(int i=0; i<n; i+=end)
        {
            string s = strs[i];
            reverse(s.begin(), s.end());
            
            res.push_back(strs[i]);
            for(int j=i+1; j<n-1; j++)
            {
                if(s==strs[j])
                {
                    res.push_back(strs[j]);
                    end = j;
                }
            }
             ans.push_back(res);   
        }
        return ans;
    }
};