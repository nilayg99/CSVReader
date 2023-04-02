
import pandas
import os

file_Path = "annual-enterprise-survey-2021-financial-year-provisional-csv (1).csv"
file_extension = "csv"
if not file_Path.endswith(file_extension):
    print("This not a CSV file")
else:

    try :
        if file_Path == "annual-enterprise-survey-2021-financial-year-provisional-csv (1).csv":
                                
                file_size = os.path.getsize(file_Path)
                if file_size == 0:
                    print("The file is empty.")
                else:
                    csvFile = pandas.read_csv(file_Path)
                    if file_size  >= 1 * 1024 :

                # displaying the only five data frame out of the CSV file
                        csv_Head_Five = (csvFile.head(6))
                        print (csv_Head_Five)
                        column_Lists = input("Please enter the columns names with Commas:").split(",")
                        selected_Col_List= csvFile[column_Lists]
                        print(selected_Col_List)
                        
                    if selected_Col_List.size == {}:
                        
                        print("File too big.")
        

                                            
                            
        else:
           
            new_File_Path = input("Please enter the file path:")
            if not new_File_Path.endswith(file_extension):
                print("This not a CSV file")
            else:
                new_file_size = os.path.getsize(new_File_Path)
            if new_file_size == 0:
                print("The file is empty.")
            else:
                csvFile = pandas.read_csv(new_File_Path)
            if new_file_size  >= 1 * 1024 :

                # displaying the only five data frame out of the CSV file
                csv_Head_Five = (csvFile.head(6))
                print (csv_Head_Five)
                new_column_Lists = input("Please enter the file path:").split(",")
                print (csvFile[new_column_Lists])


                            

    except FileNotFoundError:
        print ("Sorry, file not found")

