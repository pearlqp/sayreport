import pymysql
import datetime
# 定义和数据库的连接
conn = pymysql.connect(
    host="rm-2zeu2bup91le1scnbpo.mysql.rds.aliyuncs.com",
    port=3306,
    user="Phiin_1",
    passwd="439587426Yn",
    db="lgw",
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)

# 根据用户名查询用户是否存在的函数
def query_user_by_username(username):
    sql = "select * from sys_user where username = %s"
    cur = conn.cursor()
    cur.execute(sql, [username])
    result = cur.fetchone()
    return result
    #if result is None:
        #return True
    #else:
        #return False

# 根据用户名和密码添加数据的函数
def add_user(username,password):
    sql = "insert into sys_user (username,password) values (%s,%s)"
    cur = conn.cursor()
    cur.execute(sql, [username,password])
    conn.commit()


# 3、根据用户id查询当前用户的AI助手聊天信息的函数
def query_message_by_user_id(user_id):
    sql = "select * from chat_message where user_id = %s order by message_time asc"
    cur = conn.cursor()
    cur.execute(sql, [user_id])
    # 字典类型的列表[{},{},{}]
    list = cur.fetchall()
    return list



def do_message_by_user_id(user_id):
    sql = "select * from answer_message where user_id = %s"
    cur = conn.cursor()
    cur.execute(sql, [user_id])
    # 字典类型的列表[{},{},{}]
    list = cur.fetchall()
    return list



def update_password_by_user_id(user_id, new_password):
    """
    根据用户ID更新密码
    :param user_id: 用户的ID
    :param new_password: 新密码
    :return: 操作结果，成功返回True，失败返回False
    """
    sql = "update sys_user set password = %s where user_id = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, [new_password, user_id])
        conn.commit()
        return cur.rowcount > 0  # 如果影响的行数大于0，则表示更新成功
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        cur.close()




def add_chat_message(user_id,message,role):
    sql = "insert into chat_message (user_id,message,role,message_time)values (%s,%s,%s,%s)"
    cur = conn.cursor()
    cur.execute(sql,[user_id,message,role,datetime.datetime.now()])
    conn.commit()

def add_answer_message(user_id,message,role):
    sql = "insert into answer_message (user_id,message,role)values (%s,%s,%s)"
    cur = conn.cursor()
    cur.execute(sql,[user_id,message,role])
    conn.commit()


