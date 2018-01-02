def IdValidate(x):
    if x<0: 
        raise ValueError("The id cannot be negative:")
    return x+1;
    
ids = [1,2]
message = "The ids are x = {identify} and  auto inceremented are:{xor}. "

for x in ids:
    A = IdValidate(x)
    print(message.format(identify=x, xor=A))