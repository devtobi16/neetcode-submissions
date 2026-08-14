class Solution:
    def encode(self, strs: List[str]) -> str:
        self.encoded_str = "" 
        for char in strs:
            self.encoded_str += char + ";"
        print(self.encoded_str)
        return self.encoded_str


    def decode(self, s: str) -> List[str]:
        result = []
        strList = self.encoded_str.split(";")
        print(strList)
        for char in strList:
            result.append(char)
        result.pop()
        return result
