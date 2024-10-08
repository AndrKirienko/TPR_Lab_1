from prettytable import PrettyTable
import matplotlib.pyplot as plt

var = 7
step = 10

U_sh = [
    2.5,
    3.8,
    3.8,
    3.8,
    6.3,
    6.3,
    4.6,
    8.6,
    4.6,
    7.7,
    6.5,
    10.2,
    4.6,
    8.4,
    8.5,
    8.4,
    3.7,
    8.5,
    5.5,
    4.3,
    11.1,
    5.3,
    5.5,
    10.1,
    5.7,
    4.9,
    10.3,
    7.9,
    2.7,
    2.3,
    6.5,
    5.7,
    4.7,
    8.5,
    5.5,
    4.6,
    8.8,
    8.5,
    5.8,
    7.6,
    3.7,
    6.5,
    6.7,
    11.3,
    10.3,
    6.3,
    8.6,
    13.0,
    10.2,
    12.0,
    5.7,
    10.3,
    5.5,
    3.4,
    7.9,
    4.9,
    10.3,
    4.6,
    8.4,
    8.5,
]

a_10_3 = [
    0.07,
    0.07,
    0.09,
    0.15,
    0.15,
    0.18,
    0.1,
    0.28,
    0.15,
    0.23,
    0.22,
    0.27,
    0.18,
    0.26,
    0.27,
    0.18,
    0.05,
    0.28,
    0.1,
    0.08,
    0.3,
    0.08,
    0.15,
    0.24,
    0.15,
    0.17,
    0.27,
    0.24,
    0.06,
    0.05,
    0.18,
    0.12,
    0.2,
    0.22,
    0.11,
    0.11,
    0.3,
    0.27,
    0.16,
    0.22,
    0.04,
    0.17,
    0.18,
    0.31,
    0.29,
    0.16,
    0.31,
    0.34,
    0.26,
    0.35,
    0.17,
    0.3,
    0.1,
    0.03,
    0.24,
    0.18,
    0.28,
    0.09,
    0.27,
    0.29,
]

table = PrettyTable()
table.field_names = ["Trans", "U_sh", "a_10_3"]

max_length = max(len(U_sh), len(a_10_3))

for i in range(max_length):
    u_sh_value = U_sh[i] if i < len(U_sh) else ""
    a_10_3_value = a_10_3[i] if i < len(a_10_3) else ""
    table.add_row([i + 1, u_sh_value, a_10_3_value])

print("Початкові дані\n")
print(table)

####################################################
# Таблиця за варіантом

U_sh_var = [round(x * var, 1) for x in U_sh]

table_var = PrettyTable()
table_var.field_names = ["Trans", "U_sh_var", "a_10_3"]

max_length = max(len(U_sh_var), len(a_10_3))

for i in range(max_length):
    u_sh_value = U_sh_var[i] if i < len(U_sh_var) else ""
    a_10_3_value = a_10_3[i] if i < len(a_10_3) else ""
    table_var.add_row([i + 1, u_sh_value, a_10_3_value])

print("\n##################################################\n\nДані для варіанту\n")
print(table_var)

####################################################

u_sh_var_values = [row[1] for row in table_var.rows]

U_max = max(u_sh_var_values)
U_min = min(u_sh_var_values)


def round_to_nearest_10(num):
    return (num // 10) * 10 if num % 10 < 5 else (num // 10 + 1) * 10


U_max_rounded = round_to_nearest_10(U_max)
U_min_rounded = round_to_nearest_10(U_min)

####################################################
# створення таблиці для фінальних результатів


a_10_3_var = var / 100
U_sh_kl = var * 10

table_results_combined = PrettyTable()
table_results_combined.field_names = [
    "Крок",
    "n_K1_K1",
    "n_K2_K2",
    "n_K1_K2",
    "n_K2_K1",
    "n_roz_K1",
    "n_roz_K2",
    "r_K1_rK2",
    "r_K2_rK1",
    "r_rK1_K2",
    "r_rK2_K1",
    "r_roz_K1",
    "r_roz_K2",
    "r_pom",
    "r_virn",
]

####################################################
# Обробка для n_K1_K1  =  U_sh_var <= U_min and a_10_3 <= a_10_3_var

U_min = U_min_rounded
U_max = U_max_rounded


def find_elements_n_K1_K1(U_sh_var, a_10_3, U_min, a_10_3_var):
    selected_elements = []
    for i in range(len(U_sh_var)):
        if U_sh_var[i] <= U_min and a_10_3[i] <= a_10_3_var:
            selected_elements.append(U_sh_var[i])
    return selected_elements


n_K1_K1 = []
count_n_K1_K1 = {}

while U_min <= U_max:
    selected_elements = find_elements_n_K1_K1(U_sh_var, a_10_3, U_min, a_10_3_var)
    count_n_K1_K1[U_min] = len(selected_elements)
    if len(selected_elements) >= 4:
        n_K1_K1.extend(selected_elements)
    U_min += step

####################################################
# Обробка для n_K2_K2 = U_sh_var > U_min and a_10_3 > a_10_3_var

U_min = U_min_rounded
U_max = U_max_rounded


def find_elements_n_K2_K2(U_sh_var, a_10_3, U_min, a_10_3_var):
    selected_elements = []
    for i in range(len(U_sh_var)):
        if U_sh_var[i] > U_min and a_10_3[i] > a_10_3_var:
            selected_elements.append(U_sh_var[i])
    return selected_elements


n_K2_K2 = []
count_n_K2_K2 = {}

while U_min <= U_max_rounded:
    selected_elements = find_elements_n_K2_K2(U_sh_var, a_10_3, U_min, a_10_3_var)
    count_n_K2_K2[U_min] = len(selected_elements)
    if len(selected_elements) >= 4:
        n_K2_K2.extend(selected_elements)
    U_min += step

####################################################
# Обробка для n_K1_K2 = U_sh_var > U_min and a_10_3 <= a_10_3_var

U_min = U_min_rounded
U_max = U_max_rounded


def find_elements_n_K1_K2(U_sh_var, a_10_3, U_min, a_10_3_var):
    selected_elements = []
    for i in range(len(U_sh_var)):
        if U_sh_var[i] > U_min and a_10_3[i] <= a_10_3_var:
            selected_elements.append(U_sh_var[i])
    return selected_elements


n_K2_K2 = []
count_n_K1_K2 = {}

while U_min <= U_max_rounded:
    selected_elements = find_elements_n_K1_K2(U_sh_var, a_10_3, U_min, a_10_3_var)
    count_n_K1_K2[U_min] = len(selected_elements)
    if len(selected_elements) >= 4:
        n_K2_K2.extend(selected_elements)
    U_min += step

####################################################
# Обробка для n_K2_K1 = U_sh_var <= U_min and a_10_3 > a_10_3_var

U_min = U_min_rounded
U_max = U_max_rounded


def find_elements_n_K2_K1(U_sh_var, a_10_3, U_min, a_10_3_var):
    selected_elements = []
    for i in range(len(U_sh_var)):
        if U_sh_var[i] <= U_min and a_10_3[i] > a_10_3_var:
            selected_elements.append(U_sh_var[i])
    return selected_elements


n_K2_K1 = []
count_n_K2_K1 = {}

while U_min <= U_max_rounded:
    selected_elements = find_elements_n_K2_K1(U_sh_var, a_10_3, U_min, a_10_3_var)
    count_n_K2_K1[U_min] = len(selected_elements)
    if len(selected_elements) >= 4:
        n_K2_K1.extend(selected_elements)
    U_min += step

####################################################
# Обробка для n_roz_K1 = n_K1_K1 + n_K2_K1

n_roz_K1 = {}

all_keys = set(count_n_K1_K1.keys()).union(set(count_n_K2_K1.keys()))

for key in all_keys:
    value1 = count_n_K1_K1.get(key, 0)
    value2 = count_n_K2_K1.get(key, 0)
    n_roz_K1[key] = value1 + value2

####################################################
# Обробка для n_roz_K2 = n_K2_K2 + n_K1_K2

n_roz_K2 = {}

all_keys = set(count_n_K2_K2.keys()).union(set(count_n_K1_K2.keys()))

for key in all_keys:
    value1 = count_n_K2_K2.get(key, 0)
    value2 = count_n_K1_K2.get(key, 0)
    n_roz_K2[key] = value1 + value2

####################################################
# Обробка для n_K1 = n_K1_K1 + n_K1_K2

n_K1 = {}

all_keys = set(count_n_K1_K1.keys()).union(set(count_n_K1_K2.keys()))

for key in all_keys:
    value1 = count_n_K1_K1.get(key, 0)
    value2 = count_n_K1_K2.get(key, 0)
    n_K1[key] = value1 + value2

####################################################
# Обробка для n_K2 = n_K2_K2 + n_K2_K1

n_K2 = {}

all_keys = set(count_n_K2_K2.keys()).union(set(count_n_K2_K1.keys()))

for key in all_keys:
    value1 = count_n_K2_K2.get(key, 0)
    value2 = count_n_K2_K1.get(key, 0)
    n_K2[key] = value1 + value2

####################################################
# Обробка для r_K2_rK1 = n_K2_K1 / n_roz_K1

r_K2_rK1 = {}

all_keys = set(count_n_K2_K1.keys()).union(set(n_roz_K1.keys()))

for key in all_keys:
    value1 = count_n_K2_K1.get(key, 0)
    value2 = n_roz_K1.get(key, 0)
    if value2 != 0:
        r_K2_rK1[key] = round(value1 / value2, 2)  # Округление до сотых
    else:
        r_K2_rK1[key] = 0

####################################################
# Обробка для r_K1_rK2 = n_K1_K2 / n_roz_K2

r_K1_rK2 = {}

all_keys = set(count_n_K1_K2.keys()).union(set(n_roz_K2.keys()))

for key in all_keys:
    value1 = count_n_K1_K2.get(key, 0)
    value2 = n_roz_K2.get(key, 0)
    if value2 != 0:
        r_K1_rK2[key] = round(value1 / value2, 2)
    else:
        r_K1_rK2[key] = 0


####################################################
# Обробка для r_rK1_K2 = n_K2_K1 / n_K2

r_rK1_K2 = {}

all_keys = set(count_n_K2_K1.keys()).union(set(n_K2.keys()))

for key in all_keys:
    value1 = count_n_K2_K1.get(key, 0)
    value2 = n_K2.get(key, 0)
    if value2 != 0:
        r_rK1_K2[key] = round(value1 / value2, 2)
    else:
        r_rK1_K2[key] = 0

####################################################
# Обробка для r_rK2_K1 = n_K1_K2 / n_K1

r_rK2_K1 = {}

all_keys = set(count_n_K1_K2.keys()).union(set(n_K1.keys()))

for key in all_keys:
    value1 = count_n_K1_K2.get(key, 0)
    value2 = n_K1.get(key, 0)
    if value2 != 0:
        r_rK2_K1[key] = round(value1 / value2, 2)
    else:
        r_rK2_K1[key] = 0

####################################################
# Обробка для r_K1 = n_K1 / n

r_K1 = {}

all_keys = set(n_K1.keys()).union(set(n_K1.keys()))

for key in all_keys:
    value1 = n_K1.get(key, 0)
    value2 = len(U_sh)
    if value2 != 0:
        r_K1[key] = round(value1 / value2, 2)
    else:
        r_K1[key] = 0

####################################################
# Обробка для r_K2 = n_K2 / n

r_K2 = {}

all_keys = set(n_K2.keys()).union(set(n_K2.keys()))

for key in all_keys:
    value1 = n_K2.get(key, 0)
    value2 = len(U_sh)
    if value2 != 0:
        r_K2[key] = round(value1 / value2, 2)
    else:
        r_K2[key] = 0

####################################################
# Обробка для r_ros_K1 = n_roz_K1 / n

r_roz_K1 = {}

all_keys = set(n_roz_K1.keys()).union(set(n_roz_K1.keys()))

for key in all_keys:
    value1 = n_roz_K1.get(key, 0)
    value2 = len(U_sh)
    if value2 != 0:
        r_roz_K1[key] = round(value1 / value2, 2)
    else:
        r_roz_K1[key] = 0

####################################################
# Обробка для r_ros_K2 = n_roz_K2 / n

r_roz_K2 = {}

all_keys = set(n_roz_K2.keys()).union(set(n_roz_K2.keys()))

for key in all_keys:
    value1 = n_roz_K2.get(key, 0)
    value2 = len(U_sh)
    if value2 != 0:
        r_roz_K2[key] = round(value1 / value2, 2)
    else:
        r_roz_K2[key] = 0

####################################################
# Обробка для r_pom = n_K2_K1 + n_K1_K2 / n

r_pom = {}

all_keys = set(count_n_K2_K1.keys()).union(set(count_n_K1_K2.keys()))

for key in all_keys:
    value1 = count_n_K2_K1.get(key, 0) + count_n_K1_K2.get(key, 0)
    value2 = len(U_sh)
    if value2 != 0:
        r_pom[key] = round(value1 / value2, 2)
    else:
        r_pom[key] = 0

####################################################
# Обробка для r_virn = n_K1_K1 + n_K2_K2 / n

r_virn = {}

all_keys = set(count_n_K1_K1.keys()).union(set(count_n_K2_K2.keys()))

for key in all_keys:
    value1 = count_n_K1_K1.get(key, 0) + count_n_K2_K2.get(key, 0)
    value2 = len(U_sh)
    if value2 != 0:
        r_virn[key] = round(value1 / value2, 2)
    else:
        r_virn[key] = 0

####################################################
# Введення всіх даних в одну таблицю

for u_min in sorted(count_n_K1_K1.keys()):
    table_results_combined.add_row(
        [
            u_min,
            count_n_K1_K1[u_min],
            count_n_K2_K2.get(u_min, 0),
            count_n_K1_K2.get(u_min, 0),
            count_n_K2_K1.get(u_min, 0),
            n_roz_K1.get(u_min, 0),
            n_roz_K2.get(u_min, 0),
            r_K1_rK2.get(u_min, 0),
            r_K2_rK1.get(u_min, 0),
            r_rK1_K2.get(u_min, 0),
            r_rK2_K1.get(u_min, 0),
            r_roz_K1.get(u_min, 0),
            r_roz_K2.get(u_min, 0),
            r_pom.get(u_min, 0),
            r_virn.get(u_min, 0),
        ]
    )

print("\n\n###############################################\n\nФінальні результати\n\n")
print(table_results_combined)

####################################################
# Побудова графика кількості

u_min_values = list(count_n_K1_K1.keys())
count_n_K1_K1_values = list(count_n_K1_K1.values())
count_n_K2_K2_values = list(count_n_K2_K2.values())
count_n_K1_K2_values = list(count_n_K1_K2.values())
count_n_K2_K1_values = list(count_n_K2_K1.values())
n_roz_K1_values = list(dict(sorted(n_roz_K1.items())).values())
n_roz_K2_values = list(dict(sorted(n_roz_K2.items())).values())

plt.plot(u_min_values, count_n_K1_K1_values, label="n_K1_K1", marker="o", color="lightblue")
plt.plot(u_min_values, count_n_K2_K2_values, label="n_K2_K2", marker="o", color="orange")
plt.plot(u_min_values, count_n_K1_K2_values, label="n_K1_K2", marker="o", color="yellow")
plt.plot(u_min_values, count_n_K2_K1_values, label="n_K2_K1", marker="o", color="gray")
plt.plot(u_min_values, n_roz_K1_values, label="n_roz_K1", marker="o", color="blue")
plt.plot(u_min_values, n_roz_K2_values, label="n_roz_K2", marker="o", color="lightgreen", linestyle="--")

plt.title("Кількість", fontsize=15)
plt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.06), ncol=6, labelspacing=1.5, frameon=False, fontsize=15)
plt.grid(True)


plt.show()

####################################################
# Побудова графика кількості
r_K2_rK1_values = list(dict(sorted(r_K2_rK1.items())).values())
r_K1_rK2_values = list(dict(sorted(r_K1_rK2.items())).values())
r_rK1_K2_values = list(dict(sorted(r_rK1_K2.items())).values())
r_rK2_K1_values = list(dict(sorted(r_rK2_K1.items())).values())
r_roz_K1_values = list(dict(sorted(r_roz_K1.items())).values())
r_roz_K2_values = list(dict(sorted(r_roz_K2.items())).values())
r_pom_values = list(dict(sorted(r_pom.items())).values())
r_virn_values = list(dict(sorted(r_virn.items())).values())

plt.plot(u_min_values, r_K2_rK1_values, label="r_K2_rK1", marker="o", color="lightblue")
plt.plot(u_min_values, r_K1_rK2_values, label="r_K1_rK2", marker="o", color="orange")
plt.plot(u_min_values, r_rK1_K2_values, label="r_rK1_K2", marker="o", color="gray")
plt.plot(u_min_values, r_rK2_K1_values, label="r_rK2_K1", marker="o", color="yellow", linestyle="--")
plt.plot(u_min_values, r_roz_K1_values, label="r_roz_K1", marker="o", color="blue")
plt.plot(u_min_values, r_roz_K2_values, label="r_roz_K2", marker="o", color="lightgreen")
plt.plot(u_min_values, r_pom_values, label="r_pom", marker="o", color="darkblue")
plt.plot(u_min_values, r_virn_values, label="r_virn", marker="o", color="brown")

plt.title("Ймовірності", fontsize=15)
plt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.06), ncol=8, labelspacing=1.5, frameon=False, fontsize=15)
plt.grid(True)

plt.show()
