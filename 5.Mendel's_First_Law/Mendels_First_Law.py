
def read_file(fn):
    with open(fn, 'r') as file:
        line = file.readline()
        while line:
            line = line.replace('\n', "")
            line_split = line.split(" ")
            k = line_split[0] # 우성 동형
            m = line_split[1] # 이형
            n = line_split[2] # 열성 동형
            line = file.readline()

    return int(k), int(m), int(n)


if __name__ == "__main__":
    fn = "rosalind_iprb.txt"

    k, m, n = read_file(fn)

    total = k+m+n
    # dr dr
    drdr = (m/total) * ((m-1)/(total-1)) * (1/4)

    # dr rr
    drrr = (m/total) * (n/(total-1)) * (1/2) * 2

    # rrrr
    rrrr = (n/total) * ((n-1)/(total-1))

    percentage_dominant = 1 - (drdr + drrr + rrrr)
    print(percentage_dominant)