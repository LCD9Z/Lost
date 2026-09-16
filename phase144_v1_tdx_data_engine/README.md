# Phase144-v1 TDX Data Engine

主数据源：本地通达信 `vipdoc` 日K `.day` 文件。

默认路径：`D:\new_tdx\vipdoc`

## 运行

在本目录打开命令行：

```text
python main.py
```

程序扫描：

- `vipdoc\sh\lday\*.day`
- `vipdoc\sz\lday\*.day`
- `vipdoc\bj\lday\*.day`

并生成 `output\tdx_check_report.txt`。

## 数据格式

读取固定 32 字节记录；价格字段按实际价格×100存储，读取时除以100。

## 项目路线

Phase144-v1：TDX本地数据引擎  
Phase144-v2：标准行情/SQLite数据层  
Phase144-v3：因子计算  
Phase144-v4：真实历史回测
