import os

class FindNewFile:

    def find_new_file(self,path):
        #获取文件夹中的所有文件
        lists = os.listdir(path)

        #对获取的文件根据修改时间进行排序
        lists.sort(key=lambda x:os.path.getmtime(path +'\\'+x))

        #把目录和文件名合成一个路径
        file_new = os.path.join(path,lists[-1])

        return file_new

    def remove_file(self,dir_path,file_num=59):
        '''
        指定文件夹超过60个时删除
        :param path:
        :return:
        '''
        file_list = os.listdir(dir_path)
        file_list.sort(key=lambda x:os.path.getmtime(dir_path +'\\'+x),reverse=True)
        if len(file_list)>file_num:
            for i in file_list[file_num:-1]:
                file_addr = os.path.join(dir_path,i)
                os.remove(file_addr)                                                #删除文件


if __name__ =='__main__':
    from config.get_conf import Conf
    p = Conf().get_file_path('test_file')
    newfile = FindNewFile().remove_file(p)
