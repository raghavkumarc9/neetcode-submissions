class Solution:

    

    def isValid(self, s: str) -> bool:
        a_stack = []
        dict_a = {
            ']': '[',
            '}': '{',
            ')': '('
        }

        for i in s:
            if len(a_stack) == 0:
                a_stack.append(i)
            elif i in ['}', ']', ')'] and len(a_stack) == 0:
                return False
            elif i in ['}', ']', ')']:
                a_stack.append(i)
                print(a_stack)
                j = dict_a[i]
                print(j)
                if a_stack[len(a_stack)-2] == j:
                # check the i -1 indices and perform pop operation twice
                    a_stack.pop()
                    a_stack.pop()
            else:
                a_stack.append(i)
            print(a_stack)
            print()
        
        if len(a_stack) == 0:
            return True
        else:
            return False
                
            
        