/* TCL(Transaction Control Language): 트랙잭션 제어어 */
/* Tx:Auto -> Tx: Manual */
create table tbl_member(
    id bigint auto_increment primary key,
    name varchar(255) not null,
    address varchar(255) not null
);

insert into tbl_member(name, address)
values ('홍길동', '서울');

commit;

select * from tbl_member;
delete from tbl_member
where id = 1;

rollback;

