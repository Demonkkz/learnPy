import os
from tkinter import *
from tkinter import filedialog as ft
from tkinter import messagebox as tmb
from  Tkinter_test import *

root = Tk()
root.title('Notepad')
root.resizable(0, 0)  # 窗口大小不可变
root.geometry('450x300')

menu_bar = Menu(root)

content_text = Text(root, wrap='word')
content_text.pack(expand='yes', fill='both')
content_text.tag_configure('active_line', background='#f1f1f1')

scroll_bar = Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=content_text.yview)
scroll_bar.pack(side='right', fill='y')

def new_text(event=None):
    root.title('Untitled')
    global file_name
    file_name = None


def save_as(event=None):
    t = content_text.get('1.0', 'end-1c')
    save_location = ft.askopenfilename(defaultextension='.txt', filetypes=[('所有文件', '*.*'), ('文本文件', '*.txt*')])
    file1 = open(save_location, 'w+')
    file1.write(t)
    global file_name
    file_name = save_location
    root.title('{} - {}'.format(os.path.basename(save_location), 'Notepad'))
    file1.close()


def save(event=None):
    global file_name
    if not file_name:
        save_as()
    else:
        t = content_text.get('1.0', 'end-1c')
        file1 = open(file_name, 'w+')
        file1.write(t)
    return 'break'


def open(event=None):
    input_file_name = ft.askopenfilename(defaultextension='.txt', filetypes=[('所有文件', '*.*'), ('文本文件', '*.txt*')])
    if input_file_name:
        global file_name
        file_name = input_file_name
        root.title('{} - {}'.format(os.path.basename(file_name), 'Notepad'))
        content_text.delete(1.0, END)
        file = open(input_file_name, 'r')
        if file != '':
            try:
                txt = file.read()
            except:
                tmb.showwarning('Invalid', 'Please select a valid file to open')
            content_text.insert(INSERT, txt)
        else:
            pass


def selectALL():
    content_text.event_generate('<<SelectALL>>')


file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='文件', menu=file_menu)

file_menu.add_command(label='新建', compound='left', accelerator='Ctrl+N', underline=0)
file_menu.add_command(label='打开', compound='left', accelerator='Ctrl+O', underline=0)
file_menu.add_separator()
file_menu.add_command(label='保存', compound='left', accelerator='Ctrl+S', underline=0)
file_menu.add_command(label='另存为…', compound='left', accelerator='Ctrl+Shift+S', underline=1)
file_menu.add_command(label='重命名', compound='left', accelerator='Ctrl+Shift+R', underline=0)
file_menu.add_separator()
file_menu.add_command(label='关闭', compound='left', accelerator='Alt+F4', underline=0)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='编辑', menu=edit_menu)
edit_menu.add_command(label='返回')
edit_menu.add_command(label='重做')
edit_menu.add_command(label='剪切', accelerator='Ctrl+X')
edit_menu.add_command(label='复制', accelerator='Ctrl+C')
edit_menu.add_command(label='粘贴', accelerator='Ctrl+V')
edit_menu.add_command(label='删除', accelerator='del')
edit_menu.add_command(label='选定所有', accelerator='Ctrl+A', command=selectALL)
edit_menu.add_command(label='查找', accelerator='Ctrl+F')


view_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='视图', menu=view_menu)

about_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='关于', menu=about_menu)
about_menu.add_command(label='关于我')

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='帮助', menu=help_menu)
help_menu.add_command(label='帮助索引')
help_menu.add_command(label='许可')

root.config(menu=menu_bar)

root.mainloop()

