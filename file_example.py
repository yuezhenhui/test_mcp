#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
文件工具库使用示例
"""

import os
import json
from file_utils import FileReader, FileWriter, FileUtils

def main():
    """
    演示文件工具库的使用方法
    """
    print("文件工具库使用示例")
    print("-" * 50)
    
    # 创建示例目录
    example_dir = "examples"
    FileUtils.ensure_dir(example_dir)
    print(f"创建目录: {example_dir}")
    
    # 写入文本文件
    text_file = os.path.join(example_dir, "hello.txt")
    content = "Hello, World!\n这是一个示例文本文件。\n文件工具库测试。"
    FileWriter.write_text(text_file, content)
    print(f"写入文本文件: {text_file}")
    
    # 读取文本文件
    read_content = FileReader.read_text(text_file)
    print(f"读取文本文件内容:\n{read_content}")
    print("-" * 50)
    
    # 写入JSON文件
    json_file = os.path.join(example_dir, "config.json")
    json_data = {
        "name": "测试配置",
        "version": "1.0.0",
        "settings": {
            "debug": True,
            "log_level": "INFO",
            "max_retries": 3
        },
        "users": [
            {"id": 1, "name": "用户1"},
            {"id": 2, "name": "用户2"}
        ]
    }
    FileWriter.write_json(json_file, json_data)
    print(f"写入JSON文件: {json_file}")
    
    # 读取JSON文件
    read_json = FileReader.read_json(json_file)
    print(f"读取JSON文件内容:\n{json.dumps(read_json, ensure_ascii=False, indent=2)}")
    print("-" * 50)
    
    # 写入CSV文件
    csv_file = os.path.join(example_dir, "data.csv")
    csv_data = [
        {"id": "1", "name": "产品1", "price": "100.0"},
        {"id": "2", "name": "产品2", "price": "200.0"},
        {"id": "3", "name": "产品3", "price": "300.0"}
    ]
    FileWriter.write_csv(csv_file, csv_data)
    print(f"写入CSV文件: {csv_file}")
    
    # 读取CSV文件
    read_csv = FileReader.read_csv(csv_file)
    print(f"读取CSV文件内容:")
    for row in read_csv:
        print(f"  {row}")
    print("-" * 50)
    
    # 列出目录中的文件
    files = FileUtils.list_files(example_dir)
    print(f"目录 {example_dir} 中的文件:")
    for file in files:
        size = FileUtils.get_file_size(file)
        ext = FileUtils.get_file_extension(file)
        print(f"  {os.path.basename(file)} (大小: {size} 字节, 扩展名: {ext})")
    
    print("\n示例完成!")

if __name__ == "__main__":
    main()