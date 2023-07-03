import pandas as pd


def read_sequence_file(fn):
    fasta = {}
    seq = ""
    with open(fn, 'r') as file:
        line = file.readline()
        while line:
            line = line.replace('\n', "")
            if ">" in line:  
                if seq != "":
                    fasta[id] = seq
                    seq = ""
                id = line
            else:
                seq = seq + line.upper()
            fasta[id] = seq
            line = file.readline()

    return fasta

def get_codon_table(fn):
    codon_df = pd.read_csv(fn,header=None, sep='\s+')

    codon_aminoacid = {}
    for row in codon_df.itertuples(index=False):
        for i in (0,2,4,6):
            codon = row[i]
            aminoacid = row[i+1]
            codon_aminoacid[codon] = aminoacid

    start_codon = "AUG"
    stop_codon = [key for key, value in codon_aminoacid.items() if value == "Stop"]

    return codon_aminoacid, start_codon, stop_codon

def reverse_transcription(DNA):
    complement  = {"A" : "U", "C" : "G", "T" : "A", "G" : "C"}
    RVRNA = ""
    for base in DNA:
        RVRNA = complement[base] + RVRNA

    return RVRNA


def get_reading_frame(sub_list, orf_dict, total_orf) :
    
    for index, position in orf_dict.items():
        start = min(position)
        end = max(position)
        aminoacid = ""
        for i in range(start, end, 3):
            frame_codon = sub_list[i]
            aminoacid = aminoacid + codon_aminoacid[frame_codon]

        if aminoacid not in total_orf:
            total_orf.append(aminoacid)
            print(aminoacid)


def get_open_read_frame(sequence, total_orf):
    n = 0
    start_positions = []
    sub_list = []
    orf_dict = {}
    for i in range(len(sequence)):
        substring = sequence[i : i + 3]
        sub_list.append(substring)

        if substring == start_codon:
            start_positions.append(i)

    for start_position in start_positions:
        for i in range(len(sequence)):
            substring = sequence[i : i + 3]
            if substring in stop_codon:
                if ((i-start_position)%3 == 0) and i > start_position:
                    orf_dict[n] = [start_position, i]
                    n = n + 1
                    get_reading_frame(sub_list, orf_dict, total_orf)
                    break
                 


def get_amino_acid_frame(fasta, start_codon, stop_codon):
    
    total_orf = []
    for id, sequences in fasta.items():
        reverse_transcript = reverse_transcription(sequences)
        get_open_read_frame(reverse_transcript, total_orf)
        transcript = sequences.upper().replace("T", "U")
        get_open_read_frame(transcript, total_orf)




if __name__ == "__main__":
    fn = "rosalind_orf.txt"
    codon_table = "codon_table.txt"
    sequences = read_sequence_file(fn)
    codon_aminoacid, start_codon, stop_codon = get_codon_table(codon_table)

    get_amino_acid_frame(sequences, start_codon, stop_codon)