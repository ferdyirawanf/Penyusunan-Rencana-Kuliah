def input_file():   # Fungsi untuk input file
    data = []       # List menyimpan salinan input file perbaris
    file = open("..\\test\\input1.txt", "r")
    for i in file:
        i = i.replace("\n", "")     # Menghapus char '\n' atau new line
        i = i.replace(".", "")      # Menghapus char titik diakhir baris input
        data.append(i.split(", "))  # Menambahkan baris perbaris ke list data dipisahkan koma
    return data

def baris_kolom(input_list):    # Fungsi untuk membuat list string unik dari input
    baris_kolom = []            # Menyimpan string unik yang akan berperan sebagai baris dan kolom matriks
    for i in range(len(input_list)):
        baris_kolom += [input_list[i][0]]   # Menyalin string pertama setiap baris input
    return baris_kolom

def adjacency_matrix(list_input, list_baris_kolom): # Fungsi untuk membuat matriks ketetanggan
    matrix = [[0 for i in range(len(list_baris_kolom))] for j in range(len(list_baris_kolom))]  # Inisialisasi matriks dengan 0 semua
    for i in range(len(list_input)):
        for j in range(1,len(list_input[i])):
            k = 0
            match = False
            while k < len(list_baris_kolom) and match == False: # Sepanjang list string unik list_baris_kolom
                if list_input[i][j] == list_baris_kolom[k]: # Memetakan string input ke matriks ketetanggan
                    matrix[k][i] = 1        # Element matriks yang memiliki hubungan ketetanggan diganti dengan 1
                    match = True
                k += 1
    return matrix

def hapus_kolom_nol(list_semua_nol,matrix_adjacency):   # Fungsi untuk menghapus kolom dari matriks ketetanggan
    for i in range(len(list_semua_nol))[::-1]:          # yang semua elementnya 0
        for j in matrix_adjacency:                      # (dengan kata lain menghapus setengah sisi graf)
            del j[list_semua_nol[i]]                    # Menghapus kolom matriks ketetanggan
    return matrix_adjacency

def hapus_baris_nol(list_semua_nol,matrix_adjacency):   # Fungsi untuk menghapus baris dari matriks ketetanggan
    for i in range(len(list_semua_nol))[::-1]:          # yang kolomnya dihapus
        del matrix_adjacency[list_semua_nol[i]]         # (dengan kata lain menghapus setengah sisi graf)
    return matrix_adjacency                             # Menghapus baris matriks ketetanggan

def hapus_no_prereq(no_prereq, list_baris_kolom):       # Fungsi untuk menghapus string baris dan kolom matriks
    for i in range(len(no_prereq))[::-1]:               # (dengan kata lain menghapus node graf)
        del list_baris_kolom[no_prereq[i]]              # Menghapus node graf yang tidak memiliki sisi masuk
    return list_baris_kolom

def desimal_ke_romawi(desimal):            # Fungsi untuk mengubah bilangan bulat/desimal ke romawi
    list_desimal = [10, 9, 5, 4, 1]
    list_romawi = ["X", "IX", "V", "IV", "I"]
    hasil = ''                             # Inisialisasi variabel untuk menyimpan hasil romawi
    i = 0
    while desimal > 0:
        for j in range(desimal // list_desimal[i]):
            hasil += list_romawi[i]        # Menambahkan string romawi
            desimal -= list_desimal[i]     # Mengurangi value dari bilangan bulat
        i += 1
    return hasil

def print_semester(list_output):    # Fungsi untuk output string (mata kuliah) persemester
    for i in range(len(list_output)):
        if i+1 == 8:    # Jika semesternya 8 maka terdapat 4 char yaitu VIII
            print("Semester", desimal_ke_romawi(i+1), end="    : ")  # digunakan satu tab agar output rapi
        elif i+1 == 3 or i+1 == 7: # Jika semesternya 3 atau 7 maka terdapat 3 char yaitu III dan VII
            print("Semester", desimal_ke_romawi(i+1), end="     : ") # digunakan satu tab agar output rapi
        elif i+1 == 1 or i+1 == 5: # Jika semesternya 1 atau 5 maka terdapat 1 char yaitu I dan V
            print("Semester", desimal_ke_romawi(i+1), end="       : ") # digunakan satu tab agar output rapi
        else:       # Jika semesternya 2, 4, dan 6 maka terdapat 2 char yaitu II, IV, dan VI
            print("Semester", desimal_ke_romawi(i+1), end="      : ") # digunakan dua tab agar output rapi
        for j in range(len(list_output[i])):
            print(list_output[i][j], end="")
            if j != len(list_output[i]) - 1:
                print(end=", ")
            else:
                print(".")

def semua_lintasan(list_input, asal, tujuan, list_lintasan=[]): # Fungsi untuk mencari semua lintasan
    list_semua_lintasan = []    # List untuk menyimpan semua lintasan yang mungkin
    list_lintasan = list_lintasan + [asal]  # List untuk menyimpan lintasan yang sekarang dibuat
    if asal == tujuan:      # Jika simpul asal dan tujuan sama maka akan berhenti
        return [list_lintasan]
    if len(list_input[asal]) == 0:  # Jika string/simpul tidak ada di list input maka menghasilkan list kosong
        return []
    for simpul in list_input[asal]:
        if simpul not in list_lintasan:
            list_semua_lintasan2 = semua_lintasan(list_input, simpul, tujuan, list_lintasan)  # Rekursif
            for list_lintasan2 in list_semua_lintasan2:
                list_semua_lintasan += [list_lintasan2] # Menambahkan semua listasan ke dalam list
    return list_semua_lintasan

def lintasan_siklis(list_baris_kolom, matrix_adjacency):    # Fungsi untuk mencari semua lintasan siklis
    list_idx = []                                           # (simpul asal dan tujuan sama)
    list_siklis = []
    for i in range(len(matrix_adjacency)):
        list_idx_temp = []
        list_idx_temp += [list_baris_kolom[i]]
        list_idx += [list_idx_temp]
        for j in range(len(matrix_adjacency)):  # Bagian untuk membuat list seperti list input namun elementnya bukan
            if matrix_adjacency[i][j] == 1:     # string input melainkan indeks dari string input yang direpresentasikan
                list_idx[i] += [j]              # dalam matriks ketetanggan tadi, kemudian menghapus element pertama karena
        del list_idx[i][0]                      # untuk mencari lintasasan, simpul awalnya yaitu semua simpul setelah simpul awal
    for i in range(len(list_idx)):          # Bagian untuk mencari semua lintasan, karena dalam fungsi semua_lintasan
        for j in range(len(list_idx[i])):   # tidak boleh ada simpul asal dan tujuan yang sama, maka akan dicari mulai
            list_siklis += semua_lintasan(list_idx, list_idx[i][j], i)  # dari simpul setelah asal
    for i in range(len(list_siklis)):
        list_siklis[i].insert(0,list_siklis[i][len(list_siklis[i])-1])  # Menambahkan list pertama kembali yang tadi dihapus
    for i in range(len(matrix_adjacency)):                              # sebelum memanggil fungsi semua_lintasan
        for j in range(len(list_siklis)):
            for k in range(len(list_siklis[j])):
                if (i == list_siklis[j][k]):
                    list_siklis[j][k] = list_baris_kolom[i] # Mengubah kembali dari integer (indeks) ke string input lagi
    return list_siklis

def topological_sort(list_baris_kolom, matrix_adjacency):   # Fungsi topological sort (menghapus satu demi satu node
    list_output = []                                        # yang tidak mempunyai sisi masuk ke node tersebut, dilakukan sampai
    panjang = len(list_baris_kolom)                         # sampai tidak ada simpul yang tersisa)

    while panjang > 0:      # Selama node belum habis
        no_prereq = []      # List yang menyimpan mata kuliah yang tidak mempunyai prasyarat (prereq)
        no_prereq_id = []
        x_temp = [[matrix_adjacency[j][i] for j in range(panjang)] for i in range(panjang)] # Proses untuk transpose matriks-
        for i in range(len(x_temp)):                        # -yang tujuannya memudahkan untuk mencari secara baris perbaris-
            all_nol = True                                  # -mana yang semuanya nol (tidak memiliki sisi masuk)
            for j in range(len(x_temp)):            # Mencari apakah satu baris semua elementnya nol atau bukan
                if x_temp[i][j] == 1:
                    all_nol = False
            if all_nol:                             # Jika semua elementnya nol
                no_prereq += [list_baris_kolom[i]]  # Elementnya (mata kuliah) dimasukkan ke list no_prereq
                no_prereq_id += [i]                 # Dan indeksnya dimasukkan ke no_prereq_id
        list_output += [list(no_prereq)]    # Menambahkan semua mata kuliah tanpa syarat/prereq ke list_output
        list_hapus_kolom = hapus_kolom_nol(no_prereq_id, matrix_adjacency)  # Memanggil fungsi hapus_kolom_nol
        list_hapus_baris = hapus_baris_nol(no_prereq_id, list_hapus_kolom)  # Memanggil fungsi hapus_baris_nol
        list_baris_kolom = hapus_no_prereq(no_prereq_id, list_baris_kolom)  # Memanggil fungsi hapus_no_prereq
        panjang = panjang - len(no_prereq_id)   # Banyaknya simpul dikurangi sebanyak simpul yang dihapus
    return list_output

# MAIN PROGRAM
list_input = input_file()   # Input file dan disimpan daladm list_input
list_baris_kolom = baris_kolom((input_file()))  #
matrix_adjacency = adjacency_matrix(list_input, list_baris_kolom)   # Membuat matriks ketetanggan
if (len(lintasan_siklis(list_baris_kolom,matrix_adjacency)) != 0):  # Jika dalam input ada lintasan siklis
    print("Input tidak valid (Bukan DAG). Terdapat",len(lintasan_siklis(list_baris_kolom,matrix_adjacency)) , "lintasan siklis/loop!")
    print("Lintasan siklis tersebut antara lain: ")
    print(*lintasan_siklis(list_baris_kolom,matrix_adjacency), sep="\n")    # Print semua lintasan siklis
else:   # Jika dalam input tidak ada lintasan siklis (DAG)
    print("Daftar Mata Kuliah yang Dapat Diambil:")
    print_semester(topological_sort(list_baris_kolom, matrix_adjacency))
