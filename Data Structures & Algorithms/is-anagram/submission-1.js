class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if(s.length!==t.length){
            return false;
        }
        let sortedS = s.split('').sort();
        let sortedT = t.split('').sort();
        
        
        for (let count = 0; count<t.length;count++){
            if(sortedT[count]!==sortedS[count]){
                return false;
            }
        }
        return true;
    }
}
