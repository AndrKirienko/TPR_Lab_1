from prettytable import PrettyTable
import matplotlib.pyplot as plt

Mx = 5.0
My = 10.0
Dx = 0.5
Dy = 1.0
R1 = -0.5
R2 = -0.8
X1 = 6.5
X2 = 6.0
X3 = 5.0
X4 = 4.0

# оголошення таблиці
table_results_combined = PrettyTable()
table_results_combined.field_names = ["Test"]

for u_min in sorted(My.keys()):
    table_results_combined.add_row([MyResults])

# Побудова графика кількості

firstValues = list(first.keys())
secondValues = list(second.values())


plt.plot(firstValues, secondValues, label="n_K1_K1", marker="o", color="lightblue")


plt.title("Кількість", fontsize=15)
plt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.06), ncol=6, labelspacing=1.5, frameon=False, fontsize=15)
plt.grid(True)


plt.show()
