# 중위 표기식을 후위 표기식으로 바꾸는 방법을 간단히 설명하면 이렇다. 
# 우선 주어진 중위 표기식을 연산자의 우선순위에 따라 괄호로 묶어준다. 
# 그런 다음에 괄호 안의 연산자를 괄호의 오른쪽으로 옮겨주면 된다.
# 예를 들어 a+b*c는 (a+(b*c))의 식과 같게 된다.
# 그 다음에 안에 있는 괄호의 연산자 *를 괄호 밖으로 꺼내게 되면 (a+bc*)가 된다. 
# 마지막으로 또 +를 괄호의 오른쪽으로 고치면 abc*+가 되게 된다.

import sys
input = sys.stdin.readline

formula = input().rstrip()

isp = {'(':0, '+':1, '-':1, '*':2, '/':2, ')':0}
icp = {'(':3, '+':1, '-':1, '*':2, '/':2, ')':0}

stack = []
postfix = ''
for f in formula:
    
    # 1. 연산자
    if f in isp:
        
        # 1. stack top 연산자보다 우선순위가 높을 때
        if stack and icp[f] > isp[stack[-1]]:
            stack.append(f)
        
        # 2. stack top 연산자보다 우선순위가 높지 않을 때
        else:
            # 우측 괄호만 따로 처리
            if f == ')':
                while stack and stack[-1] != '(':
                    postfix += stack.pop()
                stack.pop() # 우측 괄호 날려버리기 
                
            # 우측 괄호가 아닐 때 처리
            else:
                # stack top 연산자보다 우선순위가 높아질 때까지 pop & push
                while stack and icp[f] <= isp[stack[-1]]:
                    postfix += stack.pop()
                stack.append(f)
    
    # 2. 피연산자
    else:
        postfix += f
      
# 3. stack에 연산자가 남아있다면 pop  
while stack:
    postfix += stack.pop()
    
print(postfix)