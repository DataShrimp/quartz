#!/bin/bash
cd /home/ryan/ai-company/quartz

echo "🔄 正在拉取最新文章..."
git pull origin v4

echo "🚀 正在重建网站..."
# 因为 Quartz 是热重载的，理论上只要文件变了它会自动更新
# 但为了保险（比如改了配置文件），我们重启容器
#cd ..
#docker compose restart quartz

echo "✅ 更新完成！"