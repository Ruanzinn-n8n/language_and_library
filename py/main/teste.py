entrada = "5,3,0,0,7,0,0,0,0,6,0,0,1,9,5,0,0,0,0,9,8,0,0,0,0,6,0,8,0,0,0,6,0,0,0,3,4,0,0,8,0,3,0,0,1,7,0,0,0,2,0,0,0,6,0,6,0,0,0,0,2,8,0,0,0,0,4,1,9,0,0,5,0,0,0,0,8,0,0,7,9"

list_inp = list(map(int, entrada.split(",")))
sudoku = []
tam = len(list_inp)
for i in range(0, tam, 9):
    linha_subs = []
    for j in range(9):
        n = i+j
        linha_subs.append(list_inp[n])
    sudoku.append(linha_subs.copy())


def preencher(sudoku_org):
    sudoku = []
    tam = len(sudoku_org)
    for linha in range(tam):
        new_line = []
        for coluna in range(tam):
            test = sudoku_org[linha][coluna]
            if test != 0:
                new_line.append(test)
            else:
                cand_c = 0
                for i in range(tam):
                    candidato_t = i+1
                    if candidato_t == sudoku_org[linha][i]:
                        break
                    else:
                        for j in range(tam):
                            if candidato_t == sudoku_org[j][coluna]:
                                break
                            else:
                                cand_c = candidato_t
                                break
                new_line.append(cand_c)
        sudoku.append(new_line)

    return sudoku
                         

resul = preencher(sudoku)
for i in resul:
    print(*i)