'''
    Write a function solution that, given a string S consisting of N letters 'a' and/or 'b' returns Accepted
    when all occurrences of letter 'a' are before all occurrences of letter 'b' and return Not Accepted otherwise.

    Examples

    1. Given S = "aabbb", the function should return Accepted.
    2. Given S = "ba", the function should return Not Accepted.
    3. Given S = "aaa", the function should return Accepted. Note that 'b' does not need to occur in S
    4. Given S = "b", the function should return Accepted. Note that 'a' does not need to occur in S
    5. Given S = "abba", the function should return Not Accepted

'''
      
# Function for state zero Q0 
def startStateQ0(s):  
    if (s == 'a'):  
        state = 1
    elif (s == 'b'):  
        state = 3  
    else:  
        state = -1
    return state  
      
# Function for first state Q1  
def firstStateQ1(s):   
    if (s == 'a'):  
        state = 2
    elif (s == 'b'):  
        state = 4
    else:  
        state = -1
    return state  
      
# Function for second state Q2   
def secondStateQ2(s):  
    if (s == 'b'):  
        state = 3
    elif (s == 'a'):  
        state = 1
    else:  
        state = -1
    return state  
      
# Function for third state Q3  
def thirdStateQ3(s):  
    if (s == 'b'):  
        state = 3
    elif (s == 'a'):  
        state = 4
    else:  
        state = -1
    return state  
      
# Function for fourth state Q4   
def fourthStateQ4(s):
    if(s == 'a'):
        state = 2
    elif(s == 'b'):
        state = 3
    else:
        state = -1
    return state  
      
def isAcceptedString(String):            
     
    l = len(String)  
          
    # dfa tells the number associated  
    # with the present dfa = state  
    state = 0
    for i in range(l):   
        if (state == 0):   
            state = startStateQ0(String[i])   
      
        elif (state == 1):   
            state = firstStateQ1(String[i])   
      
        elif (state == 2) :  
            state = secondStateQ2(String[i])   
      
        elif (state == 3) :  
            state = thirdStateQ3(String[i])   
      
        elif (state == 4) :  
            state = fourthStateQ4(String[i])   
        else:  
            return 0
    if(state == 3 or state == 1) :  
        return 1
    else:  
        return 0
      
# Driver code   
if __name__ == "__main__" :  
    
    String = input("Enter the string: ")
    if (isAcceptedString(String)) :  
        print("ACCEPTED")   
    else:  
        print("NOT ACCEPTED")   
