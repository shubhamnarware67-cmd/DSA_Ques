"""
Q171: Validate Stack Sequences
================================
Problem: Given pushed and popped sequences, return True if they could
represent the result of a sequence of push/pop on an empty stack.

Example:
    pushed=[1,2,3,4,5], popped=[4,5,3,2,1] -> True
    pushed=[1,2,3,4,5], popped=[4,3,5,1,2] -> False
"""

def validate_stack_sequences(pushed, popped):
    stack = []
    j = 0
    for val in pushed:
        stack.append(val)
        while stack and stack[-1] == popped[j]:
            stack.pop()
            j += 1
    return len(stack) == 0

if __name__ == "__main__":
    print(validate_stack_sequences([1,2,3,4,5],[4,5,3,2,1]))  # True
    print(validate_stack_sequences([1,2,3,4,5],[4,3,5,1,2]))  # False
