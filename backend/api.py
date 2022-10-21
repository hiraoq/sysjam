from flask import *
import MySQLdb

app = Flask(__name__)

@app.route("/api/hello")
def index():
    return "hello"
@app.route("/api/comic",methods=['GET'])
def get_comic():
    json = [
            {"title":"chainsaw-man","author":"Tatsuki Fujimoto"},
            {"title":"jujutsu-kaisen","author":"Gege Akutami"},
            {"title":"my-hero-academia","author":"Kohei Horikoshi"},
            {"title":"kisei-ju","author":"Hitoshi Iwaaki"}]
    return jsonify(json)

# DB操作サンプル
# 実行前に sample.sql を使用してcityテーブルを作成しておく
# mysqlclientを使うパターン
@app.route("/api/sample-msc",methods=['GET'])
def db_sample_msc():
    """ 接続サンプル """
 
    # 接続する 
    con = MySQLdb.connect(
            user='sysjam',
            passwd='sysjam',
            host='db-mysql',
            db='sysjam',
            charset="utf8")
 
    # カーソルを取得する
    cur= con.cursor()
     
    # クエリを実行する
    sql = "select * from city"
    cur.execute(sql)
 
    # 実行結果をすべて取得する
    rows = cur.fetchall()
    cur.close()
    con.close()
    return jsonify(rows)
    # http://localhost:5000/api/dbsampleで結果表示

if __name__ == "__main__":
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000
    )
