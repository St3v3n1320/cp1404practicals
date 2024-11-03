def read_wimbledon_data(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()
        data = [line.strip().split(',') for line in lines[1:]]
    return data


def count_champions(data):
    champion_counts = {}
    for row in data:
        country = row[2].strip()
        if country in champion_counts:
            champion_counts[country] += 1
        else:
            champion_counts[country] = 1
    return champion_counts


def extract_champions(data):
    champions = {row[1].strip() for row in data}
    return sorted(champions)


def main():
    filename = "wimbledon.csv"
    data = read_wimbledon_data(filename)
    champion_counts = count_champions(data)
    champions = extract_champions(data)

    print("Wimbledon Champions:")
    for country, count in sorted(champion_counts.items()):
        print(f"{country} {count}")

    print("\nThese {} champions have won Wimbledon:".format(len(champions)))
    print(", ".join(champions))


main()