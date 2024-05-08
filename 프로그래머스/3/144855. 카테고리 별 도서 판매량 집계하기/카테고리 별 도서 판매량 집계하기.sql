select a.category, sum(b.sales) total_sales
from book a inner join book_sales b on a.book_id = b.book_id
where b.sales_date like "%2022-01%"
group by a.category
order by a.category