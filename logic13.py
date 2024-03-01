def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is even".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return a>=10 and a<=99 and (a//10)%2==0 and (a%10)%2==0
print(main(42))