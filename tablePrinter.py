#tablePrinter.py

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alicia', 'Bert', 'Czech', 'David'],
             ['Dogs', 'chicken', 'moose', 'goose']]

def printTable():

    colWidths = [0] * len(tableData)

#Solve for longest string in each column and store values in a list
    for i in range(len(tableData)):
        for j in range(len(colWidths)):
            curr = len(tableData[j][i])
            nex = len(tableData[j][i+1])
            if(curr < nex):
                temp = curr
                curr = nex
                nex = temp
            else:
                pass
            colWidths[j] = curr

#Find longest string value in list of string values
    for i in range(len(colWidths)): 
        curr1 = colWidths[i]
        nex1 = colWidths[i+1]
        if((curr1 > len(colWidths)) or (nex1 > len(colWidths))):
            break
        if(curr1 < nex1):
            temp1 = curr1
            curr1 = nex1
            nex1 = temp1
        else:
            pass

    newTable = []

#Transpose list of lists
    for i in range(len(tableData[0])):
        row = []
        for item in tableData:
            row.append(item[i])
        newTable.append(row)

#Print list as table 
    print()
    for i in (newTable):
        value = ' '.join(i)
        print(value.rjust(curr1))
    

printTable()