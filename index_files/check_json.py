import json
import os

# 设置JSON文件路径（根据实际情况修改）
json_file_path = "全年龄段合并数据.json"

try:
    # 检查文件是否存在
    if not os.path.exists(json_file_path):
        print(f"错误：文件 '{json_file_path}' 不存在")
        print(f"当前工作目录：{os.getcwd()}")
        print(f"目录中的文件：{os.listdir('.')}")
    else:
        print(f"找到文件：{json_file_path}")
        print(f"文件大小：{os.path.getsize(json_file_path)} 字节")
        
        # 读取并解析JSON
        with open(json_file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        print("✅ JSON文件解析成功！")
        print(f"数据类型：{type(data)}")
        
        # 显示一些基本信息
        if isinstance(data, dict):
            print(f"包含的键数量：{len(data)}")
            print("前10个键：", list(data.keys())[:10])
            
            # 检查样本数据
            sample_key = list(data.keys())[0] if data else "无数据"
            if sample_key in data:
                sample = data[sample_key]
                print(f"\n样本数据 '{sample_key}':")
                for key, value in sample.items():
                    if key != "benefit_data":  # 避免打印大量数据
                        print(f"  {key}: {value}")
        
except json.JSONDecodeError as e:
    print(f"❌ JSON解析错误：{e}")
    print("可能的原因：文件格式不正确、缺少引号、括号不匹配等")
    
except UnicodeDecodeError as e:
    print(f"❌ 编码错误：{e}")
    print("尝试使用其他编码...")
    try:
        with open(json_file_path, "r", encoding="gbk") as f:
            data = json.load(f)
        print("✅ 使用GBK编码解析成功！")
    except Exception as e2:
        print(f"GBK编码也失败：{e2}")
    
except Exception as e:
    print(f"❌ 其他错误：{e}")

print("\n按Enter键退出...")
input()