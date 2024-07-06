import tkinter as tk
from tkinter.messagebox import showwarning #警告框

def d_wenben(shuju=None):
    if shuju is None: showwarning("加载错误 ！！", "路径信息并未正确读取出来，请检查路径信息是否正确！") ; return None
    root = tk.Tk()
    root.configure(bg='lightblue')  # 设置背景颜色为浅蓝色
    root.title("修改单个文件路径")
    
    initial_text = tk.StringVar(value=shuju)  # 初始文本为空

    # 创建 Entry 组件，设置高度为2行
    entry = tk.Entry(root, textvariable=initial_text, width=30, font=('Arial', 12), bd=2)
    entry.pack(padx=20, pady=(20, 18))  # 使用 pady=(20, 10) 调整上下间距

    def get_entry_text():
        text = entry.get()
        if text == "": showwarning("警告", "请输入内容再保存！")
        else:
            root.destroy()

    button = tk.Button(root, text="确认", command=get_entry_text, bg='lightblue', width=10, fg='#0a84ff', font=("YouSheBiaoTiHei", 16))
    button.pack(pady=10)
    
    # 获取屏幕宽度和高度
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # 计算窗口应该放置的位置
    window_width = 310  # 窗口宽度
    window_height = 133  # 窗口高度，适当增加以容纳两行高度的 Entry
    
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    
    # 设置窗口位置和大小
    root.geometry(f'{window_width}x{window_height}+{x}+{y}')

    root.mainloop()




