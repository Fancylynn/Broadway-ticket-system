DROP TABLE IF EXISTS ticket;
create table ticket (
    order_id int primary key auto_increment,
    name varchar(30) not null,
    phone_number varchar(10) not null,
    email_addr varchar(50) not null,
    home_addr varchar(100) not null,
    drama char(20) not null,
    drama_time char(20) not null,
    quantity int(8) not null,
    delivery_mode char(20) not null,
    payment char(10) not null
);
