data = int(input("Enter the number of data to stored :"))
def display(data):
    total=0
    for i in range(data):
        total+=i
    return total
retundata=display(data)
print(f"The sum of numbers form 0 to  {data} is :",retundata)