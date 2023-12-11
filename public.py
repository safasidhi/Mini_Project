from flask import *
from database import *

public=Blueprint("public",__name__)

@public.route("/",methods=['get','post'])
def index():
    data={}
    q="SELECT *,count(`medicine_id`) as med_count FROM `medicine`"
    res=select(q)
    data['med_c']=res

    q1="SELECT *,count(payment_id) as tsales FROM `payment`"
    res1=select(q1)
    data['tsales']=res1

    q2="SELECT *,count(user_id) as user_count FROM `user`"
    res2=select(q2)
    data['user_count']=res2

    q3="SELECT *,count(complaint_id) as com_count FROM `complaints`"
    res3=select(q3)
    data['com_count']=res3
    
    return render_template("index.html",data=data)


@public.route("/login",methods=['get','post'])
def login():
    data={}

    q="SELECT *,count(`medicine_id`) as med_count FROM `medicine`"
    res=select(q)
    data['med_c']=res

    q1="SELECT *,count(payment_id) as tsales FROM `payment`"
    res1=select(q1)
    data['tsales']=res1

    q2="SELECT *,count(user_id) as user_count FROM `user`"
    res2=select(q2)
    data['user_count']=res2

    q3="SELECT *,count(complaint_id) as com_count FROM `complaints`"
    res3=select(q3)
    data['com_count']=res3


    if 'login' in request.form:
        username=request.form['email']
        password=request.form['passw']
        print("chbsdghfdsgc")

        q="select * from login where username='%s' and password='%s'"%(username,password)
        res=select(q)
        if res:
            session['login_id']=res[0]['login_id']
            if res[0]['usertype']=="admin":
                return redirect(url_for("admin.admin_home"))
            if res[0]['usertype']=="User":
                qq="select * from user where login_id='%s'"%(session['login_id'])
                res1=select(qq)
                if res1:
                    session['user_id']=res1[0]['user_id']
                    return redirect(url_for("user.user_home"))
           
        else:
            return "<script>alert='Invalid Username or Password';window.location='/';</script>"
    return render_template("login.html",data=data)


@public.route("/check_username", methods=['GET'])
def check_username():
    username = request.args.get('username')

    # Perform the check in the database
    q = "select * from login where username='%s'" % (username)
    res = select(q)

    if not res:
        return "Username is available"
    else:
        return "Username is already taken"



@public.route("/user_reg",methods=['get','post'])
def user_reg():
    data={}
    q="SELECT *,count(`medicine_id`) as med_count FROM `medicine`"
    res=select(q)
    data['med_c']=res

    q1="SELECT *,count(payment_id) as tsales FROM `payment`"
    res1=select(q1)
    data['tsales']=res1

    q2="SELECT *,count(user_id) as user_count FROM `user`"
    res2=select(q2)
    data['user_count']=res2

    q3="SELECT *,count(complaint_id) as com_count FROM `complaints`"
    res3=select(q3)
    data['com_count']=res3

    if 'reg' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        phone=request.form['phone']
        username=request.form['email']
        password=request.form['passw']
        print("chbsdghfdsgc")

        q="select * from login where username='%s' "%(username)
        res=select(q)
        if not res:
            q="insert into login values(null,'%s','%s','User')"%(username,password)
            id=insert(q)
            qq="insert into user values(null,'%s','%s','%s','%s','%s')"%(id,fname,lname,phone,username)
            insert(qq)
            return redirect(url_for("public.login"))
           
        else:
            return "<script>alert='Invalid Username or Password';window.location='/user_reg';</script>"
    return render_template("user_reg.html",data=data)