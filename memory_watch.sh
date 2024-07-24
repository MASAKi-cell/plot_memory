#!/bin/bash

# 出力ファイルの設定
output_file="memory_usage.log"

# 初期化: ファイルが存在する場合は削除
if [ -f "$output_file" ]; then
  rm "$output_file"
fi

# 定期実行ループ
while true
do
  # メモリ使用量を取得してファイルに追記
  echo "$(date +%s),$(node -e 'console.log(process.memoryUsage().heapUsed)')" >> "$output_file"
  
  # 1秒待つ
  sleep 1
done
