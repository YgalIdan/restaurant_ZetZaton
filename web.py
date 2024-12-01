from flask import Flask, render_template, url_for

web = Flask(__name__)

menu_first = [
    {"name": "סלט ארטישוק פטריות טריים, שרי ופסטו", "price": 45},
    {"name": "סלט גרגיר אבוקדו, רימונים ותפוח עץ", "price": 45},
    {"name": "סלט סלרי עם מנגו וחמצויות", "price": 45},
    {"name": "טאבולה ערק ורימונים", "price": 45},
    {"name": "יווני זיתים שחורים וגבינה ברנזה", "price": 45},
    {"name": "שרי צבעים עם חריף אגוזים", "price": 45},
    {"name": "סלט נבטים ותפוזים", "price": 45},
    {"name": "סלט פלחיה עם צנוברים", "price": 45},
    {"name": "סלט לבבות חסה עם פרמזן ורוטב ויניגרט", "price": 45}
]
menu_second = [
    {"name": "מיקס בצקים", "price": 8},
    {"name": "קרפציו פילה עגל פרמיזן צנוברים חומץ בלסמי ושמן זית", "price": 65},
    {"name": "דפי סינטה עגלה במילוי גאודה מעושנת ובזיליקום ברוטב פטריות או שמנת או יין", "price": 79},
    {"name": "קובה נייה מסורתית", "price": 85},
    {"name": "מיקס פירות ים", "price": 95},
    {"name": "סלסיסו הבית ברוטב שום לימון", "price": 55},
    {"name": "לשון עגל בתנור", "price": 65},
    {"name": "פטריות במילוי גבינה ורוטב שמנת", "price": 65},
    {"name": "קרפצו חציל עם גבינת פטה", "price": 45},
    {"name": "רצועות פילה או עוף שום לימון", "price": 65},
    {"name": "רול סאג במילוי מסחן עוף", "price": 10},
    {"name": "טורטיה קבב", "price": 60},
    {"name": "טרטר עגל", "price": 75},
]
menu_main = [
    {"name": "כתף כבש במילוי פירות יבשים או אורז צנוברים", "price": 0},
    {"name": "פילה עגל בתנור במילוי רימונים ערמונים ארטישוק", "price": 0},
    {"name": "עוף שלם בלי עצמות במילוי אורז ובשר", "price": 0},
    {"name": "צוואר כבש ממולא", "price": 0},
    {"name": "פילה עגל ברוטב שמנת פטריות או יין", "price": 0},
    {"name": "אוסובוקו כבש ברוטב יין", "price": 0},
    {"name": "מנסף כבש קלאסי", "price": 0},
    {"name": "דג סלמון שלם בתנור", "price": 0}
]


@web.route('/')
def index():
    return render_template("index.html", menuF=menu_first, menuS=menu_second, menuM=menu_main)

if __name__ == '__main__':
    web.run(host="10.0.0.32", port=6789, debug=True)