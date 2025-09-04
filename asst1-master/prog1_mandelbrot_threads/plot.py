import matplotlib.pyplot as plt

# 读取数据
x = []
y = []
with open("log.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line:  # 跳过空行
            parts = line.split(",")
            x.append(int(parts[0].strip()))
            y.append(float(parts[1].strip()))

# 绘图
plt.figure(figsize=(8, 5))
plt.plot(x, y, marker='o', linestyle='-', linewidth=2, label="log data")
plt.title("Data from log.txt")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.legend()

# 保存图片（在 show 之前）
plt.savefig("output.png", dpi=300)  # 可以改成 jpg/pdf/svg 等格式
plt.show()
