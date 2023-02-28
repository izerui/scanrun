# -*- coding: UTF-8 -*-
import logging
from typing import Any

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
    def execute(sql, param: dict = None, auto_transaction=True) -> QSqlQuery:
        query = QSqlQuery(DbUnit.database)
        query.clear()
        if auto_transaction:
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
            logging.exception(query.lastError())
            # raise query.lastError()
        if auto_transaction:
            DbUnit.database.commit()
        return query

    @staticmethod
    def queryForObject(sql, param: dict = None, auto_transaction=True) -> dict:
        query = DbUnit.execute(sql, param, auto_transaction)
        if query.next():
            return query.record().value(0)
        else:
            return None

    @staticmethod
    def queryForMap(sql, param: dict = None, auto_transaction=True) -> dict:
        query = DbUnit.execute(sql, param, auto_transaction)
        if query.next():
            return DbUnit._wrapItem(query)
        else:
            return None

    @staticmethod
    def queryForList(sql, param: dict = None, auto_transaction=True) -> list:
        query = DbUnit.execute(sql, param, auto_transaction)
        list = []
        while query.next():
            list.append(DbUnit._wrapItem(query))
        return list

    @staticmethod
    def queryYieldList(sql, param: dict = None, auto_transaction=True):
        query = DbUnit.execute(sql, param, auto_transaction)
        while query.next():
            yield DbUnit._wrapItem(query)

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
    def __init__(self, tableName):
        super().__init__()
        self.tableName = tableName
        self._checked()

    def _primary_key(self) -> str:
        raise RuntimeError('必须覆盖并实现_primary_key()方法')

    def _table_name(self) -> str:
        return self.tableName

    def _create_sql(self) -> str:
        raise RuntimeError('必须覆盖并实现_create_sql()方法')

    def _create_indexs(self) -> list:
        return []

    def _insert_sql(self, ignore: bool = False) -> str:
        raise RuntimeError('必须覆盖并实现_insert_sql()方法')

    def _checked(self):
        if self.tableName in DbUnit.database.tables():
            pass
        else:
            self.createTable()

    def createTable(self):
        DbUnit.execute(self._create_sql())
        if self._create_indexs():
            for sql in self._create_indexs():
                DbUnit.execute(sql)

    def insert(self, obj):
        DbUnit.execute(self._insert_sql(), obj)

    def insertIgnore(self, obj):
        DbUnit.execute(self._insert_sql(True), obj)

    def deleteById(self, id):
        DbUnit.execute(f'delete from {self.tableName} where {self._primary_key()} = :id', {'id': id})

    def deleteByIds(self, ids: list):
        if not ids:
            return
        if len(ids) == 1:
            self.deleteById(ids[0])
        else:
            inQL = f"({','.join([str(x) for x in ids])})"
            DbUnit.execute(f'delete from {self.tableName} where {self._primary_key()} in {inQL}')

    def deleteAll(self):
        DbUnit.execute(f'delete from {self.tableName}')

    def dropTable(self):
        DbUnit.execute(f'drop table {self.tableName}')

    def execute(self, sql, param):
        return DbUnit.execute(sql, param)

    def queryForList(self, sql, param=None) -> list:
        return DbUnit.queryForList(sql, param)

    def queryYieldList(self, sql, param=None) -> list:
        return DbUnit.queryYieldList(sql, param)

    def queryForMap(self, sql, param=None) -> dict:
        return DbUnit.queryForMap(sql, param)

    def queryForObject(self, sql, param=None) -> Any:
        return DbUnit.queryForObject(sql, param)

    def update(self, item):
        DbUnit.execute(self._genUpdateSQL(item), item)

    def updateBatch(self, items):
        DbUnit.database.transaction()
        for item in items:
            DbUnit.execute(self._genUpdateSQL(item), item, False)
        DbUnit.database.commit()

    def _genUpdateSQL(self, item) -> str:
        if self._primary_key() not in item:
            raise RuntimeError(f'更新的对象不包含主键key: {self._primary_key()}')
        sql = f'update {self.tableName} set'
        sets = []
        for k in item:
            sets.append(f' {k} = :{k}')
        sql += ', '.join(sets)
        sql += f' where {self._primary_key()} = :{self._primary_key()}'
        return sql


# 表操作
class ScanTableUnit(BaseTableUnit):

    def __init__(self, tableName):
        super().__init__(tableName)

    def _primary_key(self) -> str:
        return 'id'

    def _create_sql(self) -> str:
        return f'''
        create table {self.tableName}
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
                        create_time  INTEGER,
                        creator      TEXT,
                        creator_name TEXT,
                        unit_code    TEXT not null unique,
                        box_code     TEXT ,
                        pallet_code  TEXT,
                        complete     INTEGER not null default 0,
                        upload_status INTEGER not null default 0,
                        uploader     TEXT,
                        uploader_name     TEXT,
                        upload_time  INTEGER
                    )
                '''

    # 自动创建表的时候，同步创建索引
    # def _create_indexs(self) -> None:
    #     return [
    #         f'''
    #         create unique index {self.tableName}_index0
    #         on {self.tableName} (ent_code, business_key, unit_code);
    #         '''
    #     ]

    def _insert_sql(self, ignore: bool = False) -> str:
        return f'''
                insert {'OR IGNORE' if ignore else ''} into {self.tableName} ( chejian_code, chejian_name, ent_code, business_key, banzu_code, banzu_name, create_time,
                                   creator, creator_name, unit_code, box_code, pallet_code, complete, upload_status, uploader, uploader_name, upload_time)
                        values (:chejian_code, :chejian_name, :ent_code, :business_key, :banzu_code, :banzu_name, :create_time,
                                   :creator, :creator_name, :unit_code, :box_code, :pallet_code, :complete, :upload_status, :uploader, :uploader_name, :upload_time)
            '''
