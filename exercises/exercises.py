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
    new_dict = {"a": 1, "b": 2}
    return new_dict


def ex_016():
    """
    Question: Please complete the script so that it returns the value of key b .
    """
    # Don't change the below lines
    d = {"a": 1, "b": 2}
    # Don't change the above lines

    return d["b"]


def ex_017():
    """
    Question: Calculate and return the sum of the values of keys a  and b .
    """
    # Don't change the below lines
    d = {"a": 1, "b": 2, "c": 3}
    # Don't change the above lines
    return d["a"] + d["b"]


def ex_018():
    """
    Question: Fix this code so that the Surname Smith will be returned
    """
    # Don't change the below lines
    d = {"Name": "John", "Surname": "Smith"}
    # Don't change the above lines
    return d["Surname"]


def ex_019():
    """
    Question: Add a new pair of key (e.g. c ) and value (e.g. 3 ) to the dictionary and return the new dictionary.
    """
    # Don't change the below lines
    d = {"a": 1, "b": 2}
    # Don't change the above lines
    d["c"] = 3
    return d


def ex_020():
    """
    Question: Calculate the sum of all dictionary values anbd return the new value.

    """
    # Don't change the below lines
    d = {"a": 1, "b": 2, "c": 3}
    # Don't change the above lines
    return sum(d.values())


def ex_021():
    """
    Question: Using dictionary comprehension, filter the dictionary by removing all items with a value of greater than 1. Then return the new dictionary
    """
    # Don't change the below lines
    d = {"a": 1, "b": 2, "c": 3}
    # Don't change the above lines
    return {k: v for k, v in d.items() if not v > 1}


def ex_022():
    """
    Question: Create a dictionary of keys a, b, c, where each key has a value of a list from 1 to 10, 11 to 20, 21 to 30 respectively and return it.
    """
    return {
        "a": list(range(1, 11)),
        "b": list(range(11, 21)),
        "c": list(range(21, 31)),
    }


def ex_023():
    """
    Question: Return the third value of key b from the dictionary.
    """
    # Don't change the below lines
    d = dict(a=list(range(1, 11)), b=list(
        range(11, 21)), c=list(range(21, 31)))
    # Don't change the above lines
    return d["b"][2]


def ex_024():
    """
    Question: Please complete the script so that it returns the expected output. (Each line can be on a different line or in one single line)
    Expected output: 
        "b has value [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        c has value [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        a has value [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
    """
    d = dict(a=list(range(1, 11)), b=list(
        range(11, 21)), c=list(range(21, 31)))
    return_string = ""

    # Add code below this line
    for k, v in d.items():
        return_string += (f"{k} has value {v}")
    # Add code above this line

    return return_string


if __name__ == "__main__":
    pass
