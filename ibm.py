st=["ACBD","BDCE","CEDF","DEFG"]
val=[]

def get_char_diff(string):
    # Initialize an empty list to store differences
    differences = []
    
    # Iterate through the string and calculate the difference between consecutive characters
    for i in range(1, len(string)):
        diff = ord(string[i]) - ord(string[i-1])
        differences.append(diff)
    
    return differences

def find_odd_one_out(list_of_lists):
    # Use the first list as a reference for comparison
    reference = list_of_lists[0]
    
    # Iterate over the list of lists and compare each with the reference
    for i, lst in enumerate(list_of_lists):
        if lst != reference:
            return i  # Return the index of the odd list
    
    return -1

for i in st:
    val.append(get_char_diff(i))

i=find_odd_one_out(val)
print(st[i])
print("Hello, code executed successfully")