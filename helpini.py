import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from os import remove, path

help_zifu = ""
help_liebiao = []

class helpA:
    """外部选择文件类"""

    def __init__(self, biao_z):
        # 全局参数"biao_z"
        self.biao_z = biao_z

    def select_folder(self):
        global help_zifu, help_liebiao
        folder_path = filedialog.askdirectory()
        if folder_path:
            print("选择了一个文件夹:", folder_path)
            # 判断是否为标准模式
            if self.biao_z:
                # 是就返回字符串
                help_zifu += folder_path + "\n\t"
            else:
                # 否则返回列表
                help_liebiao.append(folder_path)

    def select_file(self):
        global help_zifu
        file_path = filedialog.askopenfilename()
        if file_path:
            print("选择了一个文件:", file_path)
            if self.biao_z:
                # 是就返回字符串
                help_zifu += file_path + "\n\t"
            else:
                # 否则返回列表
                help_liebiao.append(file_path)

    def delete_file(self, file_path="C:/AppData/file.db"):
        "删除历史配置文件"
        if path.exists(file_path):
            try:
                remove(file_path)
                messagebox.showinfo("ok", " 您的历史记录已被清空")
            except Exception as e:
                messagebox.showerror("失败了", f"清空时发生了错误: {e}")
        else:
            messagebox.showinfo("失败了", f"您还没有文件历史记录哦！")

    def help_main(self):
        root = tk.Tk()
        root.title("文件选择器")
        window_width = 310
        window_height = 201

        if self.biao_z:
            qingk = True
            zi_1 = 13
            an_2 = 1
        else:
            qingk = False
            window_height = 158
            zi_1 = 13
            an_2 = 7

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        root.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

        root.configure(bg='lightblue')

        label = tk.Label(root, text="请选择一个文件夹或文件哦！", bg='lightblue', fg='#0066b8', relief="ridge", bd=2, font=("YouSheBiaoTiHei", zi_1), highlightcolor="lightblue")
        label.pack(pady=1)

        folder_button = tk.Button(root, text="选择文件夹", command=self.select_folder, width=12, height=1, bg='lightblue', fg='#0a84ff', font=("HYShangWeiShouShuW", 13))
        folder_button.pack(pady=11)

        file_button = tk.Button(root, text="选择文件", command=self.select_file, width=12, height=1, bg='lightblue', fg='#0a84ff', font=("HYShangWeiShouShuW", 13))
        file_button.pack(pady=an_2)

        file_button = tk.Button(root, text="清空文件记录", command=self.delete_file, width=12, bg='lightblue', fg='#0066b8', font=("HYShangWeiShouShuW", 13))
        if qingk:
            file_button.pack(pady=13)
        root.mainloop()

def huo_qu(biao_z=True):
    global help_zifu, help_liebiao
    help_zifu = ""
    help_liebiao = []
    obj = helpA(biao_z)
    obj.help_main()
    if biao_z:
        return help_zifu
    else:
        return help_liebiao
