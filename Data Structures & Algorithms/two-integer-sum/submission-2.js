class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
    const hashMap = {};
    for(let i = 0; i<nums.length; i++){
        hashMap[nums[i]] = i;
    }
    
    for(let j = 0; j<nums.length; j++){
    let potKey = target - nums[j];
    if(hashMap[potKey]&&hashMap[potKey]!==j){
        return [j, hashMap[potKey]];
    }
    }
}
}