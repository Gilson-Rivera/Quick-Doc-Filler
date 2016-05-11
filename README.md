#Quick Doc Filler Programming Language


##Required software

•Python 3.4


•The following python packages: 


	◦openpyxl-2.3.3


	◦python-docx-0.8.5

  
	◦PLY-3.8


•Python IDE, i.e. PyCharm



##Running the Quick Doc Filler Interpreter on Python IDE


After downloading the code and importing it to the Python IDE, run the Parser.py file to start the interpreter and beging inserting commands.


##Available commands


•add -    Inserts a new employee to database.


•delete - Erases a specific employee from database.


•generate - Creates one of 6 different documents using the information of an employee in the database.


	Types of documents that can be generated:

	1.eCert - Employment Certification


	2.eEval - Employee Performance Evaluation


	3.eCont - Employment Contract


	4.eDism - Employee Dismissal Letter


	5.eWarn - Employee Warning Notice


	6.eTrain - Employee Training Certificate



•print - Prints selected document.


•email - Sends an email with a specified document attached to a given email address.




##Examples of command usage


###Formats: 

  •add Name ID Salary Position Date Supervisor


  •delete ID


  •generate eCert ID Output_File_Name


  •generate eEval ID Output_File_Name


  •generate eCont ID Output_File_Name


  •generate eDism ID Output_File_Name


  •generate eWarn ID Output_File_Name


  •generate eTrain ID Output_File_Name


  •print fileName


  •email email_Address fileName



###Parameters:

  •Name - name of the new employee to be added


  •ID - identification number of the an employee


  •Salary - salary of the employee


  •Position - position of employee in the company


  •Date - employment date


  •Supervisor - supervisor of the employee


  •Output_File_Name - desired name of the file generated


  •fileName - name of a file generated

  •email_Address - email to which a generated file will be sent
