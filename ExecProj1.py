# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#%%

"""
Below block consists of the functions used

"""

def isGeneFieldPresent(info_list):
    """This function returns the index of location field based on if gene field is present in the identifier info"""
    if "gene" in info_list[0]:
        return 4
    else:
        return 3

def checkGeneLength(sequence):
    """This function is used to identify sequences that dont have codons mapping to a factor of 3 and fixes the sequence 
    by adding the missing base"""
    if(len(sequence) % 3 != 0):
        sequence = ' ' + sequence
        return sequence
    else:
        return sequence   
    
#%% Below code is for element 1 mentioned in the task

"""
Below codes is for opening the fasta file and segregating the sequence information and the identifier info into 2 separate lists. 
Line starting with '>' is segregated into identifier info_list and the other lines are stripped and segregated as seq_info list

"""

f = open("D:\Study\Research Project 1B\Exercise1_FASTA.txt", "r")
info_list = []
seq_list = []
seq = ""
for line in f:
    if line.startswith(">"):
        info_list.append(line)
        seq_list.append(seq)
        seq = ""
    else:
        seq = seq + line.strip() # strip function removes any line endings or trailing spaces
seq_list.remove("")
seq_list.append(seq)      

"""

gene_length_info is a list of lists where each list consists the gene lenght and the location field info from identifier line.
Gene length is identified based on the length of sequence strings stored in the seq_list. However location info is stored separate
as a string including the '..' and the complement/join info. Calculating gene length from sequence length seemed 
to be an easier approach rather than segregating numbers from location field in identifier line.Count of complement gene sequence
and coding gene sequence is calculated below from location field info present in gene_lenght_info list 

"""

gene_length_info = []
coding_count = 0
complement_count = 0

for info in info_list:
    #info = info.replace(']', '')
    spec_info = info.split('] [')
    location = spec_info[isGeneFieldPresent(spec_info)].split('=')
    gene_length_info.append([location[1]])    
    
for i in range(len(seq_list)):
    seq_list[i] = checkGeneLength(seq_list[i]) #checking if the sequence is has right number of bases to identify faults.
    gene_length_info[i].append(len(seq_list[i])) #gene length
    gene_length_info[i].append(len(seq_list[i])//3) #length in amino acids
    if "complement" in gene_length_info[i][0]:
        complement_count += 1
    else:
        coding_count += 1

print("The count of complement gene sequence : ", complement_count)
print("The count of coding gene sequence : ", coding_count)

#%%

"""    
mRNA sequence is generated from the seq_list and the base pairs are grouped into codons.mRNA_seq_list 
is a list of lists where each list has a list of codons for the sequence. The seq_list
object is deleted as it is no longer required and thus saving space.

"""

mRNA_seq_list = []

for seq in seq_list:
    seq = seq.replace('T','U')
    leading = len(seq) % 3
    output = ([seq[:leading]] if leading else []) + [seq[i:i+3] for i in range(leading, len(seq), 3)]
    mRNA_seq_list.append(output)
del seq_list
    

#%%    
#mRNA to Leucine Amino Acid
# UUA UUG CUU CUA CUG CUC are the codons that code for Leucine amino acid
""" Leucine_list is a list of tuples with 6 entries each. Each entry has the count for Leucine, 
for the 6 codons that code for leucine"""

Leucine_list = []
ATG_codon_check_list = []
others_count = 0
serine_count = 0
for codons in mRNA_seq_list:
    UUA_leucine_count = 0
    UUG_leucine_count = 0
    CUU_leucine_count = 0
    CUA_leucine_count = 0
    CUC_leucine_count = 0
    CUG_leucine_count = 0
    for codon in codons:
        if codon == 'UUA':
            UUA_leucine_count += 1
        elif codon == 'UUG':
            UUG_leucine_count += 1
        elif codon == 'CUU':
            CUU_leucine_count += 1
        elif codon == 'CUA':
            CUA_leucine_count += 1
        elif codon == 'CUC':
            CUC_leucine_count += 1
        elif codon == 'CUG':
            CUG_leucine_count += 1
        elif codon in ('AGC','AGU','UCU','UCC''UCA','UCG'):
            serine_count += 1
        else:
            others_count += 1
    Leucine_list.append((UUA_leucine_count,UUG_leucine_count,CUU_leucine_count,CUA_leucine_count,
                     CUC_leucine_count,CUG_leucine_count,others_count))
                                                        
    if codons[0] == 'AUG':
        ATG_codon_check_list.append("ATG")
    else:
        ATG_codon_check_list.append("NON ATG")
        
#%%

"""Plotting the results using matplotlib"""

import matplotlib.pyplot as plt

UUA = UUG = CUU = CUA = CUC = CUG = 0

nonCUG_list = []

for pro_counts in Leucine_list:
    UUA += pro_counts[0]
    UUG += pro_counts[1]
    CUU += pro_counts[2]
    CUA += pro_counts[3]
    CUC += pro_counts[4]
    CUG += pro_counts[5]

codon_counts = [UUA,UUG,CUU,CUA,CUC,CUG]
print("Total leucine count : " , sum(codon_counts) )
print("Total Serine count : ", serine_count)

bar_label = ["UUA","UUG","CUU","CUA","CUC","CUG"]

left = [1,2,3,4,5,6]

plt.bar(left,codon_counts,tick_label = bar_label, width = 0.8 , 
        color = ['red','blue','limegreen'])

plt.ylabel("No. of Leucine")

plt.show()



#%%

"""writing the results to a csv file"""

import csv

final_list = []

fw = open("D:\Study\Research Project 1B\Final_report_YeastFASTA.csv", "w", newline = '') 
    
for (info,gene_length,start_info,leucine_info) in zip(info_list,gene_length_info,ATG_codon_check_list,Leucine_list):
    locus_id = info[info.find("[locus"):info.find("[p")].replace('[','')
    protein_info = info[info.find("[protein"):info.find("[loca")]
    row_info = {
        "ID" : locus_id,
        "protein_info" : protein_info,
        "location" : gene_length[0],
        "gene_length" : gene_length[1],
        "amino_acids" : gene_length[2],
        "ATG_or_Non_ATG" : start_info,
        "UUA" : leucine_info[0],
        "UUG" : leucine_info[1],
        "CUU" : leucine_info[2],
        "CUA" : leucine_info[3],
        "CUC" : leucine_info[4],
        "CUG" : leucine_info[5],
        }
    final_list.append(row_info)
    
header = ["ID","protein_info","location","gene_length","amino_acids","ATG_or_Non_ATG","UUA","UUG","CUU","CUA","CUC","CUG"]
writer = csv.DictWriter(fw, fieldnames = header)
writer.writeheader()
writer.writerows(final_list)
fw.close()



    


                
   
        



