statesDic = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total = sum(statesDic.values())

percentagePerState = {state: (billing / total) *
                      100 for state, billing in statesDic.items()}

for state, percentage in percentagePerState.items():
    print(f'{state}: {percentage:.2f}')
