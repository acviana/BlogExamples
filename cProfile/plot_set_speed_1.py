import numpy as N
import time
import pylab as P

set_list = []
loop_list = []
i_list = [1,10,100,1000,10000,100000,1000000]

# ---------------------------------------------------------------------------- 
# Functions
# ---------------------------------------------------------------------------- 

def set_test(input_list):
    return set(input_list)

# ---------------------------------------------------------------------------- 

def loop_test(input_list):
    output_list = []
    for item in input_list:
        if item not in output_list:
            output_list.append(item)  
    return output_list

# ---------------------------------------------------------------------------- 

def run_tests():
    for i in i_list:
        input_list = N.random.random_integers(0,i,10000)
    
        for test_function, result_list in zip([set_test, loop_test], [set_list, loop_list]):
            t1 = time.time()
            output = map(test_function,[input_list])
            t2 = time.time()
            result_list.append(t2 - t1)
            
            print test_function, result_list, output

    return set_list, loop_list

# ---------------------------------------------------------------------------- 
    
def get_delta(set_list, loop_list):
    output = []
    for set_item, loop_item in zip(set_list, loop_list):
        output.append(loop_item - set_item)
    return output        

# ---------------------------------------------------------------------------- 
    
def plot_results():
    set_list, loop_list = run_tests()
    
    ax1 = P.subplot(211)
    ax1.plot(i_list, set_list, label = 'Set')
    ax1.plot(i_list, set_list, 'bo')
    ax1.plot(i_list, loop_list, label = 'Loop')
    ax1.plot(i_list, loop_list, 'go')
    ax1.legend(loc = 7)
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    ax1.grid(True)
    ax1.set_title('For Loop vs Set for a List of 10,000 Random Non-Negative Integers')
    ax1.set_ylabel('log(Execution Time) [s]')
    
    delta = get_delta(set_list, loop_list)
    
    ax1 = P.subplot(212)
    ax1.plot(i_list, delta, 'r-')
    ax1.plot(i_list, delta, 'ro')
    ax1.set_xscale('log')
    ax1.grid(True)
    ax1.set_xlabel('log(Max Integer Value)')
    ax1.set_ylabel('Delta Execution Time [s]')
    
    
    P.savefig('plot_set_speed.png')

# ---------------------------------------------------------------------------- 
# For command line execution.
# ---------------------------------------------------------------------------- 
    
if __name__ == '__main__':
    plot_results()
