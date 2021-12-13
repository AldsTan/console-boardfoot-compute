import math

quantity = input('Quantity (pcs): ')
size = input('Size (W x H x L): ')

''' convert to lower, then replace 'x' with '*' '''
boardfoot = size.lower().replace("x", "*")

''' Display '''
print('\n' + quantity + ' pcs. - ' + size)

''' Evaluate lumber dimensions then multiply with quantity '''
computed = eval(boardfoot) * float(quantity)

''' Final output is rounded UP to the nearest whole number '''
print('Boardfoot: ' + str(math.ceil(computed/12)))