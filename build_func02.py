def main(a = 7 , b = 5, c = 9, d = 4):
    """Return the value of the expression in README.md file.
    https://github.com/codeschool43/Build_in_function_homework#build_func02 

    Args:
        None
        
    Returns:
        float: the value of the expression
    """
    x = 3 * (a / b  - c / d)
    return x
print (main())