## Index的主要用意是優化搜尋速度，而作業常以username作為query對象，因此對username創造unique id

```sql
create unique index idx_nameID on website.user (username);
```

## 原始搜尋，以username為例，原始SQL預測找14行才會找到我的目標，並且type是All，全局搜索，因為username尚未建立ID，因此無法以B-Tree方式找尋

```sql
explain SELECT * FROM website.user where username="ply";
```

![image]("https://github.com/xboxertony/Homework/blob/master/homework8/%E5%8E%9F%E5%A7%8B%E6%90%9C%E5%B0%8B.png")


## 優化搜尋，對username創造ID後，搜尋可以從secondary index開始，到clustered index，而explain分析後，確實加快不少速度

![image]("https://github.com/xboxertony/Homework/blob/master/homework8/%E6%BC%94%E7%AE%97%E5%84%AA%E5%8C%96%E4%B9%8B%E5%BE%8C.png")

## type為const，且rows為1，有比之前快了一些