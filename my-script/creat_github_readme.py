import os


def creat_dir_dict(root_path, dir_name):
    dict = {}
    file_dir = root_path+dir_name
    for root, dirs, files in os.walk(file_dir):
        files = [f for f in files if not f[0] == '.']
        dirs[:] = [d for d in dirs if not d[0] == '.']
        if root == root_path+dir_name:
            continue
        # use files and dirs
        root_name=root[len(root_path)+len(dir_name)+1:]
        list=[]
        for file_name in files:
            if file_name.split(".")[-1] != "md":
                continue
            list.append(os.path.join("https://github.com/a827871781/", dir_name, "blob/master/", root_name, file_name))
            # print(root)
            # print(os.path.join(root, file_name) )
        dict[root_name] = list

    return dict

def create__file(file_path,dict):
    f=open(file_path,"a")
    for key in dict.keys():
        f.write("### ["+key+"](https://github.com/a827871781/Java-notes/tree/master/"+key+")"+'\n')

        count=0
        for file_name in dict[key]:
            count=count+1
            f.write(str(count)+". ["+(file_name.split('/')[-1]).split('.')[0]+"]("+file_name+")"+'\n')

        f.write("\n")

    f.close

if __name__ == '__main__':
    dict = creat_dir_dict("/Users/syz/Documents/", "Java-notes")
    # file_name="README1.md"
    # file_path="/Users/syz/Documents/Java-notes/"+file_name
    # create__file(file_path,dict)
    print(dict)
    for key in dict.keys():
        print(key)
        for file_name in dict[key]:
            print(file_name)








