while True:
    
 choice=input("Select a opr , + ,  - , * , / :-")
     
 num1=int(input("Enter num first:- "))
 num2=int(input("enter num second:- "))

 if choice== "+":
    print(num1+num2)
  
 elif choice== "-":
    print(num1-num2)
  
 elif choice== "*":
  print(num1*num2)
  
 elif choice=="/":
  print(num1/num2)
   
 else:
  print("Inviled opr")