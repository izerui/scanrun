from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtWidgets import QMessageBox


# 数据库执行工具类
class DbUnit(object):
    default_database_connection = 'scan_database_connection'
    database = QSqlDatabase('QSQLITE')
    if database.contains(default_database_connection):
        pass
    else:
        database.addDatabase(default_database_connection)
        database.setDatabaseName('scan_data.db')
        database.setUserName('sa')
        database.setPassword('sa>.yj2025.com!%')

    if not database.isOpen():
        database.open()

    @staticmethod
    def execute(sql, param: dict = None) -> QSqlQuery:
        query = QSqlQuery(DbUnit.database)
        DbUnit.database.transaction()
        if param:
            query.prepare(sql)
            for key in param:
                query.bindValue(f':{key}', param[key])
            query.exec()
        else:
            query.exec(sql)
        if query.lastError().isValid():
            QMessageBox.critical(None, '异常', query.lastError().text())
            raise query.lastError()
        DbUnit.database.commit()
        return query

    @staticmethod
    def queryForObject(sql, param: dict = None) -> dict:
        query = DbUnit.execute(sql, param)
        if query.next():
            return DbUnit._wrapItem(query)
        else:
            return None

    @staticmethod
    def queryForList(sql, param: dict = None) -> list:
        query = DbUnit.execute(sql, param)
        list = []
        while query.next():
            list.append(DbUnit._wrapItem(query))
        return list

    @staticmethod
    def _wrapItem(query: QSqlQuery) -> dict:
        item = {}
        for i in range(query.record().count()):
            field = query.record().fieldName(i)
            item[field] = query.value(field)
        return item

    @staticmethod
    def close():
        DbUnit.database.close()


# 数据库操作的基类
class BaseTableUnit(object):
    def __init__(self):
        super().__init__()
        self._checked()

    def _primary_key(self) -> str:
        raise RuntimeError('必须覆盖并实现_primary_key()方法')

    def _table_name(self) -> str:
        raise RuntimeError('必须覆盖并实现_table_name()方法')

    def _create_sql(self) -> str:
        raise RuntimeError('必须覆盖并实现_create_sql()方法')

    def _insert_sql(self) -> str:
        raise RuntimeError('必须覆盖并实现_insert_sql()方法')

    def _checked(self):
        if self._table_name() in DbUnit.database.tables():
            pass
        else:
            self._create()

    def _create(self):
        DbUnit.execute(self._create_sql())

    def insert(self, obj):
        DbUnit.execute(self._insert_sql(), obj)

    def deleteById(self, id):
        DbUnit.execute(f'delete from {self._table_name()} where {self._primary_key()} = :id', {'id': id})

    def deleteAll(self):
        DbUnit.execute(f'delete from {self._table_name()}')

    def execute(self, sql, param):
        return DbUnit.execute(sql, param)

    def queryForList(self, sql, param=None) -> list:
        return DbUnit.queryForList(sql, param)

    def queryForObject(self, sql, param=None) -> dict:
        return DbUnit.queryForObject(sql, param)

    def update(self, item):
        if self._primary_key() not in item:
            raise RuntimeError(f'更新的对象不包含主键key: {self._primary_key()}')
        sql = f'update scan_data set'
        sets = []
        for k in item:
            sets.append(f' {k} = :{k}')
        sql += ', '.join(sets)
        sql += f' where {self._primary_key()} = :{self._primary_key()}'
        DbUnit.execute(sql, item)

# scan_data 表操作
class ScanTableUnit(BaseTableUnit):

    def __init__(self):
        super().__init__()

    def _primary_key(self) -> str:
        return 'id'

    def _table_name(self) -> str:
        return 'scan_data'

    def _create_sql(self) -> str:
        return f'''
        create table {self._table_name()}
                    (
                        id           INTEGER
                            constraint id
                                primary key autoincrement,
                        chejian_code TEXT,
                        chejian_name TEXT,
                        ent_code TEXT,
                        business_key TEXT,
                        banzu_code   TEXT,
                        banzu_name   TEXT,
                        laxian_name  TEXT,
                        create_time  INTEGER,
                        creator      TEXT,
                        creator_name TEXT,
                        unit_code    TEXT,
                        box_code     TEXT,
                        pallet_code  TEXT,
                        upload_status INTEGER,
                        uploader     TEXT,
                        upload_time  TEXT
                    )
                '''

    def _insert_sql(self) -> str:
        return f'''
                insert into {self._table_name()} ( chejian_code, chejian_name, ent_code, business_key, banzu_code, banzu_name, laxian_name, create_time,
                                   creator, creator_name, unit_code, box_code, pallet_code, upload_status, uploader, upload_time)
                        values (:chejian_code, :chejian_name, :ent_code, :business_key, :banzu_code, :banzu_name, :laxian_name, :create_time,
                                   :creator, :creator_name, :unit_code, :box_code, :pallet_code, :upload_status, :uploader, :upload_time)
            '''
