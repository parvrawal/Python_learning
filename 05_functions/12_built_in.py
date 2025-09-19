def chai_flavor(flavor="masala"):
    """Return the flavor of chai.  """
    return flavor

print(chai_flavor.__doc__)
print(chai_flavor.__name__)


help(len)

def generate_bill(chai=0, samsosa=0):
    """
    Calculate the total bill for chai and samosa

    :param chai: Number of chai cups(10 rupees each)
    :param samosa: Number of samsoas (15 rupees each)
    : return: (total amount, thank you message)
    """

    total  = chai * 10 + samsosa * 15
    return total, "Thank you for visiting luffy_thehero.com"