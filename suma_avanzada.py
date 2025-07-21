def suma_n(*nums):
    """
    Suma una cantidad N de números.
    Args:
        *nums (float/int): Una cantidad variable de números.
    Returns:
        float/int: La suma total de los números.
    """
    if not nums:
        return 0 
    
    res = 0
    for n in nums:
        res += n
    return res