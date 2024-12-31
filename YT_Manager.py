import sqlite3
conn=sqlite3.connect('youtube_videos.db')
cursor=conn.cursor()
cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )
            ''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    rows=cursor.fetchall()
    if not rows:
        print("\nThe list is empty.\n")
    else:
        for row in rows:
            print(row)

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)", (name,time))
    conn.commit()


def update_video(vid,name,time):
    cursor.execute("UPDATE videos SET name=?, time=? WHERE id=?",(name,time,vid))
    conn.commit()

def delete_video(vid):
    cursor.execute("DELETE FROM videos WHERE id=?",(vid,)) #In (vid,) it is necessar to put comma otherwise it will not be considered as tuple and it only accepts tuple 
    #so be aware
    conn.commit()

def main():
    while True:
        print("\nYoutube manager app with DB\n")
        print("1. List videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit")

        choice=input("Enter your choice: ")
        if choice == '1':
            list_videos()
        elif choice == '2':
            name=input("Enter the video name: ")
            time=input("Enter the video duration: ")
            add_video(name,time)
        elif choice == '3':
            vid=input("Enter video id to update: ")
            name=input("Enter the video name: ")
            time=input("Enter the video duration: ")
            update_video(vid,name,time)
        elif choice == '4':
            vid=input("Enter video id to delete: ")
            delete_video(vid)
        elif choice=='5':
            break
        else:
            print("Invalid Choice")
    conn.close()

if __name__ == "__main__":
    main()