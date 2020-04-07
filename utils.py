def read_classification_from_file(filename):
    truth = {}
    file= open(filename, 'r', encoding="utf-8")
    lines = file.readlines() 
    file.close()
    for line in lines:
        items = line.split(' ')
        items[1] = items[1].strip()
        truth[items[0]] = items[1]
    return truth
