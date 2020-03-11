"""
This is a python 2.7 script which reads the generated FIX messages,
by taking 1 argument, the generated file-name from script 1
and produce various statistics on the trading habits of each clients.

"""
# import necessary modules
import sys
import numpy as np


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print 'python file.py fix_filename'
        exit(1)

    fix_filename = sys.argv[1]

    #intitating stat dictionary to collect data values from each line of generated fake message.
    # stat_prod dictionary to keep track of product, later on used for calculating average value.
    stat = dict()
    stat_prod = dict()

    # loop to read line by line of generated fake message
    for line in open(fix_filename, 'r'):
        #print line
        line = line.strip().split('|')[2:]
        for item in line:
            item = item.split('=')
            if item[0] in stat.keys():
                stat[item[0]].append(item[1])
            else:
                stat[item[0]] = [item[1]]
            if item[0]=='55':
                if item[1] in stat_prod.keys():
                    stat_prod[item[1]].append(int(line[2].split('=')[1]))
                else:
                    stat_prod[item[1]] = [int(line[2].split('=')[1])]

    # stat 1: show the count of stock types
    print 'Count of stock types'
    print '# FUT:', stat['167'].count('FUT')
    print '# OPT:', stat['167'].count('OPT')
    print '# CS:', stat['167'].count('CS')

    
    #stat 2 - occurences of unique symbol
    print '\n', 'Occurences of unique symbols'
    uniq_symbol = set(stat['55'])
    max_symbol = ''
    max_symbol_count = -np.inf
    for item in uniq_symbol:
        count_symbol = stat['55'].count(item)
        print item, ':', count_symbol
        if count_symbol > max_symbol_count:
            max_symbol = item
            max_symbol_count = count_symbol

    #stat 3 - most popular symbol:
    print 'Most popular symbol'

    print 'max_pop_sym', max_symbol, 'count:', max_symbol_count



    #stat 4 - occurences of unique orders
    print '\n','Occurences of unique orders'

    orders ={'1':'Market', '2':'Limit','3':'Stop','4':'Stop limit','5':'Market on close'}
    popular_order = set(stat['40'])
    max_order = ''
    max_order_value = -np.inf
    for order in popular_order:
        count_order = stat['40'].count(order)
        print orders[order], ':', count_order
        if count_order > max_order_value:
            max_order = order
            max_order_value = count_order

    #stat 5 - most popular order-types
    print 'Most popular order:', orders[max_order], ' occurence:', max_order_value, '\n'

    #stat 6 - average ordered quantity per product
    print 'Average ordered quantity per product: '
    for k,v in stat_prod.items():
        print k, sum(v)/float(len(v))
