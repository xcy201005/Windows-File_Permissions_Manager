import base64

def base64_encode(data):
    """
    将字符串编码为 Base64 格式。

    参数:
        data (str): 待编码的字符串。

    返回:
        str: 编码后的 Base64 字符串。
    """
    return base64.b64encode(data.encode('utf-8')).decode('utf-8')

def base64_decode(encoded_data):
    """
    将 Base64 编码的字符串解码。

    参数:
        encoded_data (str): 编码的 Base64 字符串。

    返回:
        str: 解码后的字符串。
    """
    return base64.b64decode(encoded_data.encode('utf-8')).decode('utf-8')

def huoqu_base64_file(filename):
    """
    读取 Base64 编码的文件，并将其内容解码。

    参数:
        filename (str): 文件路径。

    返回:
        list: 解码后的字符串列表。
    """
    with open(filename, 'r') as file:
        # 过滤掉空字符串

        now_data = [base64_decode(line.strip()).strip() for line in file]
        now = [item for item in now_data if item]
    return now
