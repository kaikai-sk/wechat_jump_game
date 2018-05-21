import matplotlib.pyplot as plt
import numpy as np

def readfile(fileName):
    hit_count=[]
    miss_count=[]
    called_num=[]
    prefetch_page_num=[]

    f = open(fileName);

    lineIndex=1;
    line = f.readline()
    while (line):
        if (line.find('#') == -1):
            if (line.find('hitcount') >= 0):
                hit_count.append(int(line.split(':')[1]))
            if (line.find('misscount') >= 0):
                miss_count.append(int(line.split(':')[1]))
            if (line.find('prefetch_success_called_num') >= 0):
                called_num.append(int(line.split(':')[1]))
            if (line.find('prefetch_page_num') >= 0):
                prefetch_page_num.append(int(line.split(':')[1]))

        line = f.readline()
        lineIndex=lineIndex+1;
    return hit_count,miss_count,called_num,prefetch_page_num

if __name__ == '__main__':
    prefetch_success_called_num_no_prefetch_with_origin=[]
    prefetch_success_called_num_with_prefetch_with_origin=[]
    prefetch_success_called_num_no_prefetch_no_origin=[]
    prefetch_success_called_num_with_prefetch_no_origin=[]

    prefetch_page_num_no_prefetch_with_origin=[]
    prefetch_page_num_with_prefetch_with_origin=[]
    prefetch_page_num_no_prefetch_no_origin=[]
    prefetch_page_num_with_prefetch_no_origin=[]

    hit_count_no_prefetch_with_origin=[]
    hit_count_with_prefetch_with_origin=[]
    hit_count_no_prefetch_no_origin=[]
    miss_count_no_prefetch_with_origin = []
    miss_count_with_prefetch_with_origin = []
    miss_count_no_prefetch_no_origin = []


    hit_count_no_prefetch_with_origin,miss_count_no_prefetch_with_origin,\
    prefetch_success_called_num_no_prefetch_with_origin,prefetch_page_num_no_prefetch_with_origin=readfile('data/sendBiaoqingNoPrefetchWithOrigin.txt')
    hit_count_with_prefetch_with_origin,miss_count_with_prefetch_with_origin, \
    prefetch_success_called_num_with_prefetch_with_origin, prefetch_page_num_with_prefetch_with_origin=readfile('data/sendBiaoqingWithPrefetchWithOrigin.txt')
    hit_count_no_prefetch_no_origin, miss_count_no_prefetch_no_origin , \
    prefetch_success_called_num_no_prefetch_no_origin, prefetch_page_num_no_prefetch_no_origin= readfile('data/sendBiaoqingNoPrefetchNoOrigin.txt')
    hit_count_with_prefetch_no_origin, miss_count_with_prefetch_no_origin , \
    prefetch_success_called_num_with_prefetch_no_origin, prefetch_page_num_with_prefetch_no_origin= readfile('data/sendBiaoqingWithPrefetchNoOrigin.txt')

    prefetch_success_all=[]
    prefetch_success_all.append(prefetch_success_called_num_no_prefetch_with_origin)
    prefetch_success_all.append(prefetch_success_called_num_with_prefetch_with_origin)
    prefetch_success_all.append(prefetch_success_called_num_no_prefetch_no_origin)
    prefetch_success_all.append(prefetch_success_called_num_with_prefetch_no_origin)

    page_num_all=[prefetch_page_num_no_prefetch_with_origin,prefetch_page_num_with_prefetch_with_origin,prefetch_page_num_no_prefetch_no_origin,prefetch_page_num_with_prefetch_no_origin]



    total_count_no_prefetch_with_origin=[]
    total_count_with_prefetch_with_origin = []
    total_count_no_prefetch_no_origin = []
    total_count_with_prefetch_no_origin = []

    for i in range(0,len(hit_count_no_prefetch_with_origin)):
        total_count_no_prefetch_with_origin.append(hit_count_no_prefetch_with_origin[i]+miss_count_no_prefetch_with_origin[i])
    for i in range(0,len(hit_count_with_prefetch_with_origin)):
        total_count_with_prefetch_with_origin.append(hit_count_with_prefetch_with_origin[i]+miss_count_with_prefetch_with_origin[i])
    for i in range(0,len(hit_count_no_prefetch_no_origin)):
        total_count_no_prefetch_no_origin.append(hit_count_no_prefetch_no_origin[i]+miss_count_no_prefetch_no_origin[i])
    for i in range(0,len(hit_count_with_prefetch_no_origin)):
        total_count_with_prefetch_no_origin.append(hit_count_with_prefetch_no_origin[i]+miss_count_with_prefetch_no_origin[i])

    per_hit_count_no_prefetch_with_origin=[]
    per_miss_count_no_prefetch_with_origin = []
    per_hit_count_with_prefetch_with_origin = []
    per_miss_count_with_prefetch_with_origin=[]
    per_hit_count_no_prefetch_no_origin = []
    per_miss_count_no_prefetch_no_origin = []
    per_hit_count_with_prefetch_no_origin = []
    per_miss_count_with_prefetch_no_origin = []

    per_prefetch_success_all = []
    per_prefetch_success_called_num_no_prefetch_with_origin=[]
    per_prefetch_success_all.append(per_prefetch_success_called_num_no_prefetch_with_origin)
    per_prefetch_success_called_num_with_prefetch_with_origin=[]
    per_prefetch_success_all.append(per_prefetch_success_called_num_with_prefetch_with_origin)
    per_prefetch_success_called_num_no_prefetch_no_origin=[]
    per_prefetch_success_all.append(per_prefetch_success_called_num_no_prefetch_no_origin)
    per_prefetch_success_called_num_with_prefetch_no_origin=[]
    per_prefetch_success_all.append(per_prefetch_success_called_num_with_prefetch_no_origin)

    per_prefetch_page_num_no_prefetch_with_origin=[]
    per_prefetch_page_num_with_prefetch_with_origin = []
    per_prefetch_page_num_no_prefetch_no_origin = []
    per_prefetch_page_num_with_prefetch_no_origin = []
    per_page_num_all=[per_prefetch_page_num_no_prefetch_with_origin,per_prefetch_page_num_with_prefetch_with_origin,
                      per_prefetch_page_num_no_prefetch_no_origin,per_prefetch_page_num_with_prefetch_no_origin]


    per_total_count_no_prefetch_with_origin = []
    per_total_count_with_prefetch_with_origin = []
    per_total_count_no_prefetch_no_origin = []
    per_total_count_with_prefetch_no_origin = []

    for i in range(len(prefetch_success_all)):
        for j in range(1,len(prefetch_success_all[i])):
            per_prefetch_success_all[i].append(prefetch_success_all[i][j]-prefetch_success_all[i][j-1])

    for i in range(len(per_page_num_all)):
        for j in range(1, len(page_num_all[i])):
            per_page_num_all[i].append(page_num_all[i][j] - page_num_all[i][j - 1])


    for i in range(1,len(hit_count_no_prefetch_with_origin)):
        per_hit_count_no_prefetch_with_origin.append(hit_count_no_prefetch_with_origin[i]-hit_count_no_prefetch_with_origin[i-1])
        per_miss_count_no_prefetch_with_origin.append(miss_count_no_prefetch_with_origin[i] - miss_count_no_prefetch_with_origin[i - 1])
    for i in range(1,len(hit_count_with_prefetch_with_origin)):
        per_hit_count_with_prefetch_with_origin.append(hit_count_with_prefetch_with_origin[i] - hit_count_with_prefetch_with_origin[i - 1])
        per_miss_count_with_prefetch_with_origin.append(miss_count_with_prefetch_with_origin[i] - miss_count_with_prefetch_with_origin[i - 1])
    for i in range(1,len(hit_count_no_prefetch_no_origin)):
        per_hit_count_no_prefetch_no_origin.append(hit_count_no_prefetch_no_origin[i] - hit_count_no_prefetch_no_origin[i - 1])
        per_miss_count_no_prefetch_no_origin.append(miss_count_no_prefetch_no_origin[i] - miss_count_no_prefetch_no_origin[i - 1])
    for i in range(1, len(hit_count_with_prefetch_no_origin)):
        per_hit_count_with_prefetch_no_origin.append(hit_count_with_prefetch_no_origin[i] - hit_count_with_prefetch_no_origin[i - 1])
        per_miss_count_with_prefetch_no_origin.append(miss_count_with_prefetch_no_origin[i] - miss_count_with_prefetch_no_origin[i - 1])

    for i in range(0, len(per_hit_count_no_prefetch_with_origin)):
        per_total_count_no_prefetch_with_origin.append(per_hit_count_no_prefetch_with_origin[i] + per_miss_count_no_prefetch_with_origin[i])
    for i in range(0, len(per_hit_count_with_prefetch_with_origin)):
        per_total_count_with_prefetch_with_origin.append(per_hit_count_with_prefetch_with_origin[i] + per_miss_count_with_prefetch_with_origin[i])
    for i in range(0, len(per_hit_count_no_prefetch_no_origin)):
        per_total_count_no_prefetch_no_origin.append(per_hit_count_no_prefetch_no_origin[i] + per_miss_count_no_prefetch_no_origin[i])
    for i in range(0, len(per_hit_count_with_prefetch_no_origin)):
        per_total_count_with_prefetch_no_origin.append(per_hit_count_with_prefetch_no_origin[i] + per_miss_count_with_prefetch_no_origin[i])

    # mean
    print('per mean of hit where no prefetch with origin : ' + str(np.mean(per_hit_count_no_prefetch_with_origin)))
    print('per mean of hit where with prefetch with origin : ' + str(np.mean(per_hit_count_with_prefetch_with_origin)))
    print('per mean of miss where no prefetch with origin : ' + str(np.mean(per_miss_count_no_prefetch_with_origin)))
    print('per mean of miss where with prefetch with origin : ' + str(np.mean(per_miss_count_with_prefetch_with_origin)))

    print('per mean of hit where no prefetch no origin : ' + str(np.mean(per_hit_count_no_prefetch_no_origin)))
    print('per mean of hit where with prefetch no origin : ' + str(np.mean(per_hit_count_with_prefetch_no_origin)))
    print('per mean of miss where no prefetch no origin : ' + str(np.mean(per_miss_count_no_prefetch_no_origin)))
    print('per mean of miss where with prefetch no origin : ' + str(np.mean(per_miss_count_with_prefetch_no_origin)))

    #stdev
    print('per std of hit where no prefetch with origin : ' + str(np.std(per_hit_count_no_prefetch_with_origin,ddof = 1)))
    print('per std of hit where with prefetch with origin : ' + str(np.std(per_hit_count_with_prefetch_with_origin,ddof = 1)))
    print('per std of miss where no prefetch with origin : ' + str(np.std(per_miss_count_no_prefetch_with_origin,ddof = 1)))
    print('per std of miss where with prefetch with origin : ' + str(np.std(per_miss_count_with_prefetch_with_origin,ddof = 1)))

    print('per std of hit where no prefetch no origin : ' + str(np.std(per_hit_count_no_prefetch_no_origin, ddof=1)))
    print('per std of hit where with prefetch no origin : ' + str(np.std(per_hit_count_with_prefetch_no_origin, ddof=1)))
    print('per std of miss where no prefetch no origin : ' + str(np.std(per_miss_count_no_prefetch_no_origin, ddof=1)))
    print('per std of miss where with prefetch no origin : ' + str(np.std(per_miss_count_with_prefetch_no_origin, ddof=1)))

    plt.figure()
    # hit count
    plt.subplot(4, 2, 1)  # （行，列，活跃区）
    plt.plot(hit_count_with_prefetch_with_origin,label='with prefetch with origin')
    plt.plot(hit_count_no_prefetch_with_origin,'x-',label='no prefetch with origin')
    plt.plot(hit_count_no_prefetch_no_origin,'o-', label='no prefetch no origin')
    plt.plot(hit_count_with_prefetch_no_origin,'+-',label='with prefetch no origin')
    plt.title('hit count')  # 添加图形标题
    plt.legend();

    # miss count
    plt.subplot(4, 2, 3)
    plt.plot(miss_count_with_prefetch_with_origin,label='with prefetch with origin')
    plt.plot(miss_count_no_prefetch_with_origin,'x-',label='no prefetch with origin')
    plt.plot(miss_count_no_prefetch_no_origin, 'o-',label='no prefetch no origin')
    plt.plot(miss_count_with_prefetch_no_origin, '+-',label='with prefetch no origin')
    plt.title('miss count')  # 添加图形标题
    plt.legend();

    # total count
    plt.subplot(4, 2, 5)
    plt.plot(total_count_with_prefetch_with_origin, label='with prefetch with origin')
    plt.plot(total_count_no_prefetch_with_origin,'x-', label='no prefetch with origin')
    plt.plot(total_count_no_prefetch_no_origin, 'o-',label='no prefetch no origin')
    plt.plot(total_count_with_prefetch_no_origin,'+-' ,label='with prefetch no origin')
    plt.title('total count')  # 添加图形标题
    plt.legend();

    # success called num
    plt.subplot(4, 2, 7)
    plt.plot(prefetch_success_called_num_with_prefetch_no_origin, label='called num with prefetch no origin')
    plt.title('success called count')  # 添加图形标题
    plt.legend();

    # per hit count
    plt.subplot(4, 2, 2)
    plt.plot(per_hit_count_with_prefetch_with_origin, label='with prefetch with origin')
    plt.plot(per_hit_count_no_prefetch_with_origin,'x-', label='no prefetch with origin')
    plt.plot(per_hit_count_no_prefetch_no_origin, 'o-',label='no prefetch no origin')
    plt.plot(per_hit_count_with_prefetch_no_origin,'+-', label='with prefetch no origin')
    plt.title('per hit count')  # 添加图形标题
    plt.legend();

    # per miss count
    plt.subplot(4, 2, 4)
    plt.plot(per_miss_count_with_prefetch_with_origin, label='with prefetch with origin')
    plt.plot(per_miss_count_no_prefetch_with_origin,'x-' ,label='no prefetch with origin')
    plt.plot(per_miss_count_no_prefetch_no_origin,'o-' ,label='no prefetch no origin')
    plt.plot(per_miss_count_with_prefetch_no_origin,'+-', label='with prefetch no origin')
    plt.title('per miss count')  # 添加图形标题
    plt.legend();

    # per total count
    plt.subplot(4, 2, 6)
    plt.plot(per_total_count_with_prefetch_with_origin, label='with prefetch with origin')
    plt.plot(per_total_count_no_prefetch_with_origin,'x-', label='no prefetch with origin')
    plt.plot(per_total_count_no_prefetch_no_origin,'o-' ,label='no prefetch no origin')
    plt.plot(per_total_count_with_prefetch_no_origin, '+-',label='with prefetch no origin')
    plt.title('per total count')  # 添加图形标题
    plt.legend();

    # per success called count
    plt.subplot(4, 2, 8)
    plt.plot(per_prefetch_page_num_with_prefetch_no_origin, label='called num with prefetch no origin')
    plt.title('per miss count')  # 添加图形标题
    plt.legend();

    # plt.subplots_adjust(wspace=0, hspace=5)  # 调整子图间距
    plt.show()


