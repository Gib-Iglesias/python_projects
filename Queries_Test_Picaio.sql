//Queries Test Picaio

//Query 1:
//obten horas trabajadas entre dos fechas y calcular el monto a pagar a los trabajadores

with hours as (
select distinct
l.id as id,
l.name as name,
l.previous_balance as previous_balance,
sum(timestampdiff(HOUR, dh.entry_time, dh.exit_time)) as tot_hours
from laborers as l
INNER JOIN daily_hours as dh on (dh.labor_id = l.id)
group by 1,2,3
)
select
name as name,
((tot_hours * 30) + previous_balance) as amount_payable
from hours
order by name asc;





//Query 2:
//Obtener el total de votos por candidato en cada estado y ordenarlos dentro de una cadena de texto

with counts as (
select distinct
r.state as state,
count(c.id) as count_id,
concat(c.first_name, ' ', c.last_name) as candidate_name
from candidates c
INNER JOIN results r on (r.candidate_id = c.id)
group by 1,3
)
select
distinct state,
group_concat(candidate_name, ' x ', count_id ORDER BY count_id desc, candidate_name asc) as votes
from counts
group by 1
order by 1 asc;
