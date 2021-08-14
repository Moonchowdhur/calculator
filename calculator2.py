# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 09:39:49 2021

@author: Kaushani
"""
#WAP for two input calculator:
#Arithmetic operation
def add(x,y):
    c=x+y
    print(c)

def substract(x,y):
    c=x-y
    print(c)

def multiply(x,y):
    c=x*y
    print(c)
    
def division(x,y):
    c=x/y
    print(c)

def floor_division(x,y):
    c=x//y
    print(c)

def mod(x,y):
    c=x%y
    print(c)

def power(x,y):
    c=x**y
    print(c)

#Relational operation

def relational(x,y):
    if (x==y):
        print(x,"is equal to", y)
        
    elif (x>y) :
        print(x,"is grater than", y)
        
    elif (x<y) :
        print(x,"is less than", y)

    else:
        print(x,"is not equal to", y)   
        
        
#Bitwise operation

def bit_and(x,y):
     c= x&y
     print(c)

def bit_or(x,y):
     c= x|y
     print(c)


def bit_xor(x,y):
     c= x^y
     print(c)


def bit_leftshift(x,y):
     c= x>>y
     print(c)

def bit_rightshift(x,y):
     c= x<<y
     print(c)


#logical operation
 
def logical(x,y):
    c= x>10 and y<50
    d= x>10 or y<50
    e= not( x>10 and y<50)
    if(c==True):
      print(x, '&', y, "lie bewteen in 10 to 50")
    if(d==True):
      print(x, '&', y, "lie bewteen in 10 to 50")  
    if(e==True):
      print(x, '&', y, " don't lie bewteen in 10 to 50")   
      
def invalid():
     print("Wrong choice")  
     
print("\n press a for arithmetic op \n press l for logical op \n press b for bitwise op \n press r for relational op  ")  
choice1=input("Enter your choice: ")   

#For Arithmetic part
if (choice1=='a'):
    x=float(input("Enter a number: ")) 
    y=float(input("Enter another number: ")) 
    op=input("choose your operation: +, -, *, /,fd,p,m: ")
    if(op=='+'):
        add(x,y)
        
    elif(op=='-'):
        substract(x,y)
        
    elif(op=='*'):

        multiply(x,y)
        
        
    elif(op=='/'):
        divison(x,y)
        
    elif(op=='fd'):
        floor_division(x,y)
        
    elif(op=='p'):
        power(x,y) 
        
    elif(op=='m'):
        add(x,y)    
        
    else:
        invalid()
        
     
# For bitwise operation
elif (choice1=='b'):
    x=int(input("Enter a number: ")) 
    y=int(input("Enter another number: ")) 
    op=input("choose your operation: &,|, ^, >>,<<: ")
    if(op=='+'):
        bit_and(x,y)
        
    elif(op=='&'):
        bit_or(x,y)
 
           
    elif(op=='|'):
        bit_or(x,y)
        
        
    elif(op=='^'):
        bit_xor(x,y)
        
    elif(op=='>>'):
        bit_leftshift(x,y)
        
    elif(op=='<<'):
        bit_leftshift(x,y)
        
        
    else:
         invalid()
         
# For relational operation 
elif(choice1=='r'):
     
    x=float(input("Enter a number: ")) 
    y=float(input("Enter another number: ")) 
    relational(x,y)
         
elif (choice1=='l'):
    x=float(input("Enter a number: ")) 
    y=float(input("Enter another number: "))
    logical(x,y)

else:
     invalid()
          

          
          
     
     
      

       
            
        
        
        
        




