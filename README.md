
# E02a-Control-Structures

Edit README.md to answer the following questions:

- Open main01.py. Before running it, what do you expect this program to do?
It will say hello and then ask what your favorite color is.
  - Now right click on the main1.py window and select “Run Python File in Terminal”. Click in the bottom panel, and answer the question. Describe what happened.
  It said greetings at the bottom and then asked what color is your favorite.
  - What do you think the program did with what you typed in answer to the question?
  It did nothing because the information was not stored in a variable.

- Open main02.py. Before running it, describe how this is different than main01.py.
It stores the input.
  - What do you think the color = input() will do?
It will take infor from an input and store it to the system.
  - Run the program in the terminal and answer the question. Did the program do what you expected?
Yes

- Open main03.py. Before running it, describe how this is different than main02.py.
Main 3 has an if else command string
  - What is happening on lines 9–12?
It is checking the answer
  - Why are lines 10 and 12 indented?
It shows what code they belong to.
  - Run the program and answer the question. What happens if you don’t capitalize Red?
The program does not work.
  - What does this tell you about "color"?
It is case sensitive

- Open main04.py. Before running it, describe how this is different than main03.py.
It has an or command.
  - What problem is this trying to solve?
The problem of case sensitivity.
  - Run the program and answer the question. What happens if you use some other capitalization scheme (i.e., “RED” or “reD“)?
The program fails.

- Open main05.py. What do you expect line 9 to do?
convert whatever the user typed into lower case
  - What problem is it trying to solve?
case sensitivity.
  - Run the program and answer the question. What happens if you add spaces before or after the word (i.e., “ RED “ or “ red”)?
The problem fails

 - Open main06.py. How is line 9 different than in main05.py?
 It adds the strip function
   - What would you guess .strip() is doing?
  Getting rid of the spaces before and after
   - Run the program and answer the question. Is there another way of writing “red” that will break this logic?
  I do not believe so

 - Open main07.py. Before running this program, how do you expect this to be different than main06.py?
 It adds another possible answer
   - What is happening on line 12?
  It is an elif statement which allows another possible answer
   - Run the program and answer the question.
  
 - Open main08.py. What is the purpose of line 9?
It is a while loop
   - Why are lines 10–17 indented?
they are all inside the while loop
   - Run the program. What would happen if line 10 were moved before line 9 (and no longer indented)?
It would turn into an infinite loop
   - Make that change and run the program again. (To end any Python program, you can type ctrl-c)

 - Open main09.py. What is happening on line 13?
It is counting the amount of times the loop has repeated
   - What is the purpose of “count”?
store a value
   - What is happening on line 22?
The value of count is being returned.
   - Run the program.

 - *Extra credit:* open main10.py. Add a comment to each line describing what it is doing (a comment follows a pound sign [#]).
 - *Extra credit:* open main11.py. What is happening on lines 6-11? It makes sure that the color for each game is not the same as the last.
  
Commit your changes and push them back to the repository.
 
