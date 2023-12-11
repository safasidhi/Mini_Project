from flask import *
from database import *
import os

user=Blueprint("user",__name__)

@user.route("user_home")
def user_home():
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

    q4="SELECT * FROM `medicine`"
    res4=select(q4)
    data['med_view']=res4

    from datetime import datetime

    current_date = datetime.now().date()
    print("Current date:", current_date)
    data['current_date']=str(current_date)

    if res4:
        for i in res4:
            
            if data['current_date'] > i['exp_date']:
                print(i['exp_date'],"hhhh")
                qq="UPDATE `medicine` SET `status`='Not-Available' WHERE `exp_date`='%s'"%(i['exp_date'])
                update(qq)



    return render_template("user_home.html",data=data)  


@user.route("user_upload_prescription",methods=['get','post'])
def user_upload_prescription():
    data={}
    if 'upl' in request.form:
        title=request.form['title'].replace("'", "''")
        image=request.files['pre_file']

        # Ensure the 'uploads' directory exists
        upload_folder = 'static/upload_prescription/'
        os.makedirs(upload_folder, exist_ok=True)

        # Save the uploaded file to the 'uploads' directory
        image_path = os.path.join(upload_folder, "Pre_"+image.filename)
        image.save(image_path)
        print(image_path)
        im=image_path.replace("'", "''")
        q="""INSERT INTO `upload_prescription`(`prescription_id`, `user_id`, `title`, `file`, `date`, `status`) 
VALUES (null,'%s','%s','%s',curdate(),'Pending')"""%(session['user_id'],title,im)
        print(q)
        insert(q)

        return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); background-color: #4CAF50; color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3>Successfully Uploaded 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'user_upload_prescription';
        }, 2000); // Redirect after 2 seconds
    </script>
"""

    return render_template("user_upload_prescription.html",data=data)

@user.route("user_view_my_prescriptions",methods=['get','post'])
def user_view_my_prescriptions():
    data={}
    q="SELECT * FROM `upload_prescription` WHERE `user_id`='%s'"%(session['user_id'])
    res=select(q)
    if res:
        data['view_my_pre']=res

    return render_template("user_view_my_prescriptions.html",data=data)


@user.route("user_view_medicines",methods=['get','post'])
def user_view_medicines():
    data={}
    data['usd']="0"
    prescription_id=request.args['prescription_id']
    st=request.args['st']
    data['prescription_id']=prescription_id
    data['st']=st
    q="SELECT * FROM `upload_pres_medicine` inner join upload_prescription using(prescription_id) INNER JOIN medicine on medicine.medicine_id=upload_pres_medicine.`medcine_id` WHERE `prescription_id`='%s'"%(prescription_id)
  
    res=select(q)
    if res:
        data['view_pre_med']=res
        data['date']=res[0]['date']
        qq="SELECT *,sum(amount) as total_amount FROM `upload_pres_medicine` where `prescription_id`='%s'"%(prescription_id)
        rs=select(qq)
        if rs:
            print("uuuuuuuu")
            data['total_amount']=rs[0]['total_amount']
            qu="select * from user where user_id='%s'"%(res[0]['user_id'])
            print(qu)
            rt=select(qu)
            if rt:
                data['usd']=rt
            else:
                data['usd']="0"
    if 'action' in request.args:
        action=request.args['action']
        total_amount=request.args['total_amount']
        prescription_id=request.args['prescription_id']
        st=request.args['st']
    else:
        action=None
    if action=="user_cod":
        qq="UPDATE `upload_prescription` SET `status`='COD' WHERE `prescription_id`='%s'"%(prescription_id)
        update(qq)
        return redirect(url_for("user.user_view_my_prescriptions"))
        

    return render_template("user_view_medicines.html",data=data)



@user.route("user_make_payment",methods=['get','post'])
def user_make_payment():
    data={}
    prescription_id=request.args['prescription_id']
    total_amount=request.args['total_amount']
    data['total_amount']=total_amount
    if 'pay' in request.form:
        q="""INSERT INTO `payment`(`payment_id`, `prescription_id`, `amount`, `date`) 
VALUES (null,'%s','%s',curdate())"""%(prescription_id,total_amount)
        insert(q)
        qq="UPDATE `upload_prescription` SET `status`='Paid' WHERE `prescription_id`='%s'"%(prescription_id)
        update(qq)
        return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); background-color: #4CAF50; color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3>Successfully Paid 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'user_view_my_prescriptions';
        }, 2000); // Redirect after 2 seconds
    </script>
"""

    return render_template("user_make_payment.html",data=data)

 
@user.route('/filter_data', methods=['POST'])
def filter_data():
    data = {}
    from datetime import datetime

    from datetime import datetime, timedelta

    # Get the current date and time
    current_date = datetime.now()

    # Calculate yesterday's date
    yesterday = current_date - timedelta(days=1)

    # Extract the date from the datetime object
    yesterday_date = yesterday.date()

    print("Yesterday's date:", yesterday_date)


    selected_value = request.form.get('filter')
    print("cdcvgvghds", selected_value)

    if selected_value == "today":
        q = "SELECT * FROM `upload_prescription` WHERE `user_id`='%s' and date=curdate()" % (session['user_id'])
        res = select(q)
        if res:
            data['view_my_pre'] = res
            return jsonify({'status': 'success', 'data': data.get('view_my_pre', [])})
        else:
            return jsonify({'status': 'failed', 'data': data.get('view_my_pre', [])})
    if selected_value == "yesterday":
        q = "SELECT * FROM `upload_prescription` WHERE `user_id`='%s' and date='%s'" % (session['user_id'],yesterday_date)
        res = select(q)
        if res:
            data['view_my_pre'] = res
            return jsonify({'status': 'success', 'data': data.get('view_my_pre', [])})
        else:
            return jsonify({'status': 'failed', 'data': data.get('view_my_pre', [])})
    if selected_value == "all":
        q = "SELECT * FROM `upload_prescription` WHERE `user_id`='%s'" % (session['user_id'])
        res = select(q)
        if res:
            data['view_my_pre'] = res
            return jsonify({'status': 'success', 'data': data.get('view_my_pre', [])})
        else:
            return jsonify({'status': 'failed', 'data': data.get('view_my_pre', [])})



@user.route("user_complaints",methods=['get','post'])
def user_complaints():
    data={}
    if 'upl' in request.form:
        title=request.form['title'].replace("'", "''")
        desc=request.form['desc'].replace("'", "''")
        qs="""INSERT INTO `complaints`(`complaint_id`, `user_id`, `title`, `description`, `reply`, `date`) 
        VALUES (null,'%s','%s','%s','Pending',curdate())"""%(session['user_id'],title,desc)
        insert(qs)
   
        return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); background-color: #4CAF50; color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3>Successfully Send 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'user_complaints';
        }, 2000); // Redirect after 2 seconds
    </script>
"""

    qq="select * from complaints where user_id='%s' order by complaint_id desc"%(session['user_id'])
    res=select(qq)
    data['view_com']=res

    return render_template("user_complaints.html",data=data)



@user.route("user_review",methods=['get','post'])
def user_review():
    data={}
    if 'upl' in request.form:
        desc=request.form['desc'].replace("'", "''")
        qs="""INSERT INTO `review`
        VALUES (null,'%s','%s',curdate())"""%(session['user_id'],desc)
        insert(qs)
   
        return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); background-color: #4CAF50; color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3>Successfully Send 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'user_review';
        }, 2000); // Redirect after 2 seconds
    </script>
"""

    qq="select * from review where user_id='%s'"%(session['user_id'])
    res=select(qq)
    if res:
        data['view_com']=res

    if 'upl_up' in request.form:
        desc=request.form['desc'].replace("'", "''")
        qs="update review set review_des='%s' where user_id='%s'"%(desc,session['user_id'])
        update(qs)
   
        return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); background-color: #4CAF50; color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3>Successfully Updated 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'user_review';
        }, 2000); // Redirect after 2 seconds
    </script>
"""

    return render_template("user_review.html",data=data)