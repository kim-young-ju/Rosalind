
def get_Max_GC_ratio(sequences):

    max_ratio = 0
    for id, seq in sequences.items():
        seq_len = len(seq)
        G_cnt = seq.count("G")
        C_cnt = seq.count("C")
        GC_ratio = ((G_cnt + C_cnt)/seq_len)*100

        if GC_ratio > max_ratio:
            max_id = id
            max_ratio = GC_ratio

    return max_id, max_ratio

# Bio 안쓰고 fasta file 읽기
def read_sequence_file(fn):
    fasta = {}
    size = []
    seq = ""
    with open(fn, 'r') as file:
        line = file.readline()
        while line:
            line = line.replace('\n', "")
            if ">" in line:  
                if seq != "":
                    fasta[id] = seq
                    size.append(len(seq))
                    seq = ""
                id = line
            else:
                seq = seq + line.upper()
            fasta[id] = seq
            line = file.readline()

    return fasta, max(size)

if __name__ == "__main__":
    fn = "rosalind_gc.txt"
    sequences, _ = read_sequence_file(fn)

    max_id, max_GC = get_Max_GC_ratio(sequences)
    print(max_id.replace(">",""))
    print(max_GC)