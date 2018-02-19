#Implementation of colorful printing console outputs

def print_red(prt):
    print("\033[91m{}\033[00m".format(prt))


def print_yel(prt):
    print("\033[33m{}\033[00m".format(prt))  # \033m[00m needed for not printing everything in yellow, just formatting part