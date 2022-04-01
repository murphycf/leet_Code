#424
#given the string s and inter k. can replace a char in s k times
#return the most string with the most similar char
#Input s = "ABAB" , k = 2 Output = 4; Explination s = "AAAA" or s = "BBBB"
#Input: s = "AABABB", k = 1 Output = 4; Expliation s="AAAABB", s="AABBBB"
# looking to have the longeest repeating substring
# iterate through the the list of characters to find the which characters to replace k times
# s holds all the vaules
#can create a new set of characters in a set
#left pointer starts at index zero right pointer iterates through the length of s
#Will be O(26 * n) cause replating into uppercase char
#
def longestRepeatingCharacterReplacement(self, s: str, k: int) -> int:
    count = {} #create a hashmap
    res = 0 #result set to 0
    
    leftpointer = 0 #left pointer set ti index 0
    maxf = 0 #maxfreq of characters set to zero as no iteration has begun
    for r in range(len(s)): #for loop choosen because iterating through a set number of items in s n times
        count[s[r]] = 1 + count.get(s[r], 0) #count the number of occurances of each character
        maxf = max(maxf, count[s[r]]) #take length of the window and subtract the count
        while (r - leftpointer + 1) - maxf > k: #
            count[s[leftpointer]] -= 1 #
            leftpointer += 1 #
        res = max(res, r - leftpointer + 1) #res is the length of the longest window
     
    return res