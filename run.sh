#!/bin/bash
# 调用生成HTML的Python脚本，一键生成并提交到GitHub

# 拉取最新的远程仓库内容
git pull
if [ $? -ne 0 ]; then
  echo "Git pull操作失败"
  exit 1
fi

# 运行Python脚本生成HTML
python3 gener.py
if [ $? -ne 0 ]; then
  echo "Python脚本执行失败"
  exit 1
fi

# 将文件添加到Git
git add *
if [ $? -ne 0 ]; then
  echo "Git add操作失败"
  exit 1
fi

# 提交更改
git commit -m "add imgs"
if [ $? -ne 0 ]; then
  echo "Git commit操作失败"
  exit 1
fi

# 推送到GitHub
git push
if [ $? -ne 0 ]; then
  echo "Git push操作失败"
  exit 1
fi

echo "更改成功推送到GitHub！"

