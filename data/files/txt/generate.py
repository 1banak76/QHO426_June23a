def search(f_name):
    print("Searching...")
    data = {}

    with open(f_name) as f:
        section = ''
        for line in f:
            if line.startswith("Section"):
                section = line.strip().split(":")[1]
                data[section] = []
            else:
                data[section].append(line.strip())
    print("Done!")
    return data


def run():
    input_file = "books.txt"
    output_file = "generated.csv"

    data = search(input_file)

    with open(output_file, 'w') as f:
        for section, items in data.items():
            for item in items:
                f.write(f"{section}, {item}\n")


run()