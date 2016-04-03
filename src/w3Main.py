"""
@author jsl
@since 160401
"""
def sayHello():
    print "I say hello!"

def sayHelloHelp(name):
    """
    sayHello function with comments

    parameters
    ----------
    arg1: str
        name

    Returns
    -------
    none

    Examples
    --------
    sayHelloHelp('jsl')
    """
    print name, "say hello!"

def lab3():
    """
    lab3 means lab for wk3
    do not add arguments for lab functions
    """
    sayHello()
    sayHelloHelp("jsl")

def main():
    lab3()

if __name__=="__main__":
    main()

