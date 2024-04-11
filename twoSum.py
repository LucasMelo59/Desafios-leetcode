meu_dic = []

list = [11,4,2,7]
target = 9


meu_dic = []
for index,chave in enumerate(nums):
                if (chave in meu_dic):
                    print([nums.index(target - chave),index])
                else :
                    meu_dic.append(target - chave)

     

