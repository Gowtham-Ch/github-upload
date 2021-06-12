class Path:
    def __init__(self, path):
        self.live_path = path

    def cd(self, new_path):
        i=0;
        val_pathList=new_path.split('/')
        pathLength=len(val_pathList)
        pathList=self.live_path.split('/')
        if val_pathList[0]=='':
            del pathList[:]
            pathList.append('/'+val_pathList[1])
            i=i+2
        while(i<pathLength):
            j=len(pathList)-1
            if val_pathList[i]=='..':
                pathList.pop(j)
            else:
                pathList.append(val_pathList[i])
            i=i+1
        self.live_path="/".join(pathList)

        pass

path = Path('/a/b/c/d')
path.cd('/x/y/../z')
print(path.live_path)