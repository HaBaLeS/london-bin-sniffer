
--- how often did wee see each mac 
select count(ts), mac from dataline group by mac order by count(ts) desc;

--- Count unique macs
select count(distinct mac) from dataline;


select * from select substr(mac,0, 9) from dataline group by mac;



select m.man from mac2man m, dataline dl where substr(dl.mac,0, 9) = lower(m.mac) group by dl.mac, m.man;

 select * from mac2man m, dataline dl where substr(dl.mac,0, 9) = lower(m.mac) group by dl.mac;

select lower(mac), man FROM mac2man where ;

