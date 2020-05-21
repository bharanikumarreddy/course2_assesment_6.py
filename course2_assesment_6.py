#Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5).


def sublist(x):
    sub = []
    x = (num for num in x)  # create a generator
    num = next(x, 5)  
    while num != 5:
        sub.append(num)
        num = next(x, 5)  # iterate
    return sub

x = [1, 3, 4, 5, 1, 2, 3]
sublist(x)

#Write a function called check_nums that takes a list as its parameter, and contains a while loop that only stops once the element of the list is the number 7. What is returned is a list of all of the numbers up until it reaches 7.

def check_nums(x):
    sub = []
    x = (num for num in x)  # create a generator
    num = next(x, 7)  
    while num != 7:
        sub.append(num)
        num = next(x, 7)  # iterate
    return sub

x = [0,2,4,9,2,3,6,8,12,14,7,9,10,8,3]
check_nums(x)

#Write a function, sublist, that takes in a list of strings as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the string “STOP” (it should not contain the string “STOP”).

def sublist(string_list):
    sub = []
    try:
        stop_index = next(i for i in range(len(string_list)) if string_list[i] == "STOP")
        sub = string_list[:stop_index]
    except:
        sub = string_list
    return sub
    
  #Write a function called stop_at_z that iterates through a list of strings. Using a while loop, append each string to a new list until the string that appears is “z”. The function should return the new list.
  
  def stop_at_z (list):
    sub = []

    for x in list:
            if x != "z":
                    sub.append(x)
            else:
                    break;
    return sub
   
  #Below is a for loop that works. Underneath the for loop, rewrite the problem so that it does the same thing, but using a while loop instead of a for loop. Assign the accumulated total in the while loop code to the variable sum2. Once complete, sum2 should equal sum1.
  
  
sum1 = 0
sum2=0
counter=0
lst = [65, 78, 21, 33]

for x in lst:
    sum1 = sum1 + x
while counter < len(lst):
    sum2 = sum2 + lst[counter]
    counter += 1

#Challenge: Write a function called beginning that takes a list as input and contains a while loop that only stops once the element of the list is the string ‘bye’. What is returned is a list that contains up to the first 10 strings, regardless of where the loop stops. (i.e., if it stops on the 32nd element, the first 10 are returned. If “bye” is the 5th element, the first 4 are returned.) If you want to make this even more of a challenge, do this without slicing

def beginning(x):
    n = 0
    lst = []
    while "bye" not in x[n] and n < 10:
        lst.append(x[n])
        n = n + 1
    return lst
