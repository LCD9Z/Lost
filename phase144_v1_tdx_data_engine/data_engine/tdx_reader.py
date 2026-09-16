import struct
from datetime import datetime

RECORD_SIZE = 32


def read_day_file(path):
    records = []
    with open(path, "rb") as f:
        while True:
            data = f.read(RECORD_SIZE)
            if len(data) < RECORD_SIZE:
                break
            date, o, h, l, c, amount, vol, _ = struct.unpack("<IIIIIfII", data)
            try:
                d = datetime.strptime(str(date), "%Y%m%d").date()
            except ValueError:
                continue
            records.append({
                "date": str(d),
                "open": o / 100.0,
                "high": h / 100.0,
                "low": l / 100.0,
                "close": c / 100.0,
                "amount": amount,
                "volume": vol,
            })
    return records
