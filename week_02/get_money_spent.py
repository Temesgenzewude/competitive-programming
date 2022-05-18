'''
A person wants to determine the most expensive computer keyboard and USB drive
that can be purchased with a give budget. Given price lists for keyboards and USB drives
 and a budget, find the cost to buy them. If it is not possible to buy both items, return -1.

 Function Description
Complete the getMoneySpent function in the editor below.
getMoneySpent has the following parameter(s):
int keyboards[n]: the keyboard prices
int drives[m]: the drive prices
int b: the budget

Returns
int: the maximum that can be spent, or -1 if it is not possible to buy both items
'''

def getMoneySpent(keyboards, drives, b):
    # Write your code here.
    total = []
    for k in keyboards:
        for d in drives:
            if k + d <= b:
                total.append(k + d)
    total.sort()
    return total[-1] if len(total) != 0 else -1


def main():
    b = 40
    k = [40, 50, 60]
    d = [5, 8, 12]
    print(getMoneySpent(k, d, b))


main()
