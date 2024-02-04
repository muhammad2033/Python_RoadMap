import argparse

if __name__=="__name__":
    parser = argparse.Argumentparser()
    parser .add_argument("number1",help = "first number")
    parser .add_argument("number2", help = "second number")

    parser .add_argument("operation", help = "operation")
    
    args = parser.parse_args()
    
    print(args.number1)
    print(args.number2)
    print(args.operation)
    
    n1 = int (args.number1)
    n2 = int (args.number2)
    
    result = None
    if args.operation == 'add':
        result  = n1+n2
    
    elif args.operation == 'sub':
            result  = n1-n2
            
    elif args.operation == 'multi':
            result  = n1*n2
     
    print(result)        
     