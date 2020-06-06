# --------------
#Code starts here
def palindrome(num):
    palindrome_input = num
    nextPalindrome = False    
    while nextPalindrome == False:
         palindrome_input = int(palindrome_input) + 1 #increments number by 1
         palindrome_input = str(palindrome_input) #converts back to a string so that it can be reversed below
         reverse_palindrome = palindrome_input[::-1] #reversed
         if palindrome_input == reverse_palindrome: #checks if it is a palindrome
             
             nextPalindrome = True #breaks loop
    return int(palindrome_input)
palindrome(13456)       




# --------------
#Code starts here
def a_scramble(str_1,str_2):
    str_1=str_1.lower()
    str_2=str_2.lower()
    count = {str_1[i] : 0 for i in range(len(str_1))} 
      
    for i in range(len(str_1)): 
        count[str_1[i]] += 1
      
    # Now traverse through str2 to check  
    # if every character has enough counts 
    for i in range(len(str_2)): 
        if count[str_2[i]] == 0: 
            return False
        count[str_2[i]] -= 1
    return True
    
a_scramble('labratory','Bat')









# --------------
#Code starts here
def check_fib(num):
    a=0
    b=1
    series=0
    i=0
    while(i<num):
        #print(series)
        a = b
        b = series
        series = a+b
        i=series
    if(i==num):
        return True
    else:
        return False     

check_fib(987)


# --------------
#Code starts here

#Function to compress string
def compress(word):
    word=word.lower()
    mist=[]
    l=0
    while(l<len(word)):
        m=word[l]
        j=0
        while(l<len(word) and word[l]==m):
                 j=j+1
                 l=l+1    

        mist.append(m)
        mist.append(str(j))
    
    return ''.join(mist)

#Code ends here


# --------------
#Code starts here
def k_distinct(string,k):
    string=string.lower()
    list1=list(set(string))

    if len(list1)==k:
        return True
    else:
        return False            

k_distinct('Rhythm',6)


