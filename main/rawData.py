from datetime import datetime
import pymysql

class UpdateDb():
    def __init__(self):
        self.host = '127.0.0.1'
        self.user = 'root'
        self.password = '123456'
        self.database = 'bishe2025'

    def create_connection(self):
        try:
            connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return connection
        except pymysql.MySQLError as e:
            print(f"连接 MySQL 失败：{e}")
            return None
    '''
    CREATE TABLE http_data (   -- 创建表
        id INT AUTO_INCREMENT PRIMARY KEY,
        src_ip VARCHAR(45),
        dst_ip VARCHAR(45),
        capture_time DATETIME,
        http_payload TEXT
    );
    ALTER TABLE http_data AUTO_INCREMENT = 1;
    '''
    def insert_http_data(self, src_ip, dst_ip,http_payload,current_time):
        connection = self.create_connection()
        if connection is None:
            print("数据库连接不可用，无法插入数据")
            return
        try:
            cursor = connection.cursor()
            sql_query = "INSERT INTO http_data (src_ip, dst_ip, http_payload, capture_time) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql_query, (src_ip, dst_ip, http_payload, current_time))
            connection.commit()
        except pymysql.MySQLError as e:
            print(f"插入数据失败：{e}")
            return 0
        finally:
            cursor.close()
            connection.close()
    '''
     CREATE TABLE normal_data (   -- 创建表
        id INT AUTO_INCREMENT PRIMARY KEY,
		predict_host VARCHAR(20),
		prediction VARCHAR(45),
        src_ip VARCHAR(45),
        dst_ip VARCHAR(45),
        capture_time DATETIME,
        url TEXT
    );
    ALTER TABLE http_data AUTO_INCREMENT = 1;
    '''
    def insert_normal_data(self, predict_host, prediction, src_ip, dst_ip, url, capture_time):
        connection = self.create_connection()
        if connection is None:
            print("数据库连接不可用，无法插入数据")
            return
        try:
            cursor = connection.cursor()
            sql_query = "INSERT INTO normal_data (predict_host, prediction, src_ip, dst_ip, capture_time,url) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql_query, (predict_host, prediction, src_ip, dst_ip,capture_time,url))
            connection.commit()
        except pymysql.MySQLError as e:
            print(f"插入正常数据失败：{e}")
            return 0
        finally:
            cursor.close()
            connection.close()
    '''
    CREATE TABLE abnormal_data (   -- 创建表
        id INT AUTO_INCREMENT PRIMARY KEY,
		predict_host VARCHAR(20),
		prediction VARCHAR(45),
        src_ip VARCHAR(45),
        dst_ip VARCHAR(45),
        capture_time DATETIME,
        url TEXT
    );
    ALTER TABLE http_data AUTO_INCREMENT = 1;
    '''
    # 插入 abnormal_data 表格
    def insert_abnormal_data(self, predict_host, prediction, src_ip, dst_ip, url, capture_time):
        connection = self.create_connection()
        if connection is None:
            print("数据库连接不可用，无法插入数据")
            return
        
        try:
            cursor = connection.cursor()
            sql_query = "INSERT INTO abnormal_data (predict_host, prediction, src_ip, dst_ip, url, capture_time) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql_query, (predict_host, prediction, src_ip, dst_ip, url, capture_time))
            connection.commit()
        except pymysql.MySQLError as e:
            print(f"插入异常数据失败：{e}")
            return 0
        finally:
            cursor.close()
            connection.close()
    # 保存日志到文件中
    def export_data_to_txt(self, table_name, date=None):
        connection = self.create_connection()
        if connection is None:
            print("数据库连接不可用，无法插入数据")
            return
        
        try:
            cursor = connection.cursor()
            if table_name in ['normal_data', 'abnormal_data']:
                # 针对 normal_data 和 abnormal_data，不查询 predict_host 和 prediction
                query_columns = "id, src_ip, dst_ip, capture_time, url"  # 只选择需要的列
            else:
                query_columns = "id, src_ip, dst_ip, capture_time, http_payload"
            sql_query = f"SELECT {query_columns} FROM {table_name}"
            if date:  # 如果提供了日期，则追加 WHERE 条件
                sql_query += f" WHERE DATE(capture_time) = '{date}'"
            
            cursor.execute(sql_query)
            results = cursor.fetchall()  # 获取所有记录
            
            # 检查是否有数据返回
            if not results:
                print(f"在表 {table_name} 中未找到相关数据。")
                return
            
            # 定义输出文件名
            if not date:
                filename = f"../log/{table_name}.txt"
            else:
                filename = f"../log/{table_name}_{date}.txt"
            # 写入数据到 TXT 文件
            with open(filename, 'w', encoding='utf-8') as file:
                for row in results:
                    # 将每行数据使用制表符隔开，然后写入文件
                    file.write('\t'.join(map(str, row)) + '\n')
            
            print(f"数据已成功导出到 {filename}")

        except pymysql.MySQLError as e:
            print(f"导出数据失败：{e}")

if __name__ == '__main__':
    db = UpdateDb()  # 创建数据库更新实例

    table_name = input("请输入要导出的表名 (normal_data, abnormal_data, http_data): ")
    
    date = input("请输入日期 (可选，格式为 'YYYY-MM-DD', 按回车跳过): ")
    date = date.strip() or None  # 如果输入为空，则将其设置为 None
    
    # 调用导出函数
    db.export_data_to_txt(table_name, date)