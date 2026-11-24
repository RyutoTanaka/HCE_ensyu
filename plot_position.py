from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt

import numpy as np

import pandas as pd


kp133_csv_file = Path(__file__).parent / "data/L15_M268_P133_lift_and_drop.csv"
kp200_csv_file = Path(__file__).parent / "data/L15_M268_P200_lift_and_drop.csv"
kp400_csv_file = Path(__file__).parent / "data/L15_M268_P400_lift_and_drop.csv"
kp800_csv_file = Path(__file__).parent / "data/L15_M268_P800_lift_and_drop.csv"

output_dir = Path(__file__).parent / "outputs"
output_dir.mkdir(exist_ok=True)

#データの読み出し
kp133_position = pd.read_csv(kp133_csv_file, encoding="utf-8-sig")["position"].to_numpy()
kp200_position = pd.read_csv(kp200_csv_file, encoding="utf-8-sig")["position"].to_numpy()
kp400_position = pd.read_csv(kp400_csv_file, encoding="utf-8-sig")["position"].to_numpy()
kp800_position = pd.read_csv(kp800_csv_file, encoding="utf-8-sig")["position"].to_numpy()

# print(position)

# 描画処理
plt.plot(kp133_position,label="kp133")
plt.plot(kp200_position,label="kp200")
plt.plot(kp400_position,label="kp400")
plt.plot(kp800_position,label="kp800")

plt.title("L15_M268_lift_and_drop.csv")
plt.xlabel("Sample")
plt.ylabel("Position")
plt.legend()
plt.grid()

plt.show()

plt.savefig(output_dir / f"{"L15_M268_lift_and_drop.csv"}.png")
plt.close()
