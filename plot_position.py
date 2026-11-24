from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt

import numpy as np

import pandas as pd


csv_file = Path(__file__).parent / "data/L15_M268_P133_lift_and_drop.csv"
output_dir = Path(__file__).parent / "outputs"
output_dir.mkdir(exist_ok=True)

#データの読み出し
velocity = pd.read_csv(csv_file, encoding="utf-8-sig")["speed"].to_numpy()
acceleration = np.gradient(velocity, 1/50, axis=0)

print(acceleration)

# 描画処理
plt.plot(acceleration)
plt.title(csv_file.stem)
plt.xlabel("Sample")
plt.ylabel("acceleration")
plt.grid()

plt.show()

plt.savefig(output_dir / f"{csv_file.stem}.png")
plt.close()
