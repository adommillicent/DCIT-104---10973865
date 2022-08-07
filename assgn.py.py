Val=int(input("Enter a number: "))
def prime_num():
    num_of_prime=0
    sum=0
    for a in range(2,Val):
            for i in range (2,a):        
                if a%i==0:
                    break
            else:
                print(a)
                num_of_prime+=1
                sum+=a
    average=sum/num_of_prime
    
    print(f"Prime numbers below {Val} are",num_of_prime)
    
    print(f"The sum of the prime numbers below {Val} is",sum)
    
    print(f"The average of the prime numbers below {Val} is",average)
    
prime_num()
    # I Millicent Adom pledge that I did this assignment by myself
        
    
                
        
                
                
