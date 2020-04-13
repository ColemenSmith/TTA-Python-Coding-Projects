import sqlite3

conn = sqlite3.connect('drill.db')
cur = conn.cursor()


def createDb():
    with conn:
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_drill( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_file TEXT)")
        addToDb()
        conn.commit()
        query()
        


def addToDb():
    fileList = ['information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg']
    txt = ".txt"
    adder = [i for i in fileList if txt in i]
    for adds in adder:           
        cur.execute("INSERT INTO tbl_drill(col_file) VALUES (?)", \
                   (adds,))

def query():
    with conn:
        cur.execute("SELECT * FROM tbl_drill")
        rows = cur.fetchall()
        for row in rows:
            print(row)


if __name__ == "__main__":
                    createDb()
                    
