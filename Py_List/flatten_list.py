"""
1- Bir listeyi düzleştiren (flatten) fonksiyon yazın.
 Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. 
 Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]
"""

l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flatten(lx):
    f_list = []
    def loop(lx):
        for i in lx:
            if isinstance(i,list):
                loop(i)
            else:
                f_list.append(i)
    loop(lx)
    return f_list

flatten(l)

