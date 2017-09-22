## hw6 | Assignment - pagila

## Database Definition Language - Schema Public
 

### Create the pagila database in the Public schema

- Start up a console (I use Git-Bash), clone the GitHub repository, and move to the directory holding the pagila sql create files.

- ~\Data-Analytics\homework\hw6\pagila-0.10.1\pagila has the three files.

- Enter > psql -U postgres and enter the password for postgres at the prompt.
- Run each of the three files.
	- \i pagila-schema.sql
	- \i pagila-insert-data.sql
	- \i pagila-data.sql
- Test pagila database access from pgAdmin or SQLWorkbench.
 

## Create SQL
### Query group 1

- You need a list of all the actors’ first name and last name.
 
	`select first_name, last_name from actor limit 5;`

	![Results](/images/actor_first_last_names_select.png)

- Display the first and last name of each actor in a single column in upper case letters. Name the column Actor Name.

	`select first_name || ' ' || last_name Actor_Name` 
	`from actor limit 5;`

	![Results](/images/actor_first-last-name_select.png)


### Query group 2

- You need to find the id, first name, and last name of an actor, of whom you know only the first name of "Joe." What is one query would you use to obtain this information?
	
	`select actor_id, first_name, last_name`
	`from actor where first_name like 'Joe.';`
	
	![Results](/images/actor_first_name_Joe._select.png)

- Find all actors whose last name contain the letters GEN. Make this case insensitive.

	`select actor_id, first_name, last_name` 
	`from actor where last_name ilike '%GEN%';`

	![Results](/images/actor_last_name_GEN_select.png)

- Find all actors whose last names contain the letters LI. This time, order the rows by last name and first name, in that order. Make this case insensitive.

	`select last_name,first_name from actor` 
	`where last_name ilike '%LI%' order by last_name,` `first_name;`

	![Results](/images/actor_last_name_LI_select.png)

- Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China.

	`select country_id, country from country` 
	`where country in `
	`('Afghanistan','Bangladesh','China');`

	
	![Results](/images/countries_using_select_in.png)


### Query group 3

- Add a middle_name column to the table actor. Specify the appropriate column type.

	`alter table actor add column middle_name varchar(50);`

	`select * from actor limit 5;`

	![Results](/images/alter_table_add_middle_name_select.png)
	
- You realize that some of these actors have tremendously long last names. Change the data type of the middle_name column to something that can hold more than varchar.
	
	[See this article on character data types](https://www.depesz.com/2010/03/02/charx-vs-varcharx-vs-varchar-vs-text/)

	`alter table actor alter column middle_name type text;`

	![Results](/images/alter_table_alter_middle_name_text.png)



- Now write a query that would remove the middle_name column.

	`alter table actor drop column middle_name;`

	`select * from actor limit 5;`

	
	![Results](/images/alter_actor_drop_middle_name.png)


### Query group 4

- List the last names of actors, as well as how many actors have that last name.
	
	
	`select last_name, count(*) from actor`
	`group by last_name`
	`order by last_name limit 5;` 

	![Results](/images/actor_last_name_count.png)

- List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors
	
	`select last_name, count(*)`
  	`  from actor`
	`group by last_name `
	`having count(*) > 1`
	`order by last_name limit 5;` 

	![Results](/images/actor_last_name_count_2_or_more.png)

- Oh, no! The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS. Write a query to fix the record.

	`select * from actor`
	` where first_name = 'GROUCHO'`
	`  and last_name = 'WILLIAMS';`

	`update actor set first_name = 'HARPO'`
	` where first_name = 'GROUCHO'`
	`   and last_name = 'WILLIAMS';`

	`select * from actor`
	`where first_name = 'HARPO'`
    `and last_name = 'WILLIAMS';`

	![Results](/images/update_actor_first_name.png)

	`commit;`

- Perhaps we were too hasty in changing GROUCHO to HARPO. It turns out that GROUCHO was the correct name after all! 

	- **In a single query:**
	- if the first name of the actor is currently HARPO, change it to GROUCHO.
	- Otherwise, change the first name to MUCHO GROUCHO, as that is exactly what the actor will be with the grievous error. 
	- BE CAREFUL NOT TO CHANGE THE FIRST NAME OF EVERY ACTOR TO MUCHO GROUCHO
	(Hint: update the record using a unique identifier.)

	`select * from actor`
	`where first_name in ('HARPO', 'GROUCHO');`

	![Results](/images/select_actor_first_name1.png)
	
	`select case`
    `     when first_name = 'GROUCHO' then 'MUCHO GROUCHO'`
    `     when first_name = 'HARPO' then 'GROUCHO'`
    `     else first_name`
    `   end as fname`
	`from actor where first_name in ('HARPO', 'GROUCHO');`

	![Results](/images/select_actor_first_name3.png)

	`update actor set first_name =`
    `  case` 
    `     when first_name = 'GROUCHO' then 'MUCHO GROUCHO'`
    `     when first_name = 'HARPO' then 'GROUCHO'`
    `  end` 
	`where first_name in ('HARPO', 'GROUCHO');`

	![Results](/images/update_actor_first_name2.png)


	`select * from actor where first_name like '%GROUCHO';`

	![Results](/images/select_actor_first_name4.png)

	`commit;`

### Query group 5 - Please include examples and answer questions in plain english.

- What’s the difference between a left join and a right join. 
	
	A left join returns all the rows of the left table and those in the right table where the joining column(s) match.  A right join is the same but with all the right table rows returned and those matching to the left table rows on the joining column(s).

- What about an inner join and an outer join? 

	An inner join is the intersection of the two joining tables where joining columns match.  An outer join returns all rows that match in the right or left  tables.

- When would you use a right join?

	When you want all rows from the right table and those matching rows in the left table.

- When would you use an inner join over an outer join?

	An inner join would be best when you only want rows that have matching join columns in both tables or the
	the intersection of the tables.

- What’s the difference between a left outer and a left join?

	No difference.  They are the same join.

	![Results](/images/sql_join_examples.png)


- When would you use rank? 

	Use Rank() to assign a rank number based on the over (partition col order by col) clause to assiciate a value with the grouping.  This groups the same values within each rank number, and between groups the rank numbers can jump to show the relative position of the next group.

	`select f.title, f.rental_duration, rank()` 
	`over (order by rental_duration desc) from film f;`

- What about dense_rank?

	Dense rank() is similar to rank() and will return the rows with a rank number based on the over (partition col order by col) clause.  This groups the same values within with the same rank number so you can easily see the relative position.  Unlike rank(), dense_rank numbers don't jump, so when the group changes the rank number increments by 1

	`select f.title, f.rental_duration, dense_rank()` 
	`over (order by rental_duration desc) from film f;`

- When would you use a subquery in a select?

	You could use a subquery when you need aggregate data, to compare values in the same column, or to use a different view of a table as a joining table.  

	`select c1.first_name, c1.last_name,`
    `(select round(avg(p2.amount),2)` 
 	`from payment p2`
    `where c1.customer_id = p2.customer_id) avg_pymt`	
	`from customer c1;`

- When would you use a group by?

	Use a group by when you want to aggregate the values within the values of the group by column or columns.

	`select last_name, count(*) from actor`
	`group by last_name order by last_name;`

- Describe how you would do data reformatting

	You can concatenate columns using SQL, ||, single quotes, and spaces in a select statement.  You can add other characters, words, and phrases within the single quotes.

	`select first_name || ' ' || last_name as Actor_Name` 
	`from actor;`

- When would you use a with clause?

	You can use a with clause when you want to can create an (in-line) view of a table or tables without creating a permanent view in the database.

	`WITH actor_film AS(`
	`select a.first_name, a.last_name, f.title, f.film_id,` `a.actor_id from actor a`
	`left join film_actor fa`
	`on a.actor_id = fa.actor_id`
	`left join film f`
	`on f.film_id = fa.film_id`
	`order by f.title, a.first_name, a.last_name)`
	`select first_name, last_name, title from actor_film;`


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