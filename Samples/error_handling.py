
#division by zero is captured by a try except block
#an error will be written the terminal 
#the function will return None
def divide(dividend, divisor):
    try:
        value = dividend / divisor
    except:
        value = None
        print("An error occurred with dividing.", )
    return value


if __name__ == "__main__": 
    value = divide(5, 0)
    print(value)