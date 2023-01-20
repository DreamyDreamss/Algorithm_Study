users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]
dis_emo = [[emoticons[k]* (100-(idx+1)*10)/100 for idx in range(len(emoticons))] for k  in range(len(emoticons))]

print(dis_emo)

