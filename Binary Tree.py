binaryTree = ["A", None, None]

def insertLeft(parent, value):

    parent[1] = [value, None, None]
    return parent[1]

def insertRight(parent, value):

    parent[2] = [value, None, None]
    return parent[2]

def insertAtAnyPosition(tree, value, position):

    if position == []:
        tree[0] = value
    else:
        if position[0] == "L":
            if tree[1] == None:
                tree[1] = [value, None, None]
            else:
                insertAtAnyPosition(tree[1], value, position[1:])
        else:
            if tree[2] == None:
                tree[2] = [value, None, None]
            else:
                insertAtAnyPosition(tree[2], value, position[1:])

level1 = binaryTree

dataB = insertLeft(level1, "B")
dataC = insertRight(level1, "C")

dataD = insertLeft(dataB, "D")
dataE = insertRight(dataB, "E")
dataF = insertRight(dataE, "F")

print(binaryTree)

insertAtAnyPosition(binaryTree, "G", ["L", "R", "R"])

print(binaryTree)