def lab2Question1(word):
    # Note - you'll need to change the signature (above) to match the arguments for this lab...
    # Create a function that takes in a string 
    # Return True if that string is a palindrome, False otherwise
    word = ''
    if word == word[::-1]:
        return True
    else:
        return False

    
#print(lab2Question1('madam'))


def lab2Question2(number_val):
    # Create a function that takes in a number
    # Return a list of the fibonacci sequence up to that number
    if number_val < 0:
        return []
    if number_val == 0:
        return [0]
    if number_val == 1:
        return [0,1]
    if number_val == 2:
        return [0,1,1]
      
    result = lab2Question2(number_val -1)
    answer = sum(result[-2:])
    result.append(answer)
    return result
    
    
#print(lab2Question2(-1))  
#print(lab2Question2(0))
#print(lab2Question2(1))
#print(lab2Question2(2))
#print(lab2Question2(3)) 
#print(lab2Question2(4)) 
#print(lab2Question2(5))
#print(lab2Question2(6))


def lab2Question3(str1, str2):
    # Create a function that takes in two strings - str1 and str2
    # Return the number of times str2 appears in str1
    # For example if str1 = "coding is cool" and str2 = "co" then output should be 2.
  str1 = str1.lower()
  str2 = str2.lower()
  count_number_of_times = str1.count(str2)
  return count_number_of_times

#print(lab2Question3('Hello there', 'H'))
#print(lab2Question3('Hello', 'what'))
#print(lab2Question3('hello', 'hello'))
    
    
    


def lab2Question4(list1, list2):
    # Create a function that takes in two equal length list of numbers. 
    # Return a list of the element-wise sum of the two lists - i.e. the first element of the output list is the sum of the first elements of the input lists
    # If the condition of the function is not satisfied, return a blank list
    sum_list = []
    if len(list1) != len(list2):
        return []
    for each_number in range(len(list1)):
        sum = list1[each_number] + list2[each_number]
        sum_list.append(sum)
    return sum_list
    

#print(lab2Question4([0,1],[2,4,8]))
#print(lab2Question4([3,6],[2,7]))
#print(lab2Question4([1,4],[1,4]))
#print(lab2Question4([],[]))

def lab2Question5():
    # Create a function* that asks a user to enter a password that meets the following criteria:
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    # Keep asking the user to enter a password until they enter a valid password.
    # Return the valid password.
    # *Note: This function should call another function, called isValidPassword(password), 
    # that takes in a password and returns True if the password is valid, False otherwise.
    # You will need to make that function, exactly as described above. 
    password = None
    result = False
    print('please enter a correct password')
    password = input()
    while result == False:
        result = isValidPassword(password)
        if result == False:
            print('please enter a correct password')
            password = input()
    return password







def isValidPassword(password):
    # Create a function that takes in a password and returns True if the password is valid, False otherwise
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    password_len = False
    password_upper = False
    password_lower = False
    password_contain_one_number = False
    if len(password) < 8:
        return False
    for each_character in password:
        if each_character.isupper() is True:
            password_upper = True
        if each_character.islower() is True:
            password_lower = True
        if each_character.isdigit() is True:
            password_contain_one_number = True
    return password_upper and password_lower and password_contain_one_number

#print(lab2Question5())

    

