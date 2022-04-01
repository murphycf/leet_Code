
#Longest substring without repeating Char
#ex Input = "abcabcbb"
#res Output = 3
#abc doesn't have duplicants. And we Cannont have duplicates.
#can brute force it through the list by interating
#better is the 'sliding window algorithum
#we will use a set for a substring to ensure that there are no duplicates in our set. 
#we will move the pointers over to see if there are duplicates
#we remove char from both the window and the set
#this should be O(n) making our solution linear.
def lengthOfSubstring(self, s: str) -> int:
    charSet = set() # make an empty set
    leftpointer = 0 # set leftpointer to zero
    res = 0 #set the result to zero
    for rightpointer in range(len(s)): #the right pointer moves through the length of s
        while s[rightpointer] in charSet: # need a while loop to find the sets right pointer to discover the longest length of a substring
            charSet.remove(s[leftpointer]) #remove thecharacter and update the left pointer when the
            leftpointer += 1 #increment the leftpointer by one
        charSet.add(s[rightpointer]) #add the rightpointer to the set
        res = max(res, rightpointer - leftpointer + 1) #the resulting substring length is the rightpointer minus the left + 1 to correct the index
    return res