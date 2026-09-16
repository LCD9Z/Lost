from pathlib import Path


def scan_vipdoc(vipdoc):
    root = Path(vipdoc)
    result = []
    for market in ("sh", "sz", "bj"):
        folder = root / market / "lday"
        if not folder.exists():
            continue
        for path in folder.glob("*.day"):
            result.append({"market": market, "file": str(path), "code": path.stem})
    return result
