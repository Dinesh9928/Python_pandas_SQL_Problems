class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length, n = matrix[0].length;
        
        for(int i =0; i<m; i++){
            
            if(target<=matrix[i][n-1]){
                int low = 0, high = n-1;
                
                while(low<=high){
                    int mid = (low+high)/2;
                    if(target == matrix[i][mid]) return true;
                    
                    else if (target>matrix[i][mid]){
                        low = mid+1;
                    }
                    else 
                        high = mid-1;
                }
            }
        }
        return false;
    }
}