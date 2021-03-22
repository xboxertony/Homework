## 使用insert指令，新增資料，以及取得user資料

```sql
insert into website.user (name,username,password) values ('test','ply','ply');
insert into website.user (name,username,password) values ('test1','test1','test1');
insert into website.user (name,username,password) values ('test2','test2','test2');
insert into website.user (name,username,password) values ('test3','test3','test3');
insert into website.user (name,username,password) values ('test4','test4','test4');
```

![image](https://github.com/xboxertony/Homework/blob/master/homework5/img/%E4%BA%94%E7%AD%86%E8%B3%87%E6%96%99%E7%95%AB%E9%9D%A2.png)

## 使用select指令取得user資料

```sql
select * from website.user;
```

![image](https://github.com/xboxertony/Homework/blob/master/homework5/img/%E4%BA%94%E7%AD%86%E8%B3%87%E6%96%99%E7%95%AB%E9%9D%A2.png)

## 總共幾筆資料

```sql
select count(*) from website.user;
```

![image](https://github.com/xboxertony/Homework/blob/master/homework5/img/%E7%B8%BD%E5%85%B1%E5%A4%9A%E5%B0%91%E6%AC%84%E4%BD%8D.png)

## 時間由近到遠排序指令

```sql
select * from website.user order by time desc;
```

![img](https://github.com/xboxertony/Homework/blob/master/homework5/img/%E7%94%B1%E8%BF%91%E5%88%B0%E9%81%A0.png)

## 時間由近到遠排序指令，第二到四筆

```sql
SELECT * FROM website.user order by time desc limit 3 offset 1;
```

![img](https://github.com/xboxertony/Homework/blob/master/homework5/img/%E7%94%B1%E8%BF%91%E5%88%B0%E9%81%A0%E7%AC%AC%E4%BA%8C%E5%88%B0%E5%9B%9B%E7%AD%86.png)

## username是ply的資料
```sql
select * from website.user where username="ply";
```
![img](https://github.com/xboxertony/Homework/blob/master/homework5/img/username%E6%98%AFply.png)

## username是ply且密碼也是

```sql
select * from website.user where username="ply" and password="ply"
```
![img](https://github.com/xboxertony/Homework/blob/master/homework5/img/username%E6%98%AFply%E4%B8%94%E5%AF%86%E7%A2%BC%E4%B9%9F%E6%98%AF.png)

## 更改使用者為丁滿畫面

```sql
update website.user set name="丁滿" where (username="ply");
```
![img](https://github.com/xboxertony/Homework/blob/master/homework5/img/%E4%B8%81%E6%BB%BF%E7%95%AB%E9%9D%A2.png)

## delete所有資料
```sql
delete from user
```
![img](https://github.com/xboxertony/Homework/blob/master/homework5/img/%E5%88%AA%E9%99%A4%E6%89%80%E6%9C%89%E8%B3%87%E6%96%99.png)
![img](https://github.com/xboxertony/Homework/blob/master/homework5/img/%E8%B3%87%E6%96%99%E7%82%BA%E7%A9%BA%E7%9A%84%E7%95%AB%E9%9D%A2.png)

## 要求四：join語法，取得所有留言包含姓名
![img](https://github.com/xboxertony/Homework/blob/master/homework5/img/%E7%95%99%E8%A8%80%E4%B8%AD%E5%BF%85%E9%A0%88%E5%8C%85%E5%90%AB%E6%9C%83%E5%93%A1%E5%90%8D%E7%A8%B1.png)

## 要求四：join語法，ply的所有留言
![img](https://github.com/xboxertony/Homework/blob/master/homework5/img/%E6%93%B7%E5%8F%96%E6%98%AFply%E7%9A%84%E6%89%80%E6%9C%89%E7%95%99%E8%A8%80.png)
