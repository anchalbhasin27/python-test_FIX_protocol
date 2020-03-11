"""
This is a python 2.7 script which generates fake FIX messages.
It takes 2 arguments, 1st specifies the number of fake messages to generate and
the 2nd argument is the name for output file which contains the generated message info,
which will be later used for parsing data.

"""

#importing necessary modules
import random
import sys


if __name__ == '__main__':

    if len(sys.argv) < 3:
        print 'python file.py num_fix_messages_to_generate output_filename'
        exit(1)

    num_fix_messages = int(sys.argv[1])
    output_filename = sys.argv[2]

    #setting up fix_rule dictionary:
    # 54 - 1(buy) or 2(sell) the given symbol/product
    # 40 - Orde Type. 1-Market, 2-Limit, 3-Stop, 4-Stop limit, 5-Market on close
    # 59=[0-6] (all time in force orders per FIX 4.2 spec: https://www.onixs.biz/fix-dictionary/4.2/tagNum_59.html)
    # 167 - FUT-Future, OPT-Options, CS-Common Stocks


    fix_rule = {'54':['1','2'],
                '40':['1','2','3','4','5'],
                '59':['0','1','2','3','4','5','6'],
                '167':['FUT', 'OPT', 'CS'],
                }

    fid = open(output_filename, 'w')

    for _ in range(num_fix_messages):

	# symbol_n is the company listing
        symbol_n = str(random.randint(1,10))

	# select a random value for buy or sell
        c_54 = random.choice(fix_rule['54'])

    # quantity of the symbol/product tp buy or sell
        n_38 = str(random.randint(1,10000))


        c_40 = random.choice(fix_rule['40'])

        c_59 = random.choice(fix_rule['59'])

        c_167 = random.choice(fix_rule['167'])

        #client_n (random client id)
        client_n = str(random.randint(1,100000))

        #Any price (price at which you will sell or buy the given product)
        any_price = str(random.uniform(0, 10000))

        msg = '8=FIX.4.2|35=D|55=SYMBOL_'+symbol_n+'|54='+c_54+'|38='+n_38+'|40='+c_40
        msg += '|59='+c_59+'|167='+c_167+'|1=CLIENT_'+client_n+'|44='+any_price

        #print msg
        fid.write(msg+'\n')


    fid.close()
