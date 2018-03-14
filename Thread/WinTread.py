from multiprocessing import Process

import os

def run_proc(name):
    print('Run child proces % s (%s)   ' % (name,os.getpid()))

if __name__=='__main__':
    print('')