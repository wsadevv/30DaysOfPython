import datetime


def formatter(toInsert):
    finalText = "Nome do contribuinte: {toCome}".format(toCome=toInsert)
    return finalText


def percentParser(toInsert):
    finalText = "Nome do contribuinte: %s" % (toInsert)
    return finalText


def purchases(consumers, items):
    if(len(consumers) == len(items)):
        i = 0
        for consumer in consumers:
            new_msg = default_message.format(consumer=consumer, item=items[i])
            i += 1
            print(new_msg)
print(formatter('Willian'))
print(percentParser('Josefina'))


consumers = ['Willian', 'Karina', 'Manoela', 'Joana']
items = ['PS4', 'Zenfone 3', 'Cirilo', 'Belfort Action Figure']

default_message = "Thank you {consumer}, for your purchase of {item}"

purchases(consumers, items)
