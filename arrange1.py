import os
def ArrangeFiles(path):
     
    files = os.listdir(path)
    extention = []
    
    for file in files:
        ext = os.path.join(path,os.path.splitext(file)[1][1:])
        if ext not in extention:
            extention.append(ext)
    for folder in extention:
        try:
            os.mkdir(folder)
        except:
            pass
        
        for file in files:
            if os.path.split(folder)[1] == os.path.splitext(file)[1][1:]:
                os.rename(os.path.join(path,file),os.path.join(folder,file))



if __name__ == "__main__":
    path = input('enter the path:')
    ArrangeFiles(path)