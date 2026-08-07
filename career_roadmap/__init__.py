# Use PyMySQL as the MySQL driver. It is pure Python, so it needs no compiler
# or MySQL dev headers to install. This must run before Django imports the
# mysql backend, which is why it lives in the project package's __init__.
import pymysql

pymysql.install_as_MySQLdb()
