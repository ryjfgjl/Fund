# fund
alter table fund 
    add index(code);

# jzhistory
alter table jzhistory 
    add index(fundCode, FSRQ);

commit;
