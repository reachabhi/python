#https://www.hackerrank.com/challenges/text-wrap/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
import textwrap

def wrap(string, max_width):
    x=0
    y=[]
    for i in range(0,int(len(string)/max_width)+1):
        y.append(string[i*max_width:max_width+x])
        x=x+max_width
    return '\n'.join(y)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)