# Insight Data Science Challenge/pharmacy_counting

### Problem
As a data engineer working for an online pharmacy, I have generated a list of all drugs, the 
total number of unique individuals who were prescribed the medication, and the total drug cost, which 
is listed in descending order based on the total drug cost and if there is a tie, according to 
drug name in ascending order. 

### Procedure
Python language is used to solve the challenge. Following are the approaches I have used to solve the
pharmacy counting challenge.
1. Read the records from the itcont txt file and stored the necessary fields data (checking if the 
file is not empty and each row has 5 columns)
2. Stored the information by implementing a data dictionary for the key value pairs, where key is 
drug name, and value is a list of two variables where- first is a set of provider and second 
is drug cost.
3. If the drug name is already present in data dictionary, the provider name was appended to
first value and drug cost was added to the second value. As the provider is stored as a set,
only unique providers will be stored.
4. The total number of unique providers was calculated by finding the length of set of the first
 value for each drug in the data dictionary.
5. A sort operation was used to sort the data dictionary according to the given requirements i.e first 
sorted according to total drug cost (descending) and if there is a tie,sorted according to 
the name of the drug in alphabetical order.
6. Output was written and stored in a top_cost_drug.txt file as given in the system 
arguments during run.sh file.
Output file, **`top_cost_drug.txt`**, would contain the following lines
```
drug_name,num_prescriber,total_cost
CHLORPROMAZINE,2,3000
BENZTROPINE MESYLATE,1,1500
AMBIEN,2,300
```

### How to run the program
Use the following procedure to run the program:
1. Download the entire Insight challenge folder
2. Run the terminal and check if python is installed (If not then install)
3. Change the directory of the terminal to pharmacy_counting folder
 (You can change the input file if you want)
4. Now use command: chmod 777 ./run.sh
5. Now run the .sh file by using command: ./run.sh
6. It will generate output file top_cost_drug.txt in the output folder
7. Now to run the tests from insight_testsuite/run_tests.sh file change the directory of terminal 
to insight_testsuite
8. Now use command: chmod 777 ./run_tests.sh
9. Now run the .sh file by using command: ./run_tests.sh
10. This command will show how many of the given test cases passed by the program.
