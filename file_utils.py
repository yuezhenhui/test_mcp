#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
文件处理工具库
提供各种文件读取、写入和处理功能
"""

import os
import json
import csv
import yaml
from typing import Dict, List, Any, Union, Optional, TextIO


class FileReader:
    """文件读取工具类，支持多种格式的文件读取"""
    
    @staticmethod
    def read_text(file_path: str, encoding: str = 'utf-8') -> str:
        """
        读取文本文件内容
        
        Args:
            file_path: 文件路径
            encoding: 文件编码，默认为utf-8
            
        Returns:
            文件内容字符串
            
        Raises:
            FileNotFoundError: 文件不存在
            IOError: 读取文件失败
        """
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                return f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"文件不存在: {file_path}")
        except IOError as e:
            raise IOError(f"读取文件失败: {str(e)}")
    
    @staticmethod
    def read_lines(file_path: str, encoding: str = 'utf-8') -> List[str]:
        """
        按行读取文本文件内容
        
        Args:
            file_path: 文件路径
            encoding: 文件编码，默认为utf-8
            
        Returns:
            文件内容行列表
            
        Raises:
            FileNotFoundError: 文件不存在
            IOError: 读取文件失败
        """
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                return f.readlines()
        except FileNotFoundError:
            raise FileNotFoundError(f"文件不存在: {file_path}")
        except IOError as e:
            raise IOError(f"读取文件失败: {str(e)}")
    
    @staticmethod
    def read_json(file_path: str, encoding: str = 'utf-8') -> Dict[str, Any]:
        """
        读取JSON文件内容
        
        Args:
            file_path: 文件路径
            encoding: 文件编码，默认为utf-8
            
        Returns:
            JSON解析后的字典对象
            
        Raises:
            FileNotFoundError: 文件不存在
            json.JSONDecodeError: JSON解析失败
            IOError: 读取文件失败
        """
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"文件不存在: {file_path}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"JSON解析失败: {str(e)}", e.doc, e.pos)
        except IOError as e:
            raise IOError(f"读取文件失败: {str(e)}")
    
    @staticmethod
    def read_csv(file_path: str, delimiter: str = ',', encoding: str = 'utf-8') -> List[Dict[str, str]]:
        """
        读取CSV文件内容
        
        Args:
            file_path: 文件路径
            delimiter: 分隔符，默认为逗号
            encoding: 文件编码，默认为utf-8
            
        Returns:
            CSV解析后的字典列表，每行对应一个字典
            
        Raises:
            FileNotFoundError: 文件不存在
            IOError: 读取文件失败
        """
        try:
            result = []
            with open(file_path, 'r', encoding=encoding, newline='') as f:
                reader = csv.DictReader(f, delimiter=delimiter)
                for row in reader:
                    result.append(row)
            return result
        except FileNotFoundError:
            raise FileNotFoundError(f"文件不存在: {file_path}")
        except IOError as e:
            raise IOError(f"读取文件失败: {str(e)}")
    
    @staticmethod
    def read_yaml(file_path: str, encoding: str = 'utf-8') -> Dict[str, Any]:
        """
        读取YAML文件内容
        
        Args:
            file_path: 文件路径
            encoding: 文件编码，默认为utf-8
            
        Returns:
            YAML解析后的字典对象
            
        Raises:
            FileNotFoundError: 文件不存在
            yaml.YAMLError: YAML解析失败
            IOError: 读取文件失败
        """
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"文件不存在: {file_path}")
        except yaml.YAMLError as e:
            raise yaml.YAMLError(f"YAML解析失败: {str(e)}")
        except IOError as e:
            raise IOError(f"读取文件失败: {str(e)}")


class FileWriter:
    """文件写入工具类，支持多种格式的文件写入"""
    
    @staticmethod
    def write_text(file_path: str, content: str, encoding: str = 'utf-8', mode: str = 'w') -> None:
        """
        写入文本文件
        
        Args:
            file_path: 文件路径
            content: 要写入的内容
            encoding: 文件编码，默认为utf-8
            mode: 写入模式，'w'为覆盖，'a'为追加，默认为'w'
            
        Raises:
            IOError: 写入文件失败
        """
        try:
            with open(file_path, mode, encoding=encoding) as f:
                f.write(content)
        except IOError as e:
            raise IOError(f"写入文件失败: {str(e)}")
    
    @staticmethod
    def write_lines(file_path: str, lines: List[str], encoding: str = 'utf-8', mode: str = 'w') -> None:
        """
        按行写入文本文件
        
        Args:
            file_path: 文件路径
            lines: 要写入的行列表
            encoding: 文件编码，默认为utf-8
            mode: 写入模式，'w'为覆盖，'a'为追加，默认为'w'
            
        Raises:
            IOError: 写入文件失败
        """
        try:
            with open(file_path, mode, encoding=encoding) as f:
                f.writelines(lines)
        except IOError as e:
            raise IOError(f"写入文件失败: {str(e)}")
    
    @staticmethod
    def write_json(file_path: str, data: Dict[str, Any], encoding: str = 'utf-8', indent: int = 4) -> None:
        """
        写入JSON文件
        
        Args:
            file_path: 文件路径
            data: 要写入的数据字典
            encoding: 文件编码，默认为utf-8
            indent: 缩进空格数，默认为4
            
        Raises:
            IOError: 写入文件失败
        """
        try:
            with open(file_path, 'w', encoding=encoding) as f:
                json.dump(data, f, ensure_ascii=False, indent=indent)
        except IOError as e:
            raise IOError(f"写入文件失败: {str(e)}")
    
    @staticmethod
    def write_csv(file_path: str, data: List[Dict[str, str]], fieldnames: Optional[List[str]] = None, 
                 delimiter: str = ',', encoding: str = 'utf-8') -> None:
        """
        写入CSV文件
        
        Args:
            file_path: 文件路径
            data: 要写入的数据列表，每个元素为一行的字典
            fieldnames: 字段名列表，如果为None则使用data[0]的键
            delimiter: 分隔符，默认为逗号
            encoding: 文件编码，默认为utf-8
            
        Raises:
            IOError: 写入文件失败
            ValueError: 数据为空或字段名为空
        """
        if not data:
            raise ValueError("数据不能为空")
        
        if fieldnames is None and data:
            fieldnames = list(data[0].keys())
        
        if not fieldnames:
            raise ValueError("字段名不能为空")
        
        try:
            with open(file_path, 'w', encoding=encoding, newline='') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=delimiter)
                writer.writeheader()
                writer.writerows(data)
        except IOError as e:
            raise IOError(f"写入文件失败: {str(e)}")
    
    @staticmethod
    def write_yaml(file_path: str, data: Dict[str, Any], encoding: str = 'utf-8') -> None:
        """
        写入YAML文件
        
        Args:
            file_path: 文件路径
            data: 要写入的数据字典
            encoding: 文件编码，默认为utf-8
            
        Raises:
            IOError: 写入文件失败
        """
        try:
            with open(file_path, 'w', encoding=encoding) as f:
                yaml.dump(data, f, allow_unicode=True, default_flow_style=False)
        except IOError as e:
            raise IOError(f"写入文件失败: {str(e)}")


class FileUtils:
    """文件工具类，提供文件操作的实用方法"""
    
    @staticmethod
    def ensure_dir(directory: str) -> None:
        """
        确保目录存在，如果不存在则创建
        
        Args:
            directory: 目录路径
            
        Raises:
            IOError: 创建目录失败
        """
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
            except IOError as e:
                raise IOError(f"创建目录失败: {str(e)}")
    
    @staticmethod
    def list_files(directory: str, extension: Optional[str] = None) -> List[str]:
        """
        列出目录中的文件
        
        Args:
            directory: 目录路径
            extension: 文件扩展名过滤，如'.txt'，默认为None表示不过滤
            
        Returns:
            文件路径列表
            
        Raises:
            FileNotFoundError: 目录不存在
        """
        if not os.path.exists(directory):
            raise FileNotFoundError(f"目录不存在: {directory}")
        
        files = []
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                if extension is None or file.endswith(extension):
                    files.append(file_path)
        return files
    
    @staticmethod
    def file_exists(file_path: str) -> bool:
        """
        检查文件是否存在
        
        Args:
            file_path: 文件路径
            
        Returns:
            文件是否存在
        """
        return os.path.isfile(file_path)
    
    @staticmethod
    def get_file_size(file_path: str) -> int:
        """
        获取文件大小（字节）
        
        Args:
            file_path: 文件路径
            
        Returns:
            文件大小（字节）
            
        Raises:
            FileNotFoundError: 文件不存在
        """
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"文件不存在: {file_path}")
        
        return os.path.getsize(file_path)
    
    @staticmethod
    def get_file_extension(file_path: str) -> str:
        """
        获取文件扩展名
        
        Args:
            file_path: 文件路径
            
        Returns:
            文件扩展名（包含点，如'.txt'）
        """
        return os.path.splitext(file_path)[1]


# 示例用法
if __name__ == "__main__":
    # 创建测试文件
    test_dir = "test_files"
    FileUtils.ensure_dir(test_dir)
    
    # 写入文本文件
    text_file = os.path.join(test_dir, "sample.txt")
    FileWriter.write_text(text_file, "Hello, World!\nThis is a test file.")
    
    # 读取文本文件
    content = FileReader.read_text(text_file)
    print(f"Text file content: {content}")
    
    # 写入JSON文件
    json_file = os.path.join(test_dir, "sample.json")
    data = {"name": "Test", "value": 123, "items": ["a", "b", "c"]}
    FileWriter.write_json(json_file, data)
    
    # 读取JSON文件
    json_data = FileReader.read_json(json_file)
    print(f"JSON file content: {json_data}")
    
    # 列出目录中的文件
    files = FileUtils.list_files(test_dir)
    print(f"Files in directory: {files}")