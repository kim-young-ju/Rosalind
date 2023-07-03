# collections Counter과 most 추출 구현
def collections_Counter(all_bases, bases_list):
    base_count = {}
    max_cnt = 0
    for base in bases_list:
        base_cnt = all_bases.count(base)
        base_count[base] = base_cnt
        if base_cnt > max_cnt:
            max_cnt = base_cnt
            max_base = base

    return base_count, max_base


# 각각의 base 위치별로 정보 추출
def get_base_info(alignment, i, bases_list):
    all_bases = []
    for id, seq in alignment.items():
        all_bases.append(seq[i])

    base_count, most_base = collections_Counter(all_bases, bases_list)

    return base_count, most_base

# 각 base별로 갯수 추출
def get_all_base(all_bases, all_dict, base_probs):
    for base in all_bases:
        if base in base_probs:
            all_dict[base].append(base_probs[base])
        else:
            all_dict[base].append(0)

    return all_dict

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
    fn = "rosalind_cons.txt"

    fasta, alignment_length = read_sequence_file(fn)
    consensus = ""
    all_dict = {}
    all_bases = ["A", "C", "G", "T"]

    for base in all_bases:
        all_dict[base] = []
    
    for i in range(alignment_length):
        base_count, most_base = get_base_info(fasta, i, all_bases)
        consensus += most_base
        all_dict = get_all_base(all_bases, all_dict, base_count)

    print(consensus)
    for base in all_bases:
        to_str = [str(x) for x in all_dict[base]]
        print(base + ":", " ".join(to_str))
