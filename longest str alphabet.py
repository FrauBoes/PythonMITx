#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 15:23:38 2017

@author: thelma
"""
s = "oswirhvoqreaulod"
ans = max(s)
temp = ""
last_ans = 0
last_temp = 0
for start in range(len(s)-1):
    end = start+1
    if s[start] <= s[end]:
        if last_ans == start:
            if last_ans == 0:
                ans = s[start:end+1]
                last_ans = end
            else:
                ans = ans + s[end]
                last_ans = end
        elif last_temp == start:
            if last_temp == 0:
                temp = s[start:end+1]
                last_temp = end
            else:
                temp = temp + s[end]
                last_temp = end
                if len(temp) > len (ans):
                    ans = temp
                    last_ans = end
                    temp = ""
        else:
            temp = s[start:end+1]
            last_temp = end
print(ans)