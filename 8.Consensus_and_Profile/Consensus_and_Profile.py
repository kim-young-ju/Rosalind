from Bio import AlignIO
from collections import Counter


# 각각의 base 위치별로 정보 추출
def get_base_info(alignment, i):
    all_bases = []
    for record in alignment:
        all_bases.append(record.seq[i].upper())

    # Counter 함수는 list의 원소 갯수가 알고 싶을 때 사용
    # 각각의 원소가 몇 개씩 있는지를 딕셔너리 형태로 반환합니다.
    base_count = Counter(all_bases)
    # 가장 갯수가 많은 1개의 원소 추출
    most_base = base_count.most_common(1)[0][0]
    return base_count, most_base

# 각 base별로 갯수 추출
def get_all_base(all_bases, all_dict, base_probs):
    for base in all_bases:
        if base in base_probs:
            all_dict[base].append(base_probs[base])
        else:
            all_dict[base].append(0)

    return all_dict


if __name__ == "__main__":
    fn = "rosalind_cons.txt"

    # alignment file 읽을 때 사용하는 library
    fasta = AlignIO.read(fn, "fasta")
    alignment_length = fasta.get_alignment_length()

    consensus = ""
    all_dict = {}
    all_bases = ["A", "C", "G", "T"]

    # list 를 value로 받기 위한 설정
    for base in all_bases:
        all_dict[base] = []
    
    for i in range(alignment_length):
        base_count, most_base = get_base_info(fasta, i)
        consensus += most_base
        all_dict = get_all_base(all_bases, all_dict, base_count)

    print(consensus)
    for base in all_bases:
        to_str = [str(x) for x in all_dict[base]]
        print(base + ":", " ".join(to_str))
    
