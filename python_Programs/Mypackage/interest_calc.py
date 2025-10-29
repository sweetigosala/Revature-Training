""" Module for interest calculations"""

def simple_interest(prin,ny,roi):
    """
    calculating simple interest
    :param prn:principal amount
    :param ny:no of years
    :param roi:rate of interest
    :return: si , total interest
    """
    si = (prin * ny * roi)/100
    amt=prin + si
    return si,amt


def compound_interest(prin,t,roi):
    """
    calculating compound interest
    :param prin: principal amount
    :param ny: no of years
    :param roi: rate of interest
    :return: compound interest
    """
    amt=prin*(1+(roi/100)**(1*t))
    return amt
