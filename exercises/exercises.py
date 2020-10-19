def ex_001():
    """
    Question: Let's start with easy things first. Return what (a + a + a) will produce?
    """
    a = 2
    a = 4
    a = 6
    return 18
def ex_002():
    """
    Question: What's wrong with the following script? (return the correct answer)
        a = 1
        _a = 2
        _a2 = 3
        2a = 4

    a - You cannot name a variable that starts with _
    b - You cannot name a variable that contains a number
    c - You cannot name a variable that starts with a number
    d - You can only name a variable with letters only
    """
    
    return "c"
def ex_003():
    """
    a = 1
    b = 2
    print(a == b)
    print(b == c)

    Question: Executing the above code will throw an error. Why? (return the correct answer)

    a - You cannot use == in python
    b - c is not defined
    c - a does not equal b
    d - this will not throw an error
    """
    return "b"
def ex_004():
    """
    Question: Fix the last line so that it outputs the sum of 1 and 2. Please do not change the first two lines. Only the last one.
    """
    pass
    a = "1"
    b = 2
    return (int(a) + b)
def ex_005():
    """
    Question: Complete the script so that it returns the second item of the list.
    """
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    return letters[1]
def ex_006():
    """
    Question: Please complete the script so that it returns a list slice containing items d , e , and f .
    """
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    return letters[3:6]
def ex_007():
    """
    Question: List slicing is important in various data manipulation activities. Let's do a few more exercises on that.

    Please complete the script so that it returns the first three items of list letters.
    """
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    return letters[:3]
def ex_008():
    """
    Question: Complete the script so that it returns letter i using negative indexing.
    """
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    return letters[-2]
def ex_009():
    """
    Question: Complete the script so that it returns a list slice containing the last three items of list letters .
    """
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    return letters[-3:]
def ex_010():
    """
    Question: Complete the script so that it returns a list slice containing letters a, c, e, g, and i. 
    """
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    return letters[::2]
def ex_011():
    """
    Return a list from 1-20 using Range.
    """
    return list(range(1, 21))
def ex_012():
    """
    Question: Complete the script so that it returns the expected output. Please use my_range as input data.
    Expected output: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
    """
    my_range = range(1, 21)

    new_list = []
    for x in my_range:
        new_list.append(x * 10)

    return new_list
def ex_013():
    """
    Question: Complete the script so it returns the expected output using my_range  as input data. Please note that the items of the expected list output are all strings.
    Expected output: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
    """
    my_range = range(1, 21)

    new_list = []

    for x in my_range:
        new_list.append(f"{x}")

    return new_list
def ex_014():
    """
    Question: Complete the script so that it removes duplicate items from list a
    """
    a = ["1", 1, "1", 2]
    # Add solution below
    a = list(set(a))
    # Add solution above
    return a
def ex_015():
    """
    Question: Create a dictionary that contains the keys a  and b  and their respective values 1  and 2. Return it.
    """
    new_dict = {"a":1, "b":2}
    return new_dict