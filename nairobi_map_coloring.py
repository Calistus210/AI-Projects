from constraint import Problem

problem = Problem()

sub_counties = [
    'Westlands', 'Dagoretti North', 'Dagoretti South', 'Langata', 'Kibra',
    'Kamukunji', 'Starehe', 'Mathare', 'Makadara', 'Embakasi South',
    'Embakasi East', 'Embakasi West', 'Embakasi Central', 'Ruaraka',
    'Kasarani', 'Devesa', 'Roysambu'
]

adjacent = [
    ('Westlands', 'Dagoretti North'),
    ('Westlands', 'Dagoretti South'),
    ('Westlands', 'Starehe'),
    ('Westlands', 'Kamukunji'),
    ('Dagoretti North', 'Dagoretti South'),
    ('Dagoretti North', 'Starehe'),
    ('Dagoretti North', 'Mathare'),
    ('Dagoretti North', 'Kibra'),
    ('Dagoretti South', 'Langata'),
    ('Dagoretti South', 'Kibra'),
    ('Dagoretti South', 'Starehe'),
    ('Langata', 'Kibra'),
    ('Langata', 'Makadara'),
    ('Langata', 'Embakasi South'),
    ('Kibra', 'Kamukunji'),
    ('Kibra', 'Starehe'),
    ('Kibra', 'Makadara'),
    ('Kamukunji', 'Starehe'),
    ('Kamukunji', 'Mathare'),
    ('Kamukunji', 'Ruaraka'),
    ('Starehe', 'Mathare'),
    ('Starehe', 'Makadara'),
    ('Mathare', 'Makadara'),
    ('Mathare', 'Ruaraka'),
    ('Makadara', 'Embakasi South'),
    ('Makadara', 'Embakasi West'),
    ('Makadara', 'Embakasi Central'),
    ('Embakasi South', 'Embakasi West'),
    ('Embakasi South', 'Embakasi Central'),
    ('Embakasi West', 'Embakasi Central'),
    ('Embakasi West', 'Embakasi East'),
    ('Embakasi West', 'Kasarani'),
    ('Embakasi West', 'Ruaraka'),
    ('Embakasi Central', 'Embakasi East'),
    ('Embakasi Central', 'Kasarani'),
    ('Embakasi East', 'Kasarani'),
    ('Embakasi East', 'Roysambu'),
    ('Ruaraka', 'Kasarani'),
    ('Ruaraka', 'Roysambu'),
    ('Ruaraka', 'Devesa'),
    ('Kasarani', 'Roysambu'),
    ('Kasarani', 'Devesa'),
    ('Devesa', 'Roysambu'),
]

def find_min_colors(sub_counties, adjacent, max_colors=5):
    color_names = ['Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Orange']
    for num_colors in range(3, max_colors + 1):
        colors = color_names[:num_colors]
        problem = Problem()
        for sub_county in sub_counties:
            problem.addVariable(sub_county, colors)
        for r1, r2 in adjacent:
            problem.addConstraint(lambda a, b: a != b, (r1, r2))
        solution = problem.getSolution()
        if solution:
            return num_colors, solution
    return None, None

min_colors, solution = find_min_colors(sub_counties, adjacent)

if solution:
    print(f"Nairobi Sub-Counties Coloring Solution using {min_colors} colors:")
    for sub_county, color in sorted(solution.items()):
        print(f"{sub_county}: {color}")
else:
    print("No solution found with up to 5 colors.")