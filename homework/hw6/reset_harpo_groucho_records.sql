select * from actor
where first_name like '%GROUCHO';

update actor set first_name = 'GROUCHO' where actor_id in(78,106);

update actor set first_name = 'HARPO' where actor_id =172;

commit;

