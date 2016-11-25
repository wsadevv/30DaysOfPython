import datetime


def formatter(toInsert):
    finalText = "Nome do contribuinte: {toCome}".format(toCome=toInsert)
    return finalText


def percentParser(toInsert):
    finalText = "Nome do contribuinte: %s" % (toInsert)
    return finalText


def purchases(default_message, consumers, items, prices):
    for i in len(consumers):
    	default_message.format(consumer=consumers[i], item=items[i], price=prices[i]
    print(default_message)
    return default_message

print(formatter('Willian'))
print(percentParser('Josefina'))


consumers=['Willian', 'Karina', 'Manoela', 'Joana']
items=['PS4', 'Zenfone 3', 'Cirilo', 'Belfort Action Figure']
prices=[100.99, 200, 999.666, 700]

default_message="Thank you {consumer}, for your purchase of {item} with value of {price}"

purchases(default_message, consumers, items, prices)
