
def read_file(file_path):

    str_list = []
    with open(file_path, 'r') as file:
        line = file.readline()
        while line:
            line.replace('\n', "").upper()
            line = line.strip()
            str_list.append(line) 
            line = file.readline()

    return str_list[0], str_list[1]

if __name__=="__main__":
    fn = "rosalind_subs.txt"
    sequence, motif = read_file(fn)

    print(sequence, motif)
    print(len(sequence), len(motif))
    print(motif[9:10])

    motif_position = []
    for i in range(len(sequence)):
        substring = sequence[i:i + len(motif)]
        if substring == motif:
            motif_position.append(i + 1)
    print(motif_position)
    motif_position_str = [str(x) for x in motif_position]
    print(" ".join(motif_position_str))