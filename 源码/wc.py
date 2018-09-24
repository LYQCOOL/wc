# _*_ encoding:utf-8 _*_
__author__ = 'LYQ'
__date__ = '2018/9/21 9:50'
import sys
import re
import os
from tkinter import *
import tkinter.filedialog
from tkinter.filedialog import askdirectory, askopenfile

# 获取wc.py的父目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 生成result.txt在当前目录
result_path = os.path.join(BASE_DIR, 'result.txt')
# 初始化目录所有文件为空
allfile = []
# 获取当前所在目录
Now_Dir = os.getcwd()


def only_one():
    '''
    无命令参数时，写入文件单词，字符，行数
    :return: 
    '''
    file_path = sys.argv[-1]
    try:
        with open(file_path, 'r') as fp:
            all_text = fp.read()
            zifu = len(all_text)
            words = len(re.split('[\s,，]', all_text))
            hangs = len(all_text.split('\n'))
            with open(result_path, 'a', encoding='utf-8') as fp2:
                fp2.write(sys.argv[-1] + ',' + '字符数:' + str(zifu) + '\n')
                fp2.write(sys.argv[-1] + ',' + '单词数:' + str(words) + '\n')
                fp2.write(sys.argv[-1] + ',' + '行数:' + str(hangs) + '\n')
                # print(fp2.name)
                # print('字符数：' + str(zifu) + '\n' + '单词数：' + str(words) + '\n' + '行数：' + str(hangs))
        fp.close()
    except:
        print('参数为一个时只能是文件或文件路径！' + '请检查参数是否正确或文件是否正确！')


def include_many_minglin(file_path, out_file=result_path, stop_txt_path=''):
    '''
    包含多个参数时：
        file_path:被读取文件的路径
        out_file:输出结果输入的文件路径
    :param file_path: 
    :param out_file: 
    :return: 
    '''
    try:
        with open(file_path, 'r') as fp:
            all_text = fp.read()
            all_minglin = sys.argv[1:-1]
            if '-c' in all_minglin:
                zifu = len(all_text.strip())
                try:
                    with open(out_file, 'a', encoding='utf-8') as fp2:
                        fp2.write(file_path + ',字符数：' + str(zifu) + '\n')
                    fp2.close()
                except:
                    print('输出文件打开或创建失败！')
                    exit()
                    # print('字符数：' + str(zifu))
            if '-w' in all_minglin:
                words = re.split('[\s,，]', all_text)
                try:
                    if stop_txt_path:
                        try:
                            with open(stop_txt_path, 'r') as stops:
                                stop_words = stops.read().split()
                                with open(out_file, 'a', encoding='utf-8') as fp2:
                                    for word in words:
                                        if word in stop_words:
                                            words.remove(word)
                                        else:
                                            pass
                                    fp2.write(file_path + ',单词数：' + str(len(words)) + '\n')
                                fp2.close()
                            stops.close()
                        except:
                            print('停止词文件打开失败！！')
                    else:
                        with open(out_file, 'a', encoding='utf-8') as fp2:
                            fp2.write(file_path + ',单词数：' + str(len(words)) + '\n')
                        fp2.close()
                except:
                    print('输出文件打开或创建失败！')
                    exit()
            if '-l' in all_minglin:
                hangs = len(all_text.split('\n'))
                try:
                    with open(out_file, 'a', encoding='utf-8') as fp2:
                        fp2.write(file_path + ',行数：' + str(hangs) + '\n')
                    fp2.close()
                except:
                    print('输出文件打开或创建失败！')
                    exit()
                    # print('行数：' + str(hangs))
            if '-a' in all_minglin:
                control_data = ['%', '-', 'm.n', 'l', 'h']
                hangss = all_text.split('\n')
                null_ = True
                code = 0
                nulls = 0
                zhushi = 0
                for hang in hangss:
                    if len(hang) > 1:
                        for every_data in hang:
                            if every_data in control_data:
                                pass
                            else:
                                null_ = False
                                break
                    if null_ == True or hang == '{' or hang == '}' or len(hang) == 0:
                        nulls += 1
                    else:
                        if '//' in hang or '/*' in hang:
                            zhushi += 1
                        else:
                            code += 1
                with open(out_file, 'a', encoding='utf-8') as fp2:
                    fp2.write(file_path + ',' + '代码行/空行/注释行：' + str(code) + '/' + str(nulls) + '/' + str(zhushi) + '\n')
                fp2.close()
        fp.close()
    except:
        print('你的文件路径或文件格式错误，无法打开该文件，请检查后再次输入！！！')


def out_nominglin(file_path, stop_txt_path=''):
    '''
    输出结果指定文件指定，但不带参数
    :param file_path: 
    :return: 
    '''
    try:
        with open(file_path, 'r') as fp:
            all_text = fp.read()
            zifu = len(all_text)
            words = len(re.split('[\s,，]', all_text))
            hangs = len(all_text.split('\n'))
            with open(out_file, 'a', encoding='utf-8') as fp2:
                fp2.write(sys.argv[-3] + ',字符数：' + str(zifu) + '\n')
                if stop_txt_path:
                    try:
                        with open(stop_txt_path, 'r') as stops:
                            stop_words = stops.read().split()
                            with open(out_file, 'a', encoding='utf-8') as fp2:
                                for word in words:
                                    if word in stop_words:
                                        words.remove(word)
                                    else:
                                        pass
                                fp2.write(file_path + ',单词数：' + str(len(words)) + '\n')
                            fp2.close()
                        stops.close()
                    except:
                        print('停止词文件打开失败！！')
                else:
                    fp2.write(sys.argv[-3] + ',单词数：' + str(words) + '\n')
                fp2.write(sys.argv[-3] + ',行数：' + str(hangs) + '\n')
            fp2.close()
        fp.close()
    except:
        print('你的文件路径或文件格式错误，无法打开该文件，请检查后再次输入！！！')


def getallfile(path):
    '''
    递归获取目录下所有文件
    :param path: 
    :return: 
    '''
    allfilelist = os.listdir(path)
    for file in allfilelist:
        filepath = os.path.join(path, file)
        # 判断是不是文件夹
        if os.path.isdir(filepath):
            getallfile(filepath)
        else:
            allfile.append(filepath)
    return allfile


def tomgpei(re_file):
    '''
    通配符匹配
    :param re_file: 
    :return: 
    '''
    if os.path.exists(re_file):
        if os.path.isdir(re_file):
            allfiles = getallfile(re_file)
            return allfiles
        elif os.path.isfile(re_file):
            all = []
            all.append(re_file)
            return all
        else:
            print('不是文件名或目录！')
            return None
    elif '*' in re_file:
        all_txts = []
        allfiles = getallfile(Now_Dir)
        split_datas = re_file.split('*')
        for file in allfiles:
            y_n = True
            for split_data in split_datas:
                if split_data in file:
                    pass
                else:
                    y_n = False
            if y_n == True:
                all_txts.append(file)
            else:
                pass
        return all_txts
    else:
        print('目录或文件不存在！')
        return None


class App:
    '''
    gui实现可视化
    '''

    def __init__(self, master):
        # 构造函数里传入一个父组件(master),创建一个Frame组件并显示
        frame = Frame(master)
        frame.pack()
        # 创建两个button，并作为frame的一部分
        self.wenjian_path = StringVar()
        self.label = Label(text="文件路径： ")
        self.label.pack(side=TOP)
        self.entry = Entry(textvariable=self.wenjian_path)
        self.entry.pack(side=TOP)
        self.button = Button(frame, text="退出", fg="red", command=frame.quit, anchor='sw')
        self.button.pack(side=RIGHT)  # 此处side为LEFT表示将其放置 到frame剩余空间的最左方
        self.hi_there = Button(frame, text="选择文件", fg='red', command=self.chose_wenjian, anchor='se')
        self.hi_there.pack(side=LEFT)
        self.label = Label(text="文件信息显示： ")
        self.label.pack(side=TOP)
        self.txt = Text(width=55, height=15)
        self.txt.pack()

    def chose_wenjian(self):
        paths = askopenfile()
        self.wenjian_path.set(paths.name)
        if paths:
            self.txt.delete(0.0, tkinter.END)
            try:
                with open(paths.name, 'r') as f:
                    all_contents = f.read()
                    zifu = len(all_contents)
                    words = len(re.split('[\s,，]', all_contents))
                    hangs = len(all_contents.split('\n'))
                    control_data = ['%', '-', 'm.n', 'l', 'h']
                    null_ = True
                    code = 0
                    nulls = 0
                    zhushi = 0
                    hangss = all_contents.split('\n')
                    for hang in hangss:
                        if len(hang) > 1:
                            for every_data in hang:
                                if every_data in control_data:
                                    pass
                                else:
                                    null_ = False
                                    break
                        if null_ == True or hang == '{' or hang == '}' or len(hang) == 0:
                            nulls += 1
                        else:
                            if '//' in hang or '/*' in hang:
                                zhushi += 1
                            else:
                                code += 1
                    self.txt.insert(END, "字符数：" + str(zifu) + "\n")
                    self.txt.insert(END, "单词数：" + str(words) + "\n")
                    self.txt.insert(END, "行数：" + str(hangs) + "\n")
                    self.txt.insert(END, "代码行数：" + str(code) + "\n")
                    self.txt.insert(END, "空行数：" + str(nulls) + "\n")
                    self.txt.insert(END, "注释行数：" + str(zhushi) + "\n")

            except:
                self.txt.insert(END, "文件打开失败，请检查文件格式是否正确！！！")
        else:
            pass


if __name__ == '__main__':
    # 默认无结果输出文件
    data_out_txt = False
    # 默认为停止词文件
    data_stop_txt = False
    #是否含需要遍历目录
    DIGUI = False
    if len(sys.argv) <= 1:
        print('命令格式不正确！！！')
    elif len(sys.argv) == 2:
        if sys.argv[-1] == '-x':
            win = Tk()
            win.geometry('500x310+500+200')
            # 设置窗口标题
            win.title('文件检索')
            app = App(win)
            win.mainloop()
        else:
            only_one()
    else:
        minglin = ['-c', '-w', '-l', '-o', '-s', '-a', '-e']
        for i in sys.argv[1:-1]:
            if i not in minglin and sys.argv[sys.argv.index(i) + 1] == '-o':
                pass
            elif i not in minglin and sys.argv[sys.argv.index(i) - 1] == '-o':
                pass
            elif i not in minglin and sys.argv[sys.argv.index(i) - 1] == '-e':
                pass
            elif i not in minglin and sys.argv[sys.argv.index(i) + 1] == '-e':
                pass
            elif i not in minglin and "-s" in sys.argv[1:sys.argv.index(i)]:
                pass
            else:
                if i in minglin and sys.argv.count(i) == 1 and i != '-o' and i != '-e' and i!='-s':
                    pass
                elif i in minglin and sys.argv.count(i) > 1:
                    print('命令重复！！请修改！')
                    # break
                    exit()
                elif sys.argv.count(i) == 1 and i == '-o':
                    data_out_txt = True
                elif sys.argv.count(i) == 1 and i == '-e':
                    data_stop_txt = True
                    stop_txt_path = sys.argv[sys.argv.index(i) + 1]
                elif sys.argv.count(i) == 1 and i == '-s':
                    DIGUI = True
                else:
                    print('命令格式错误！！！')
                    # break
                    exit()
        if data_out_txt == False and data_stop_txt == False:
            if DIGUI:
                file_paths = tomgpei(sys.argv[-1])
                if file_paths:
                    for file_path in file_paths:
                        include_many_minglin(file_path)
                else:
                    print('未匹配到相关文件')
            else:
                file_path = sys.argv[-1]
                include_many_minglin(file_path, result_path)
        elif data_out_txt == True and data_stop_txt == False:
            if DIGUI:
                file_paths = tomgpei(sys.argv[-3])
                out_file = sys.argv[-1]
                if sys.argv[-2] == '-o':
                    if len(sys.argv) == 4:
                        if file_paths:
                            for file_path in file_paths:
                                out_nominglin(file_path)
                        else:
                            print('未匹配到相关文件')
                    else:
                        if file_paths:
                            for file_path in file_paths:
                                include_many_minglin(file_path, out_file)
                        else:
                            print('未匹配到相关文件')
                else:
                    print('命令格式错误，"-o"后面应该紧挨结果输出的指定文件文件')
            else:
                file_path = sys.argv[-3]
                out_file = sys.argv[-1]
                if sys.argv[-2] == '-o':
                    if len(sys.argv) == 4:
                        out_nominglin(file_path)
                    else:
                        include_many_minglin(file_path, out_file)
                else:
                    print('命令格式错误，"-o"后面应该紧挨结果输出的指定文件文件')
        elif data_out_txt == False and data_stop_txt == True:
            if DIGUI:
                file_paths = tomgpei(sys.argv[-1])
                if file_paths[0]==stop_txt_path:
                    file_paths=tomgpei(sys.argv[-3])
                else:
                    pass
                if file_paths:
                    for file_path in file_paths:
                        include_many_minglin(file_path, result_path, stop_txt_path)
                else:
                    print('未匹配到相关文件')
            else:
                file_path = sys.argv[-1]
                if file_path==stop_txt_path:
                    file_path=sys.argv[-3]
                include_many_minglin(file_path, result_path, stop_txt_path)
        elif data_out_txt == True and data_stop_txt == True:
            file_paths = tomgpei(sys.argv[-3])
            out_file = sys.argv[-1]
            if file_paths[0] == stop_txt_path:
                file_paths = tomgpei(sys.argv[-5])
            if sys.argv[-2] == '-o':
                if len(sys.argv) == 4:
                    if DIGUI:
                        if file_paths:
                            for file_path in file_paths:
                                out_nominglin(file_path, stop_txt_path)
                        else:
                            print('未匹配到相关文件')
                    else:
                        file_path = sys.argv[-3]
                        if file_path==stop_txt_path:
                            file_path=sys.argv[:-5]
                        out_nominglin(file_path,out_file,stop_txt_path)
                else:
                    if DIGUI:
                        if file_paths:
                            for file_path in file_paths:
                                include_many_minglin(file_path, out_file, stop_txt_path)
                        else:
                            print('未匹配到相关文件')
                    else:
                        file_path = sys.argv[-3]
                        if file_path == stop_txt_path:
                            file_path = sys.argv[:-5]
                        include_many_minglin(file_path, out_file, stop_txt_path)
            else:
                print('命令格式错误，"-o"后面应该紧挨结果输出的指定文件文件')
