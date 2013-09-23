
--- how often did wee see each mac 
select count(ts), mac from dataline group by mac order by count(ts) desc;

--- Count unique macs
select count(distinct mac) from dataline;

