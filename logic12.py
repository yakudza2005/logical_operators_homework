def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits of the number are the same".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return a>=10 and a<=99 and a/(a//10)==11
print(main(23))