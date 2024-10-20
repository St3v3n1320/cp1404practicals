color_codes_dict = {
    'AMBER': '#ffbf00', 'BEIGE': '#f5f5dc', 'CARDINAL': '#c41e3a', 'DENIM': '#1560bd',
    'EMERALD': '#50c878', 'FAWN': '#e5aa70', 'GOLD': '#ffd700', 'HONEYDEW': '#f0fff0',
    'ICEBERG': '#71a6d2', 'IRIS': '#5a4fcf'
}

color_name = input("Enter a color: ").upper()
while color_name != '':
    try:
        print(color_codes_dict[color_name])
    except KeyError:
        print("Color not found!")

    color_name = input("Enter a color: ").upper()