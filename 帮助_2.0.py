import os
from subprocess import run,DEVNULL
from termcolor import colored  # 用于终端字符颜色
import helpini as wai
import base as jiakey

# 清理屏幕输出
def clear():
    os.system('cls')

# 全局变量
init = 0
jilu_file = ""
content = ""

# 定义文件路径
file_path = r"C:/AppData/file.db"

def adminceshi():
    print("当前历史记录数据(无论如何都为空)", jilu_file)
    print("当前文件记录数据", content)

class Lishi:
    """历史记录类"""

    def jiance(hou_tai=False):
        global content
        wen_jian = True
        # 初始化配置文件，采用 os 库
        if not os.path.exists(file_path):
            open(file_path, "w").close()
            wen_jian = False
        
        # 逐行读取文件内容
        yes = jiakey.huoqu_base64_file(file_path)
        yes.sort()

        if wen_jian :
            # 如果是普通模式，展示路径
            if hou_tai == False:
                print("展示模式：",yes)
                yesr = ""
                for line in yes:
                    yesr += line + "\n\t"
                print("您所浏览过的文件或文件夹：")
                print("\t"+yesr, end="")
            else:
                # 检测是否为后台读取模式
                print("读取模式：",yes)
                content = yes
        else:
            print("欢迎新用户！")

    def lishi():
        global jilu_file
        # 让用户选择文件夹，调用文件wai库
        jilu_file = wai.huo_qu()
        print("\t"+jilu_file)
        # 将获取的路径数据写入文件
        with open(file_path, "a") as file:
            jilu = [jilu_file]
            bese64_text = ''.join(jilu)
            # 对文件进行加密
            jiami = "\n" + jiakey.base64_encode(bese64_text)
            file.write(jiami)
        
        print("添加成功！")
        Lishi.jiance(hou_tai=True)
        jilu_file = ""

class Wenjian:
    """文件夹 类"""

    def execute_cmd_silently(cmd):
        """可以执行带有空格命令的cmd，但不显示输出"""
        # 使用subprocess模块执行命令
        run(cmd, stdout=DEVNULL, stderr=DEVNULL, shell=True)
        # , stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True

    def is_file_hidden(file_path):
        "检查文件是否隐藏成功"
        try:
            return bool(os.stat(file_path).st_file_attributes & 2)
        except FileNotFoundError:
            pass
        except ArithmeticError:
            pass
    
    def noget():
        "隐藏文件"
        wi_data = wai.huo_qu(biao_z=False)
        jeigo = ""
        for wia in wi_data:
            wi = r"{}".format(wia)
            cmd = ['attrib', '+s', '+a', '+h', '+r', wi]  # 隐藏命令，可以有空格
            Wenjian.execute_cmd_silently(cmd)

            if Wenjian.is_file_hidden(wi):      
                jeigo += f"\n- 隐藏成功！ 文件: {wi}"
            else:
                jeigo += f"\n- 路劲错误！ 文件: {wi}"
        input("\n执行完成！")
        clear()

    def yesget():
        "显示文件"
        wi_data = wai.huo_qu(biao_z=False)
        wi = r"{}".format(wi_data)
        os.system(f"attrib -a -s -h -r {wi}")

        if Wenjian.is_file_hidden(wi):      
            input(f"\n显示成功！ 文件: {wi}")
        else:
            input("请再检查下路径...")
        clear()

    def wenmain():
        "文件类主页"
        print(colored("\n( 1.文件夹_类 ): ", "light_blue"))
        print("""
        1.隐藏文件夹
              
        2.显示文件夹
              
        3.管理文件历史记录
              
        4.测试""")

        a1 = input("\n<: ")
        if a1 == "1":
            Wenjian.noget()
        elif a1 == "2":
            Wenjian.yesget()
        elif a1 == "3":
            Lishi.lishi()
        elif a1 == "4":
            adminceshi()
        else:
            print(colored("无效选择，请重新输入。", "red"))

# 程序打开时检查是否有配置文件
Lishi.jiance()

while True:
    # 清空屏幕内容
    if init == 1:
        clear()
        init += 1

    print(colored("\n主页 >", "blue"))
    print("""  
    欢迎来到帮助工具 有什么可以帮你？       
        1.文件夹 类  2.cmd 类""")
    
    user = input("\n(: ")
    new_user = user.replace(" ", "")
    clear()

    if new_user == "1":
        Wenjian.wenmain()
    elif new_user == "2":
        print("cmd 类功能尚未实现")  # 这里可以添加 cmd 类的相关功能
    else:
        print(colored("无效选择，请重新输入。", "red"))
