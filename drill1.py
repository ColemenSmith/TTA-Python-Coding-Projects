
import os

# use listdir() to iterate through all files
# use path.join() concatenate file name to file path forming absolute path
# use use getmtime() find latest date taht file has been created or modified
# print each file ending with a .txt extension and corresponding mtime to console




def findTxt():
    folder = 'E:\\Documents - HDD\\drill\\'
    for file in os.listdir(folder):
        filename = os.fsdecode(file)
        if filename.endswith('.txt'):
            print(os.path.getmtime(os.path.join(folder, filename)), os.path.join(folder, filename))
            continue
        else:
            continue
    
        




if __name__ == '__main__':
    findTxt()
