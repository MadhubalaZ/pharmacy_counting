# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 14:31:43 2019

@author: madhu
"""
import sys

# This function takes the .txt input file, reads data line by line  
# And stores the necessary information in a data dictionary-drug
def read_store_data(inputfile):
    drug={}
    print("Reading and storing data")
    with open(inputfile,'r') as f:
        lines=f.readlines()[1:] #to skip header
        if (len(lines)>0):
            for line in lines:
                data=line.strip().replace('\n','').split(',')
                if (len(data)==5):
                    provider = data[1].upper() +' '+ data[2].upper()
                    drug_name = data[3].upper()
                    drug_cost = int(float(data[4]))
                    if drug_name not in drug:
                        unique_providers=set([provider])
                        total_cost=drug_cost
                        drug[drug_name]=[unique_providers,total_cost]
                    else:
                        combine = drug[drug_name]
                        combine[0].add(provider)
                        combine[1] += drug_cost
        else:
            print("Input file is empty, please provide appropriate input file")
            exit()     
    return(drug)

# This function takes the dictionary calculates total unique providers and returns a copy of sorted dictionary
def process_data(data):
    lists={}
    print("Processing data")
    for drug in data:
        num_unique_providers=len(data[drug][0])
        total_drug_cost = data[drug][1]
        lists[drug]=[num_unique_providers,total_drug_cost]
    sorted_dict = sorted(lists.items(), key=lambda x: (-x[1][1], x[0]))
    return(sorted_dict)

# This function will write the sorted output to a .txt file
def write_file(List):
    print("Data processed, writing to txt file")
    with open(output_filename,'w') as f:
        f.write('drug_name,num_prescriber,total_cost\n')
        for drug in List:
            f.write(str(drug[0])+','+str(drug[1][0]) +','+str(drug[1][1])+'\n')
    print("Please check output folder to view output file")  
    
if len(sys.argv)!=3:
    print("Incorrect number of arguments")
    exit()
input_filename=sys.argv[1]
output_filename=sys.argv[2]

data=read_store_data(input_filename)
sorted_dict=process_data(data)
writefile=write_file(sorted_dict)


            
    