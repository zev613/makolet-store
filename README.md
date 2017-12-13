Zev Seltzer and Harrison Muthui
CPS 111A
Final Project Writeup
December 12, 2017
Makolet_Main
The project was about coming up with a text based store called Makolet which works in a similar way to Amazon, however it uses widgets instead of being a webpage hosted on the Internet. 
The program works by creating a main “welcome” page using the appJar module. Each subsequent “page” is really a subWindow, which is displayed on top of the main window. Everytime the page is changed, it shows the specified subWindow, and hides the previous one.
It is important to note that the entire graphical user interface is not in any function, even a main function. This made the programming easier because any part of the code that refers to the gui uses the instance variable of appJar.gui, called “app”, and needs to refer back to such.
	
It is easy to follow through the code while looking at the buttons instead of functions. The program also imports json, smtp2, datetime and sys. It also makes use of appJar that is used to show the widget. 
The menu_button_press button uses the if loop. The loop makes use of the showSubWindow and hideSubWindow to create two widgets, each a subWindow, called ‘My Account’ and ‘Inventory’.  The buy_button_press button uses a for loop to access the keys under the inventory. Under the inventory category you have the item name, price, quantity of the item, account information which branches out to the balance. The aforementioned categories are the keys in which you 
