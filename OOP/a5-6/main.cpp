/*
Master C++

	You are very passionate about programing (otherwise you wouldn't be reading this) and C++ is a language close to your heart. 
	On your way to becoming a guru, you study a lot and watch many tutorials. To make sure you do not miss any good tutorials, 
	you absolutely need a software application to help you manage your tutorials and create watch lists. The application can be 
	used in two modes: administrator and user. When the application is started, it will offer the option to choose the mode.

	ADMINISTRATOR MODE: The application will have a database , which holds all the tutorials. You must be able to update the database, 
	meaning: add a new tutorial, delete a tutorial and update the information of a tutorial. Each Tutorial has a title, a presenter 
	(name of the presenter person), a duration (minutes and seconds), a number of likes and a link towards the online resource containing 
	the tutorial. The administrators will also have the option to see all the tutorials in the database.
	
	USER MODE: A user can create a watch list with the tutorials that he/she wants to watch. The application will allow the user to:

		~ See the tutorials in the database having a given presenter (if the presenter name is empty, see all the tutorials), one by one.
		When the user chooses this option, the data of the first tutorial (title, presenter, duration, number of likes) is displayed and 
		the tutorial is played in the browser.

		~ If the user likes the tutorial, he/she can choose to add it to his/her tutorial watch list. If the tutorial seems uninteresting,
		the user can choose not to add it to the watch list and continue to the next. In this case, the information corresponding to the 
		next tutorial is shown and the user is again offered the possibility to add it to the watch list. This can continue as long as 
		the user wants, as when arriving to the end of the list of tutorials with the given presenter, if the user chooses next, the 
		application will again show the first tutorial.
	
		~ Delete a tutorial from the watch list, after the user watched the tutorial. When deleting a tutorial from the watch list, 
		the user can also rate the tutorial (with a like), and in this case, the number of likes for the tutorial will be increased.
	
		~ See the watch list.


WEEK 5
	- Solve the requirements related to the administrator mode
	- Define the DynamicVector class which provides the specific operations: add, remove, length, etc. 
	- The array of elements must be dynamically allocated

WEEK 6
	- Solve all problem requirements
	- DynamicVector must be a templated class
*/
#include "UI.h"
#include "Tests.h"

// OpenCppCoverage --sources Project1 -- ./x64/Debug/Project1.exe

int main()
{
	//Tests t;
	//t.testDynamicVector();
	//t.testTutorial();
	//t.testRepository();
	//t.testService();
	//t.testWatchlist();

	Tutorial t1("Introduction to classes and objects for beginners", "CodeBeauty", Duration(12, 5), 3100, "https://www.youtube.com/watch?v=iVLQeWbgbXs");
	Tutorial t2("C++ Pointers - Finally Understand Pointers", "Caleb Curry", Duration(15, 56), 3400, "https://www.youtube.com/watch?v=rtgwvkaYt1A");
	Tutorial t3("Stack vs Heap Memory in C++", "The Cherno", Duration(19, 30), 31000, "https://www.youtube.com/watch?v=wJ1L2nSIV1s");
	Tutorial t4("The NEW Keyword in C++", "The Cherno", Duration(10, 52), 7200, "https://www.youtube.com/watch?v=NUZdUSqsCs4");
	Tutorial t5("Const Member Function In C++", "CppNuts", Duration(4, 49), 499, "https://www.youtube.com/watch?v=MR37gqFEmFA");
	Tutorial t6("First program Hello World", "CodeBeauty", Duration(26, 31), 6500, "https://www.youtube.com/watch?v=iBG0fN8lY8Y&list=PL43pGnjiVwgQHLPnuH9ch-LhZdwckM8Tq");
	Tutorial t7("How to draw rectangle shape in C++", "CodeBeauty", Duration(10, 53), 703, "https://www.youtube.com/watch?v=XwQmDmXTxdM&list=PL43pGnjiVwgQHLPnuH9ch-LhZdwckM8Tq&index=18");
	Tutorial t8("Operator Overloading In C++", "CppNuts", Duration(13, 49), 462, "https://www.youtube.com/watch?v=DVMZPOt816E&list=PLk6CEY9XxSIAUeZYJYOOwHGr1XZKW6PPG");

	DynamicVector<Tutorial> dv_repo;
	dv_repo.addElem(t1);
	dv_repo.addElem(t2);
	dv_repo.addElem(t3);
	dv_repo.addElem(t4);
	dv_repo.addElem(t5);
	dv_repo.addElem(t6);
	dv_repo.addElem(t7);
	dv_repo.addElem(t8);

	DynamicVector<Tutorial> dv_database;
	Repository repo(dv_repo);
	Watchlist w;
	Service service(repo, w);
	UI ui(service);
	ui.start();
	
	_CrtDumpMemoryLeaks();

	return 0;
}
