import os

def processFiles(dirPath, dstFilePath):
    new_f = open(dstFilePath, 'w')

    for file in os.listdir(dirPath):
        file_path = os.path.join(dirPath, file)

        f = open(file_path, 'r')

        line = f.readline()
        while (line):
            new_f.write(line)
            line = f.readline()

if __name__ == '__main__':
    processFiles('C:\\Users\\shankai\\Desktop\\result','data/sendBiaoqingWithPrefetchNoOrigin.txt')