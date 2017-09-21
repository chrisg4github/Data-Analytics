## hw6 | Assignment - pagila

## Infrastructure
 

### Create the pagila database

- Start up a console (I use Git-Bash), and move to the directory holding the pagila sql create files.
- Enter > psql -U postgres and enter the password for postgres at the prompt.
- Run each of the three files.
	- \i pagila-schema.sql
	- \i pagila-insert-data.sql
	- \i pagila-data.sql
- Test pagila database access from pgAdmin or SQLWorkbench.
 

## Create SQL
### Query group 1

- You need a list of all the actors’ first name and last name.

- Display the first and last name of each actor in a single column in upper case letters. Name the column Actor Name.

### Query group 2

- You need to find the id, first name, and last name of an actor, of whom you know only the first name of "Joe." What is one query would you use to obtain this information?

- Find all actors whose last name contain the letters GEN. Make this case insensitive.

- Find all actors whose last names contain the letters LI. This time, order the rows by last name and first name, in that order. Make this case insensitive.

- Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China.

### Query group 3

- Add a middle_name column to the table actor. Specify the appropriate column type.

- You realize that some of these actors have tremendously long last names. Change the data type of the middle_name column to something that can hold more than varchar.

- Now write a query that would remove the middle_name column.

### Query group 4

- List the last names of actors, as well as how many actors have that last name.

- List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors

- Oh, no! The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS. Write a query to fix the record.

- Perhaps we were too hasty in changing GROUCHO to HARPO. It turns out that GROUCHO was the correct name after all! 

- **In a single query:**
	- if the first name of the actor is currently HARPO, change it to GROUCHO.
	- Otherwise, change the first name to MUCHO GROUCHO, as that is exactly what the actor will be with the grievous error. 
	- BE CAREFUL NOT TO CHANGE THE FIRST NAME OF EVERY ACTOR TO MUCHO GROUCHO
	(Hint: update the record using a unique identifier.)


### Query group 5 
- What’s the difference between a left join and a right join. 

- What about an inner join and an outer join? 

- When would you use rank? 

- What about dense_rank? 

- When would you use a subquery in a select? 

- When would you use a right join?

- When would you use an inner join over an outer join?

- What’s the difference between a left outer and a left join

- When would you use a group by?

- Describe how you would do data reformatting

- When would you use a with clause?


### Query group 6
- Use a JOIN to display the first and last names, as well as the address, of each staff member. Use the tables staff and address:

- Use a JOIN to display the total amount rung up by each staff member in January of 2007. Use tables staff and payment.
You’ll have to google for this one, we didn’t cover it explicitly in class. 

- List each film and the number of actors who are listed for that film. Use tables film_actor and film. Use inner join.

- How many copies of the film Hunchback Impossible exist in the inventory system?

- Using the tables payment and customer and the JOIN command, list the total paid by each customer. List the customers alphabetically by last name:

### Query group 7
- The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence, films starting with the letters K and Q have also soared in popularity. display the titles of movies starting with the letters K and Q whose language is English.

- Use subqueries to display all actors who appear in the film Alone Trip.

- You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all Canadian customers. Use joins to retrieve this information.

- Sales have been lagging among young families, and you wish to target all family movies for a promotion. Identify all movies categorized as a family film.
Now we mentioned family film, but there is no family film category. There’s a category that resembles that. In the real world nothing will be exact.

- Display the most frequently rented movies in descending order.

- Write a query to display how much business, in dollars, each store brought in.

- Write a query to display for each store its store ID, city, and country.

- List the top five genres in gross revenue in descending order. 


### Query group 8
- In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. Use the solution from the problem above to create a view. 

- How would you display the view that you created in previous sql statement?

- You find that you no longer need the view top_five_genres. Write a query to delete it.


## Appendix 

### markdown discards some UNDERSCORES so those table or view names are bolded

### Tables
- actor

- address

- category

- city

- country

- customer

- film

- film_actor

- film_category

- film_text (not in the database)

- inventory

- language

- payment

- **payment_p2007_01**

- **payment_p2007_02**

- **payment_p2007_03**

- **payment_p2007_04**

- **payment_p2007_05**

- **payment_p2007_06**

- rental

- staff

- store

### Views
- actor_info

- **actors_and_films**

- customer_list

- film_list

- **nicer_but_slower_film_list**

- **sales_by_film_category**

- **sales_by_store**

- staff_list