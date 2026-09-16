from pathlib import Path
from .tdx_scanner import scan_vipdoc
from .tdx_reader import read_day_file


def run_check(vipdoc):
    stocks = scan_vipdoc(vipdoc)
    lines = [
        "Phase144-v1 通达信数据检测报告",
        "=" * 40,
        f"数据目录: {vipdoc}",
        f"股票文件数量: {len(stocks)}",
    ]
    for market in ("sh", "sz", "bj"):
        n = sum(1 for x in stocks if x["market"] == market)
        lines.append(f"{market.upper()} 文件数量: {n}")
    for item in stocks[:10]:
        try:
            data = read_day_file(item["file"])
            lines.append(f"{item['code']} 数据条数: {len(data)}")
            if data:
                lines.append(f"  日期范围: {data[0]['date']} ~ {data[-1]['date']}")
        except Exception as exc:
            lines.append(f"{item['code']} 读取失败: {exc}")

    out = Path("output") / "tdx_check_report.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))
    print(f"报告生成: {out}")
