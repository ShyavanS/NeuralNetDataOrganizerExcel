import pandas as pd

file = input("Enter the name of the excel file to be organized: ")

stdin = pd.read_excel(f"{file}.xlsx", header=[1])

num_dfs = len(stdin.columns) // 2

data = pd.DataFrame()

edge_ls = [1 if j < 10 else 0 for i in range(20) for j in range(50)]
start_ls = [1 if 9 < j < 30 else 0 for i in range(20) for j in range(50)]
end_ls = [1 if j > 29 else 0 for i in range(20) for j in range(50)]
pH_ls = [7 if not (j % 2) else 10 if j == 1 else 3 if j ==
         3 else None for i in range(5) for j in range(4) for k in range(50)]

for i in range(0, len(stdin.columns), 2):
    run = stdin.iloc[1:, i + 1:i + 2]
    
    run.columns.values[0] = "Voltage"

    run = run.assign(Edge=edge_ls)
    run = run.assign(Start=start_ls)
    run = run.assign(End=end_ls)
    run = run.assign(pH=pH_ls)

    data = data.append(run)

data = data.reset_index(drop=True)

print(data)

data.to_excel(f"{file}_organized.xlsx", index=False)
