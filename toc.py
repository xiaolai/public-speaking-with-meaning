for i in range(40):
    filename = 'ch' + str.zfill(str(i + 1), 2) + '.md'
    with open(filename, 'r') as fin:
        data = fin.read().splitlines(True)
    with open('toc', 'a') as fout:
        fout.writelines(f'- [{data[0].strip()}]({filename})\n')