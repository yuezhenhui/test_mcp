# test_mcp

一个简单的Hello, World程序，用于MVP测试。同时包含一个功能强大的文件处理工具库。

## 功能

- 打印"Hello, World!"消息
- 文件读写工具库，支持多种格式：
  - 文本文件（TXT）
  - JSON文件
  - CSV文件
  - YAML文件

## 使用方法

### 运行Hello World程序

```bash
python main.py
```

### 使用文件工具库示例

```bash
python file_example.py
```

### 在自己的代码中使用文件工具库

```python
from file_utils import FileReader, FileWriter, FileUtils

# 读取文本文件
content = FileReader.read_text("example.txt")

# 写入JSON文件
data = {"name": "测试", "value": 123}
FileWriter.write_json("config.json", data)

# 列出目录中的文件
files = FileUtils.list_files("./data", extension=".csv")
```

## 安装依赖

```bash
pip install -r requirements.txt
```

## 项目结构

- `main.py`: Hello World主程序文件
- `file_utils.py`: 文件处理工具库
- `file_example.py`: 文件工具库使用示例
- `requirements.txt`: 项目依赖
- `README.md`: 项目说明文件