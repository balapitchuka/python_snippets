# MySQL Snippets

### Create a database
``` CREATE DATABASE  IF NOT EXISTS `hb_student_tracker`; ```

### Change to a database
``` USE `hb_student_tracker`; ```

### Delete a table
```DROP TABLE IF EXISTS `student`; ```

### Create a table
```
CREATE TABLE student (
id int(11) NOT NULL AUTO_INCREMENT,
first_name varchar(45) DEFAULT NULL,
last_name varchar(45) DEFAULT NULL,
email varchar(45) DEFAULT NULL,
PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;
```

### Show all the tables in Current Database
```show tables;```

### Query a table
``` select * from student; ```

### Reset AUTO_INCREMENT Field to 3000
```
TABLE hb_student_tracker.student AUTO_INCREMENT=3000;
```

### Delete all rows and reset AUTO_INCREMENT Field
```TRUNCATE hb_student_tracker.student;```