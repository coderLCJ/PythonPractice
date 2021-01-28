import logging
import pdb
logging.basicConfig(level=logging.INFO)

def main(s):
    n = int(s)
    assert n != 0, 'n is zero'
    print(10/n)


# main(0)

# logging
def fun(n):
    # logging.info('s = %d' % int(n))

    pdb.set_trace()
    print(1/n)


fun(0)
