#!/usr/bin/env python
# coding: utf-8

# In[57]:


MASSAGE_FORMAT = "{}번 원반을 {}에서 {}로 이동"

def moving(N, start, end):# 이동경로를 표시한다.
    print(MASSAGE_FORMAT.format(N, start, end))
    

def hanoi(N,start, end, tmp):
    """N은 원판의 개수, start는 시작지점
       end는 도착지점, tmp는 경유지를 의미합니다.
    """
    if N == 1:#원판의 개수가 1개면 종료됩니다. 
        moving(1, start, end)
        return 1
    else: 
        #원반 n-1개를 시작 기둥에서 경유지로 옮긴다.
        #count 변수를 만들어 옮겨지는 횟수를 구한다.
        count = 0 
        count += hanoi(N-1, start, tmp, end)
        #가장 큰 원반을 시작 기둥에서 경유지로 옮긴다.
        count += 1
        moving(N, start, end)
        #원반 n-1개를 경유지에서 도착 기둥으로 옮긴다.
        count += hanoi(N-1, tmp, end, start)
    return count

hanoi(4,"A","C","B")


# In[ ]:





# In[ ]:




