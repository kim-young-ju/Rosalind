import pandas as pd

def read_sequence_file(fn):
    seq = ""
    with open(fn, 'r') as file:
        line = file.readline()
        while line:
            line = line.replace('\n', "")
            seq = seq + line.upper()
            line = file.readline()

    return seq

def get_codon_table(fn):
    # '\s+': 공백을 구분자로 사용
    codon_df = pd.read_csv(fn,header=None, sep='\s+')

    # 딕셔너리 생성
    codon_aminoacid = {}
    for row in codon_df.itertuples(index=False):
        for i in (0,2,4,6):
            codon = row[i]
            aminoacid = row[i+1]
            codon_aminoacid[codon] = aminoacid

    start_codon = "AUG"
    stop_codon = [key for key, value in codon_aminoacid.items() if value == "Stop"]

    return codon_aminoacid, start_codon, stop_codon

def get_amino_acid_frame(sequences, start_codon, stop_codon):
    sub_list = []
    start_positions = []
    for i in range(len(sequences)):
        substring = sequences[i : i + 3]
        sub_list.append(substring)

        if substring == start_codon:
            start_positions.append(i)
        if substring in stop_codon:
            for start_position in start_positions:
                if (i-start_position)%3 == 0:
                    start = start_position
                    end = i
                    break

    return sub_list, start, end

if __name__ == "__main__":
    fn = "rosalind_prot.txt"
    codon_table = "codon_table.txt"
    sequences = read_sequence_file(fn)

    codon_aminoacid, start_codon, stop_codon = get_codon_table(codon_table)

    sub_list, start, end = get_amino_acid_frame(sequences, start_codon, stop_codon)

    aminoacid = ""
    for i in range(start, end, 3):
        frame_codon = sub_list[i]
        aminoacid = aminoacid + codon_aminoacid[frame_codon]

    print(aminoacid)