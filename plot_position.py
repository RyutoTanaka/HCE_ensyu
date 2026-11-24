from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt

import numpy as np

import pandas as pd

# 振り子の物理定数
l = 0.15
m = 0.268
g = 9.81

# 入出力ファイルの設定
csv_file = Path(__file__).parent / "data/L15_M268_P133_lift_and_drop.csv"
output_dir = Path(__file__).parent / "outputs"
output_dir.mkdir(exist_ok=True)

#データの読み出し
position = pd.read_csv(csv_file, encoding="utf-8-sig")["position"].to_numpy()
velocity = pd.read_csv(csv_file, encoding="utf-8-sig")["speed"].to_numpy()

acceleration = np.gradient(velocity, 1/200, axis=0)

tau = m*l**2*acceleration + m*l*g*np.sin(position)

print(acceleration)

# 描画処理
plt.plot(tau)
plt.title(csv_file.stem)
plt.xlabel("Sample")
plt.ylabel("tau")
plt.grid()

plt.show()

plt.savefig(output_dir / f"{csv_file.stem}.png")
plt.close()
