# fund
drop table if exists fund;
create table fund
(
    id int unsigned primary key auto_increment,
    code varchar(255) default null,
    name varchar(255) default null
);

# jzhistory
drop table if exists jzhistory;
create table jzhistory
(
    id int unsigned primary key auto_increment,
    fundCode varchar(255) default null,
    FSRQ varchar(255) default null,
    DWJZ varchar(255) default null,
    LJJZ varchar(255) default null,
    SDATE varchar(255) default null,
    ACTUALSYI varchar(255) default null,
    NAVTYPE varchar(255) default null,
    JZZZL varchar(255) default null,
    SGZT varchar(255) default null,
    SHZT varchar(255) default null,
    FHFCZ varchar(255) default null,
    FHFCBZ varchar(255) default null,
    DTYPE varchar(255) default null,
    FHSP varchar(255) default null
);
