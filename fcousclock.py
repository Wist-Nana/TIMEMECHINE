import time

# 设置专注时间（以秒为单位）
focus_time = 25 * 60 

# 暂停时间（以秒为单位）
rest_time = 5 * 60 

# 开始计时并输出当前时间
start_time = time.time()
print("开始专注:", time.strftime('%H:%M:%S', time.localtime(start_time)))

# 循环直到专注时间结束
while time.time() - start_time < focus_time:
    time.sleep(1)

# 输出休息提示
print("休息一下！")

# 开始休息时间并输出当前时间
start_time = time.time()
print("开始休息:", time.strftime('%H:%M:%S', time.localtime(start_time)))

# 循环直到休息时间结束
while time.time() - start_time < rest_time:
    time.sleep(1)

# 输出完成提示
print("任务完成！")
