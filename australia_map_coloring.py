from constraint import Problem
problem = Problem()

regions = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
colors = ['Red', 'Green', 'Blue']
for region in regions:
    problem.addVariable(region, colors)

adjacent = [
    ('WA', 'NT'),
    ('WA', 'SA'),
    ('NT', 'SA'),
    ('SA', 'Q'),
    ('SA', 'NSW'),
    ('SA', 'V'),
    ('Q', 'NSW'),
    ('NSW', 'V')
]

for r1, r2 in adjacent:
    problem.addConstraint(lambda a, b: a != b, (r1, r2))
solution = problem.getSolution()

if solution:
    print("Australia Map Coloring Solution:")
    for region, color in solution.items():
        print(f"{region}: {color}")
else:
    print("No solution found.")