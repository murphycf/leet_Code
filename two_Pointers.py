
#Two Pointers
#time moves in one direction so the indicies of the list will reflect the lost value minus the highest value
# left point will be the purchase date and right will be the sell date
#if right is less than left thant the left pointer becomes the right point and the right pointer is incremented one value
#current max profit is rightpointer minus the left pointer
#can leave the left pointer and keep incrementing the rightpointer and curr profit and max profit
#Should be in O(n) time and should be the most optimal solution. Only scanning through the array 1 time.
#Memory should be O(1) not using extra memeory
def maxProfit(self, prices: list[int]) -> int:
    l, r = 0 # l = buy and r = sell
    maxP = 0 # maxP doesn't exist at the start so set to 0
    while r < len(prices): # loop through as long as the right pointer is less than the list
        #profitable??
        if prices [l] < prices[r]: # conditional to buy and sell as long as the left pointer is less than the right pointer. keeps going until the right pointer is out of bounds
            profit = prices[r] - prices[l] #profit is equal to right pointer index minus the left pointer index
            maxP = max(maxP, profit) #maxP find the max point and the purchase point
        else:
            l = r #increment the left pointer through the list. Want the left pointer to be at the minimum
        r += 1 #increment the right pointer through the list
    return maxP #return the maxP
   