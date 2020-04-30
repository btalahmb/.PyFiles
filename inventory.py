#inventory.py

stock = {'notebook:':1, 'pen':6, 'programming languages':3, 'bottle':1, 'pencil':12}
inv = {'bag':5,'upskill':1}
returns = ['bag', 'upskill', 'bag', 'bag', 'coin']

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items is ' + str(item_total))


def addToInventory(inventory, addedItems):

    count = {}
    d = {}
#Add new items to established inventory
    for i in range(len(addedItems)):
        for j in range(len(inventory.keys())):
            if addedItems[i] not in inventory.keys():
                newkey = addedItems[i]
        inventory[newkey] = 0

#Count the number of added items and their values 
    for t in addedItems:
        count.setdefault(t, 0)
        count[t] = count[t] + 1
    print(count)                    

#Update the number of items in inventory
    for k,t in count.items():
        for j,v in inventory.items():
            if k == j:
                v = v + t
                d[k] = v
            else:
                pass
    inventory.update(d)
    return inventory

displayInventory(stock)
stock = addToInventory(stock, returns)
displayInventory(stock)