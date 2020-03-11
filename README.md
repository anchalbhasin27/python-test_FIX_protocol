FIX Messages Python test

FIX is an open source protocol widely used to trade all asset types in the global financial systems.


EX 1: Simplified FIX 4.2 new order message example: 
8=FIX.4.2|35=D|55=SYMBOL_1|54=1|38=100|40=2|59=0|167=FUT|1=CLIENT_1|44=199.99 

EX 2: Simplified rules: <br />
8=FIX.4.2 (always this value) <br />
35=D (always a new order message ‘D’) <br />
55=SYMBOL_N (Symbol meaning the product name: N is a number) Note that in real life this could be a stock like GOOGLE <br />
54=[1-2] side (buy or sell the given symbol/product) <br />
38=N (quantity of the symbol/product that you want to buy or sell) <br />
40=[1-5] (only order types 1-5 per the FIX 4.2 spec: http://btobits.com/fixopaedia/fixdic42/tag_40_OrdType_.html) <br />
59=[0-6] (all time in force orders per FIX 4.2 spec: https://www.onixs.biz/fix-dictionary/4.2/tagNum_59.html) <br />
167=(FUT|OPT|CS) (Futures, Options and Common stocks) <br />
1=CLIENT_N (random client id) <br />
44=Any price (price at which you will sell or buy the given product) <br />

There are 2 scripts.

1st script "generate_fix_mesgs" takes 2 arguments. 
This is a python 2.7 script which generates fake FIX messages.It takes 2 arguments, 
1st specifies the number of fake messages to generate and the 2nd argument is the name for output file 
which contains the generated message info,which will be later used for parsing data. <br />
format : <python generate_fix_msgs.py int "file_name">


2nd script "read_fix_msgs"
This is a python 2.7 script which reads the generated FIX messages,
by taking 1 argument, the generated file-name from script 1
and produce various statistics on the trading habits of each clients. <br />
format : <python read_fix_msgs.py "file_name">

6 stats have been included : <br />
stat 1: show the count of stock types<br />
stat 2 - occurences of unique symbol<br />
stat 3 - most popular symbol <br />
stat 4 - occurences of unique orders<br />
stat 5 - most popular order-types<br />
stat 6 - average ordered quantity per product<br />

In future many more stats will be included including data visualization.

