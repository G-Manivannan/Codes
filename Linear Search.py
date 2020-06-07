pos = -1

def search(list, n):
   # i = 0

    #while i< len(list):
     #   if list[i] == n:
      #      return True
       # i = i+1

    #return False

    for i in  range(len(list)):
        if list[i] == n:
            globals()['pos'] = i

            return 1
            i = i+1
    return 0


list = [5,9,6,4,7,3]
n = int(input("Enter the Number"))

if search(list, n):
    print("Found at", pos+1)
else:
    print("Not Found")
