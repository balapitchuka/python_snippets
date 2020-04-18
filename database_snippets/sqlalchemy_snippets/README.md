## References

> https://www.compose.com/articles/using-postgresql-through-sqlalchemy/

## Three different ways to use SQLAlchemy:

#### How to choose between the three ways of using SQLAlchemy?

> You probably never want to use the first method (using raw SQL strings), unless you are writing a throwaway script that you need to run only once and are already using SQLAlchemy for the rest of your code base. This method can also be useful if you have existing complex SQL code that you need to run. However, usually, if you want to run raw SQL from Python, you can use a simpler Python database driver such as psycopg2 directly, without the need to install SQLAlchemy as well.

> The second method (SQL Expression Language) can be useful if you need to do something unusual or to run some SQL code that is specific to a certain database. Because the ORM layer tries to abstract away completely from which database you're using, it is sometimes not possible to use it to run SQL code that is highly customized and which targets non-general features of a specific backend. The Expression Language is designed to map to primitive constructs of each backend, and can, therefore, be useful in advanced scenarios

> The final method we showed (The ORM) is useful to keep your code Pythonic and to abstract away from the database completely. It allows one to deal directly with Python classes instead of Tables, with instantiations of objects instead of rows, and with object attributes instead of columns. It also abstracts away from the specific database flavor that you're using, and thus switching your codebase to a different backend can be as simple as changing the call to create_engine, if you've only used functionality that is general to all RDBMSs. Using the ORM for general database applications that do not require specializations provided by only a subset of RDBMSs is thus highly advantageous and you should strongly consider using it wherever possible
