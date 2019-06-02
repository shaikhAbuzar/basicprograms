import os
try:
        print(">>>>>>>>>> WORKING WITH DIRECTORIES <<<<<<<<<<")
        print("Creating directory->MyRollno")
        os.mkdir("MyRollno")
        print("Directory Created")
        try:
                print("Creating Rollno in MyRollno")
                os.chdir("MyRollno")
                print("Entered into the MyRollno")
                try:
                        os.mkdir("Rollno")
                        print("Rollno Created Succesfully")
                        print("Creating file in Rollno")
                        os.chdir("Rollno")
                        try:
                                f=open("Rollno.txt","a")
                                for i in range(3):
                                        print("Enter line",i+1,": ", end=' ')
                                        line=input()
                                        f.write(line+"\n")
                                f.close()
                                f=open("Rollno.txt","r")
                                print("\n")
                                for i in range(3):
                                        print("Line {}: ".format(i+1),end=' ')
                                        print(f.readline())
                                f.close()
                        except:
                                print("Error in Rollno File creation")
                except:
                        print("Error in Rollno creation")
        except:
                print("Error in MyRollno creation")
except:
        print("Error in Starting position")
        
choice=input("Delete Rollno [Y/N]: ")
if choice=="Y" or choice=="y":
        print("Deleting the File")
        try:
                os.remove("Rollno.txt")
                print("Rollno.txt removed successfully")
                os.chdir("..")
                os.rmdir("Rollno")
                print("Directory Rollno removed succesfully")
                os.chdir("..")
                os.rmdir("MyRollno")
                print("Directory MyRollno removed successfully")
        except Exception as e:
                print("Error in Deletion: "+str(e))
else:
        print("File not deleted")
