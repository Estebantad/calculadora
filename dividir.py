def div(n1, n2):
    """
    Divide el primer número por el segundo.
    Args:
        n1 (float/int): El dividendo.
        n2 (float/int): El divisor.
    Returns:
        float/int: El cociente de n1 y n2, o un mensaje de error si el divisor es cero.
    """
    if n2 == 0:
        return "Error: No se puede dividir por cero."
    return n1 / n2