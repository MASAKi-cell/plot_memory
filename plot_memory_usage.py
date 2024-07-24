import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import pytz

# ログファイルを読み込む
log_file = "memory_usage.log"
data = pd.read_csv(log_file, header=None, names=["timestamp", "heapUsed"])

# タイムスタンプを変換し、JSTに設定
data["timestamp"] = pd.to_datetime(data["timestamp"], unit='s')
jst = pytz.timezone('Asia/Tokyo')
data["timestamp"] = data["timestamp"].dt.tz_localize('UTC').dt.tz_convert(jst)

# グラフを作成
plt.figure(figsize=(10, 5))
plt.plot(data["timestamp"], data["heapUsed"], label="Heap Used (bytes)")

# グラフの装飾
plt.xlabel("Time (JST)")
plt.ylabel("Heap Used (bytes)")
plt.title("Memory Usage Over Time (JST)")
plt.legend()
plt.grid(True)

# グラフを表示
plt.show()
