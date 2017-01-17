import sys
import random

def minCut(graph):
    while len(graph) > 2:
        #pick an edge at random
        node1 = random.randint(0,len(graph)-1)
        edgeIndex = random.randint(1,len(graph[node]))  #start at 1 rather than 0 cuz 0 has the node number rather than an edge
        edge = graph[node][edgeIndex]
        node2 = graph[findNodeIndex(graph, edge)]

        contract(graph, node1, node2. edgeIndex)

def contract(graph, node1, node2, edgeIndex):
    node1num = node1[0]
    node2num = node2[0]
    #remove the edge we are contracting from node1
    del node1[edgeIndex]
    #remove the edge we are contracting from node2
    edgeIndex = binarySearch(node1num, node2)
    del node2[edgeIndex]
    #put the edges of node2 into node1 in sorted order
    graph[node1][1:] = merge(graph[node1][1:], graph[node2][1:])
    #remove self loops
    node1[1:] = removeNum(node1num, node1[1:])

    #set the neighbors of node2 to point to node1 instead
    for neighbor in graph[node2][1:]:
        neighborIndex = findNodeIndex(graph, neighbor)
        graph[neighborIndex][1:] = replaceNum(node2num, node1num, graph[neighborIndex][1:])


    #delete node2
    del graph[node2]
    return


#replaces all instances of a number with a different number in a soreted list
def replaceNum(num, replacementNum, list):
    index = binarySearch(num, list)
    i = index
    if index > 0:
        while(list[i] == num and i >= 0):
            i -= 1
        i+=1

    while(i <= len(list) - 1 and list[i] == num):
        list[i] = replacementNum
        i+=1

    return list



#removes all instances of a certain number from a sorted list
def removeNum(num, list):
    index = binarySearch(num, list)
    del list[index]
    i = index
    if index > 0:
        while(list[i] == num and i >= 0):
            i -= 1
        i+=1

    while(i <= len(list) - 1 and list[i] == num):
        del list[i]

    return list



def binarySearch(num, list):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = int((high + low) / 2)
        if list[mid] == num:
            return mid
        elif list[mid] > num:
            high = mid - 1
        else:
            low = mid + 1

    print("error: index not found in binary search")
    return


#put two lists together preserving sorted order of both
def merge(list1, list2):
    mergedList = []
    i = 0
    j = 0
    done = False

    while not done:
        if i >= len(list1):
            mergedList = mergedList + list2[j:]
            done = True
        elif j >= len(list2):
            mergedList = mergedList + list1[i:]
            done = True
        elif list1[i] < list2[j]:
            mergedList.append(list1[i])
            i += 1
        else:
            mergedList.append(list2[j])
            j += 1

    return mergedList


#does binary search to find the given node
def findNodeIndex(graph, nodeNum):
    low = 0
    high = len(graph) - 1
    while low <= high:
        mid = int((high + low) / 2)
        if graph[mid][0] == nodeNum:
            return mid
        elif graph[mid][0] > nodeNum:
            high = mid - 1
        else:
            low = mid + 1

    print("error: index not found")
    return




#load data into an array creating a sub-array at each index indicating which nodes the node at that
#index is connected to
f = open(sys.argv[1], 'r')
graph = []
for line in f:
    graph.append(line.split())
    graph[-1] = [int(i) for i in graph[-1]]

print(graph)

#testing random function
#print(random.randint(0,5))

#testing the binarySearch function
print(binarySearch(3, [1,2,2,3,7,8]))

#testing removeNum function
#print(removeNum(5,[3,3,4,5,5,6,6]))

#testing replaceNum function
print(replaceNum(3,10,[3,3,4,5,5,6,6]))

#testing merge function
#print(merge([1,2,2],[2,2,10]))


#TODO: pick an edge at random
#TODO: Contract that edge
#TODO: eliminate self loops
#TODO: do until only 2 nodes remain
