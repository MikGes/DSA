# Sort a stack using only one additional stack and O(1) extra space.
# The sorted stack should have the smallest items on the top.
def sortStack(stack):
    tempStack = []
    while stack:
        num = stack.pop()
        while tempStack and tempStack[-1] < num:
            stack.append(tempStack[-1])
            tempStack.pop()
        tempStack.append(num)
    return tempStack

