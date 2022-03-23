from decision import price_ascend,cost_performance,score_descend
cars_list=[]
raw=open('data.txt','r')
for x in raw.readline():
    cars_detail={'价格得分':0,'性能得分':0,'性价比得分':0,}
    