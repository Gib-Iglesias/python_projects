/*
SQL: Tax Calculation for Online Tax Application
This SQL query calculates the total income and tax for each account in the year 2023.
It retrieves the IBAN, total income, tax rate, and calculated tax amount.
The tax rate is fixed at 20% for this example.
The results are grouped by IBAN and ordered in ascending order.

[Test from KIOSKO Group]
*/

select
distinct a.iban,
sum(i.amount) as total_income,
'20%' as tax_rate,
round(sum(i.amount) * 0.20, 2) as calculated_tax
from accounts a
inner join income i on (i.account_id = a.id)
where year(i.dt) = 2023
group by 1,3
order by a.iban asc;