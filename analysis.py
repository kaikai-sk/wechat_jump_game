import matplotlib.pyplot as plt
import numpy as np

def readfile(fileName):
    hit_count=[]
    miss_count=[]

    f = open(fileName);

    lineIndex=1;
    line = f.readline()
    while (line):
        if (line.find('#') == -1):
            if (line.find('hitcount') >= 0):
                hit_count.append(int(line.split(':')[1]))
            if (line.find('misscount') >= 0):
                miss_count.append(int(line.split(':')[1]))
        line = f.readline()
        print(lineIndex)
        lineIndex=lineIndex+1;
    return hit_count,miss_count

if __name__ == '__main__':
    hit_count_no_prefetch=[];
    miss_count_no_prefetch = [];
    hit_count_with_prefetch = [];
    miss_count_with_prefetch = [];

    hit_count_no_prefetch,miss_count_no_prefetch=readfile('data/sendBiaoqingNoPrefetch.txt')
    hit_count_with_prefetch,miss_count_with_prefetch=readfile('data/sendBiaoqingWithPrefetch.txt')

    total_count_no_prefetch=[]
    total_count_with_prefetch = []

    for i in range(0,len(hit_count_no_prefetch)):
        total_count_no_prefetch.append(hit_count_no_prefetch[i]+miss_count_no_prefetch[i])
    for i in range(0,len(hit_count_with_prefetch)):
        total_count_with_prefetch.append(hit_count_with_prefetch[i]+miss_count_with_prefetch[i])

    per_hit_count_no_prefetch=[]
    per_miss_count_no_prefetch = []
    per_hit_count_with_prefetch = []
    per_miss_count_with_prefetch=[]
    per_total_count_no_prefetch = []
    per_total_count_with_prefetch = []

    for i in range(1,len(hit_count_no_prefetch)):
        per_hit_count_no_prefetch.append(hit_count_no_prefetch[i]-hit_count_no_prefetch[i-1])
        per_miss_count_no_prefetch.append(miss_count_no_prefetch[i] - miss_count_no_prefetch[i - 1])
    for i in range(1,len(hit_count_with_prefetch)):
        per_hit_count_with_prefetch.append(hit_count_with_prefetch[i] - hit_count_with_prefetch[i - 1])
        per_miss_count_with_prefetch.append(miss_count_with_prefetch[i] - miss_count_with_prefetch[i - 1])

    for i in range(0, len(per_hit_count_no_prefetch)):
        per_total_count_no_prefetch.append(per_hit_count_no_prefetch[i] + per_miss_count_no_prefetch[i])
    for i in range(0, len(per_hit_count_with_prefetch)):
        per_total_count_with_prefetch.append(per_hit_count_with_prefetch[i] + per_miss_count_with_prefetch[i])

    plt.figure()
    plt.subplot(6, 1, 1)  # （行，列，活跃区）
    plt.plot(hit_count_with_prefetch,label='with prefetch')
    plt.plot(hit_count_no_prefetch,label='no prefetch')
    plt.title('hit count')  # 添加图形标题
    plt.legend();

    plt.subplot(6, 1, 2)
    plt.plot(miss_count_with_prefetch,label='with prefetch')
    plt.plot(miss_count_no_prefetch,label='no prefetch')
    plt.title('miss count')  # 添加图形标题
    plt.legend();

    plt.subplot(6, 1, 3)
    plt.plot(total_count_with_prefetch, label='with prefetch')
    plt.plot(total_count_no_prefetch, label='no prefetch')
    plt.title('total count')  # 添加图形标题
    plt.legend();

    plt.subplot(6, 1, 4)
    plt.plot(per_hit_count_with_prefetch, label='with prefetch')
    plt.plot(per_hit_count_no_prefetch, label='no prefetch')
    plt.title('per hit count')  # 添加图形标题
    plt.legend();

    plt.subplot(6, 1, 5)
    plt.plot(per_miss_count_with_prefetch, label='with prefetch')
    plt.plot(per_miss_count_no_prefetch, label='no prefetch')
    plt.title('per miss count')  # 添加图形标题
    plt.legend();

    plt.subplot(6, 1, 6)
    plt.plot(per_total_count_with_prefetch, label='with prefetch')
    plt.plot(per_total_count_no_prefetch, label='no prefetch')
    plt.title('per total count')  # 添加图形标题
    plt.legend();

    plt.show()


