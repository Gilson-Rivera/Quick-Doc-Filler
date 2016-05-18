#Quick Doc Filler Programming Language


##Required software

• Python 3.4


• The following python packages: 


	◦ openpyxl-2.3.3


	◦ python-docx-0.8.5

  
	◦ PLY-3.8


• Python IDE, i.e. PyCharm


<br><br>


##Running the Quick Doc Filler Interpreter on Python IDE


After downloading the code and importing it to the Python IDE, run the Parser.py file to start the interpreter and beging inserting commands.


<br><br>


##Language Features


• add - Inserts a new employee to database.


• delete - Erases a specific employee from database.


• generate - Creates one of 6 different documents using the information of an employee in the database.


	Types of documents that can be generated:

		1. eCert - Employment Certification


		2. eEval - Employee Performance Evaluation


		3. eCont - Employment Contract


		4. eDism - Employee Dismissal Letter


		5. eWarn - Employee Warning Notice


		6. eTrain - Employee Training Certificate



• print - Prints selected document.


• email - Sends an email with a specified document attached to a given email address.


• exit - Close the interpreter


<br><br>


##Examples of features usage


###Formats: 

  	add Name ID Salary Position Date Supervisor


  	delete ID


  	generate eCert ID Output_File_Name


  	generate eEval ID Output_File_Name


  	generate eCont ID Output_File_Name


  	generate eDism ID Output_File_Name


  	generate eWarn ID Output_File_Name


  	generate eTrain ID Output_File_Name


  	print fileName


  	email email_Address fileName
  	
  	
  	exit


<br><br>


###Parameters:

  • Name - name of the new employee to be added


  • ID - identification number of the an employee


  • Salary - salary of the employee


  • Position - position of employee in the company


  • Date - employment date, i.e. 15/dec/2001


  • Supervisor - supervisor of the employee


  • Output_File_Name - desired name of the file generated


  • fileName - name of a file generated
  

  • email_Address - email to which a generated file will be sent
  
  
<br><br>


###How to use QDF:  

Next is an example of a code that can be run in the interpreter:

	add John 65 10000 Cashier 2/May/2016 Michael
	

This line adds a new worker to the database. The parameters are the following:

 • Name = John
 
 
 • ID = 65
 
 
 • Salary = 10000
 
 
 • Position = Cashier
 
 
 • Date = 2/May/2016
 
 
 • Supervisor = Michael
 
 
<br><br>


	generate eCert 65 NewCert
	
	
This line generates an employee certificate with the information of the employee with the ID and will be named NewCert. The parameters are the following:	


 • Doc = eCert
 
 
 • ID = 65
 
 
 • DocName = NewCert
 
 
 <br><br>
 
 
 	print NewCert
 	

This line prints the created document NewCert. The parameter is the DocName (document name). 


<br><br>


	email luis.suarez85@upr.edu NewCert
	
	
This line send an email to the given address with the selected document attached. The parameters are:


 • emailAddress = luis.suarez85@upr.edu
 
 
 • DocName = NewCert
 
 
 <br><br>
 
 
 	delete 65
 	
 	
This line deletes the employee with ID equal to 65, the one that was added at the beginning of the example. The parameters is the employee ID.


<br><br>


	exit
	

This line closes the interpreter.

	
<br><br>

  
##Team:

*Luis E. Rivera Padilla*

*Miguel A. Velez Ocasio*

*Luis A. Suárez Burgos*
