import tkinter as tk

def save_changes():
    global file_paths
    file_paths = text.get("1.0", "end-1c").splitlines()
    file_paths = [path for path in file_paths if path.strip() != ""]
    

def update_scrollbar(event=None):
    num_lines = text.get("1.0", "end-1c").count('\n') + 1  # 计算文本编辑框中的行数
    if num_lines > 15:  # 如果行数超过17行，则显示滚动条
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        Gaodu(610)
    else:
        scrollbar.pack_forget()  # 否则隐藏滚动条
        Gaodu()


def Gaodu(window_width = 580, window_height = 350):
    # 获取屏幕宽度和高度
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 设置窗口的宽度和高度
    window_width = window_width
    window_height = window_height

    # 计算窗口左上角坐标使其居中
    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)

    # 设置窗口的位置和大小
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
# 初始的 file_paths 列表
file_paths = ['C:/Windows', 'H:/FileHistory', 'C:/obly', 'H:/FiHistory']

# 创建主窗口
root = tk.Tk()
root.title("文件路径编辑器")
root.configure(bg='#87CEEB')  # 设置背景颜色为浅蓝色

Gaodu()

# 创建框架并放置文本编辑框和滚动条
frame = tk.Frame(root, width=85, height=20)
frame.pack(padx=0, pady=2)
# padx：设置组件左侧和右侧的外部填充（padding）空白像素数。
# pady：设置组件顶部和底部的外部填充（padding）空白像素数。

# 创建文本编辑框
text = tk.Text(frame, wrap="word", bg='#ADD8E6', font=("Arial", 13), width=60, height=15)
text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# 创建滚动条
scrollbar = tk.Scrollbar(frame, command=text.yview)
text.config(yscrollcommand=scrollbar.set)

# 将初始的 file_paths 列表内容加载到文本编辑框中
text.insert("1.0", "\n\n".join(file_paths))

# 初始时更新滚动条状态
update_scrollbar()

# 绑定文本编辑框内容变化时的事件，更新滚动条状态
text.bind("<KeyRelease>", update_scrollbar)

# 创建保存按钮
save_button = tk.Button(root, text="保存更改", command=save_changes, bg='lightblue', width=12, fg='#0a84ff', font=("YouSheBiaoTiHei", 14))
save_button.pack()

# 运行主循环
root.mainloop()
