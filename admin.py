from flask import *
from database import *
import os

admin=Blueprint("admin",__name__)

@admin.route("admin_home")
def admin_home():
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

    return render_template("admin_home.html",data=data)  



@admin.route("admin_manage_medicine",methods=['get','post'])
def admin_manage_medicine():
    data={}
    from datetime import datetime

    current_date = datetime.now().date()
    print("Current date:", current_date)
    data['current_date']=str(current_date)
    
    
    if "add" in request.form:
        mname=request.form['mname']
        mdes=request.form['mdes']
        price=request.form['price']
        exdate=request.form['exdate']
        stock=request.form['stock']
        image=request.files['image']

        # Ensure the 'uploads' directory exists
        upload_folder = 'static/uploads/'
        os.makedirs(upload_folder, exist_ok=True)

        # Save the uploaded file to the 'uploads' directory
        image_path = os.path.join(upload_folder, mname+"_"+image.filename)
        image.save(image_path)
        print(image_path)
        
        q="""INSERT INTO `medicine`(`medicine_id`, `name`, `description`, `price`, `exp_date`, `stock`, `image`, `status`) 
        VALUES (null,'%s','%s','%s','%s','%s','%s','NA')"""%(mname,mdes,price,exdate,stock,image_path)
        insert(q)
        
        return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); background-color: #4CAF50; color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3>Successfully Added 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'admin_manage_medicine';
        }, 2000); // Redirect after 2 seconds
    </script>
"""

    q="select * from medicine"
    res=select(q)
    data['view_med']=res

    if "action" in request.args:
        action=request.args['action']
        id=request.args['id']
        data['id']=id
    else:
        action=None
    if action=="change_price":
        data['change_price']="change_price"
    if action=="update_stock":
        data['update_stock']="update_stock"
    if action=="update_status":
        data['update_status']="update_status"
    return render_template("admin_manage_medicine.html",data=data)  



@admin.route('/update_price', methods=['POST'])
def update_price():
    medicine_id = request.form.get('id')
    new_price = request.form.get('new_price')
    print("gggggg")

    q="update medicine set price='%s' where medicine_id='%s'"%(new_price,medicine_id)
    print(q)
    update(q)

    return jsonify({'status': 'success'})

@admin.route('/update_stock', methods=['POST'])
def update_stock():
    medicine_id = request.form.get('id')
    new_stock = request.form.get('new_stock')
    print("sssss")

    q="update medicine set stock='%s' where medicine_id='%s'"%(new_stock,medicine_id)
    print(q)
    update(q)
    return jsonify({'status': 'success'})

@admin.route('/update_status', methods=['POST'])
def update_status():
    medicine_id = request.form.get('id')
    new_status = request.form.get('new_status')
    print("sssss")

    q="update medicine set status='%s' where medicine_id='%s'"%(new_status,medicine_id)
    print(q)
    update(q)
    return jsonify({'status': 'success'})





@admin.route("admin_view_complaints",methods=['get','post'])
def admin_view_complaints():
    data={}
    qq="select * from complaints inner join user using(user_id) order by complaint_id desc"
    res=select(qq)
    data['compl']=res

    return render_template("admin_view_complaints.html",data=data)  




@admin.route("submit_reply", methods=['POST'])
def submit_reply():
    complaint_id = request.form.get('complaint_id')
    reply = request.form.get('rp')

    q="UPDATE `complaints` SET `reply`='%s' WHERE complaint_id='%s'"%(reply,complaint_id)
    update(q)
    
    # Perform database update to save the reply based on the complaint_id
    
    # Redirect back to the view complaints page
    return """
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); background-color: #4CAF50; color: white; padding: 20px; text-align: center; border-radius: 20px;">
            <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
            <h3>Successfully Sent 😄</h3>
        </div>
        <script>
            setTimeout(function() {
                window.location.href = 'admin_view_complaints';
            }, 2000); // Redirect after 2 seconds
        </script>
    """




@admin.route("admin_view_prescription",methods=['get','post'])
def admin_view_prescription():
    data={}

    qq="select * from upload_prescription inner join user using(user_id) where date=curdate() order by prescription_id desc"
    res=select(qq)
    data['files']=res

    # qq="select * from upload_prescription inner join user using(user_id) order by prescription_id desc"
    # res=select(qq)
    # data['files']=res

    if 'action' in request.args:
        action=request.args['action']
        prescription_id=request.args['prescription_id']
    else:
        action=None

    if action=="tday":
        qq="select * from upload_prescription inner join user using(user_id) where date=curdate() order by prescription_id desc"
        res=select(qq)
        data['files']=res
    if action=="prevd":
        qq="select * from upload_prescription inner join user using(user_id) where date!=curdate() order by prescription_id desc"
        res=select(qq)
        data['files']=res


    if action=="reject":
        q="update upload_prescription set status='Rejected' where prescription_id='%s'"%(prescription_id)
        update(q)
        return """
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); background-color: #4CAF50; color: white; padding: 20px; text-align: center; border-radius: 20px;">
            <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
            <h3>Rejected </h3>
        </div>
        <script>
            setTimeout(function() {
                window.location.href = 'admin_view_prescription';
            }, 2000); // Redirect after 2 seconds
        </script>
    """
    
    if 'ccoodd' in request.args:
        ccoodd=request.args['ccoodd']
        prescription_id=request.args['prescription_id']
        status=request.args['status']
    else:
        ccoodd=None
        
    if ccoodd=="cod_rec":
        qa="UPDATE `upload_prescription` SET `status`='Paid' WHERE `prescription_id`='%s'"%(prescription_id)
        update(qa)
        q="SELECT *,SUM(`amount`) AS total_amount FROM `upload_pres_medicine` WHERE `prescription_id`='%s'"%(prescription_id)
        rs=select(q)
        q="""INSERT INTO `payment`(`payment_id`, `prescription_id`, `amount`, `date`) 
VALUES (null,'%s','%s',curdate())"""%(prescription_id,rs[0]['total_amount'])
        insert(q)
        return redirect(url_for("admin.admin_view_prescription"))

    return render_template("admin_view_prescription.html",data=data)  




@admin.route("admin_add_prescription_medicine",methods=['get','post'])
def admin_add_prescription_medicine():
    data={}
    prescription_id=request.args['prescription_id']
    pre_status=request.args['status']
    data['pre_status']=pre_status
    q="SELECT * FROM `medicine` where status='Available'"
    res=select(q)
    data['med']=res

    if "add" in request.form:
        med=request.form['med']
        qnty=request.form['qnty']
        tamount=request.form['tamount']
        q="""INSERT INTO `upload_pres_medicine`
        (`up_pres_medicine_id`, `prescription_id`, `medcine_id`, `quantity`, `amount`) 
        VALUES (null,'%s','%s','%s','%s')"""%(prescription_id,med,qnty,tamount)
        insert(q)
        
        q1="UPDATE `medicine` SET `stock`=`stock`-'%s' WHERE `medicine_id`='%s'"%(qnty,med)
        update(q1)
        return redirect(url_for('admin.admin_add_prescription_medicine', prescription_id=prescription_id,status=pre_status))
    
    qw="SELECT * FROM `upload_pres_medicine` inner join medicine on medicine.medicine_id =  upload_pres_medicine.medcine_id WHERE `prescription_id`='%s'"%(prescription_id)
    ress=select(qw)
    if ress:
        data['view_pre_med']=ress
        qa="SELECT *,SUM(`amount`) as gt FROM `upload_pres_medicine` WHERE `prescription_id`='%s'"%(prescription_id)
        resa=select(qa)
        if resa:
            data['gt']=resa[0]['gt']
        else:
            data['gt']="0"

    if "action" in request.args:
        action=request.args['action']
        medcine_id=request.args['medcine_id']
        up_pres_medicine_id=request.args['up_pres_medicine_id']
        quantity=request.args['quantity']
        prescription_id=request.args['prescription_id']
    else:
        action=None
    if action=="remove":
        qu="DELETE FROM `upload_pres_medicine` WHERE `up_pres_medicine_id`='%s'"%(up_pres_medicine_id)
        delete(qu)
        qu1="UPDATE `medicine` SET `stock`=`stock`+'%s' WHERE `medicine_id`='%s'"%(quantity,medcine_id)
        update(qu1)
        return redirect(url_for('admin.admin_add_prescription_medicine', prescription_id=prescription_id,status=pre_status))
    
    if "submit" in request.form:
        qq="UPDATE `upload_prescription` SET `status`='Accepted' WHERE `prescription_id`='%s'"%(prescription_id)
        update(qq)
        return """
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); background-color: #4CAF50; color: white; padding: 20px; text-align: center; border-radius: 20px;">
            <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
            <h3>Submited </h3>
        </div>
        <script>
            setTimeout(function() {
                window.location.href = 'admin_view_prescription';
            }, 2000); // Redirect after 2 seconds
        </script>
    """
    
    return render_template("admin_add_prescription_medicine.html",data=data)  


@admin.route('med_details', methods=['GET'])
def get_medicine_data():
    medicine_id = request.args.get('medicine_id')
    query = "SELECT * FROM medicine WHERE medicine_id='%s'" % (medicine_id)
    fetched_data = select(query)

    # Return data in JSON format
    return jsonify({
        'medicine_id': fetched_data[0]['medicine_id'],
        'description': fetched_data[0]['description'],
        'price': fetched_data[0]['price'],
        'expDate': fetched_data[0]['exp_date'],
        'stock': fetched_data[0]['stock'],
        'imageSrc': fetched_data[0]['image']
    })



@admin.route("admin_review",methods=['get','post'])
def admin_review():
    data={}
    qq="select * from review inner join user using(user_id) order by review_id desc"
    res=select(qq)
    data['compl']=res
    return render_template("admin_review.html",data=data)  




@admin.route("admin_view_sales_history",methods=['get','post'])
def admin_view_sales_history():
    data={}

    qq="SELECT *,payment.date as date FROM `payment` INNER JOIN upload_prescription using(`prescription_id`) inner join user using(user_id) order by payment_id DESC"
    res=select(qq)
    data['files']=res
    print(qq)

    # qq="select * from upload_prescription inner join user using(user_id) order by prescription_id desc"
    # res=select(qq)
    # data['files']=res

    if 'action' in request.args:
        action=request.args['action']
        prescription_id=request.args['prescription_id']
    else:
        action=None

    if action=="tday":
        qq="SELECT *,payment.date as date FROM `payment` INNER JOIN upload_prescription using(`prescription_id`) inner join user using(user_id) where payment.date=curdate()  order by payment_id DESC"
        res=select(qq)
        data['files']=res
        print(qq)
    if action=="prevd":
        qq="SELECT *,payment.date as date FROM `payment` INNER JOIN upload_prescription using(`prescription_id`) inner join user using(user_id) where payment.date !=curdate()  order by payment_id DESC"
        res=select(qq)
        data['files']=res
        print(qq)


    return render_template("admin_view_sales_history.html",data=data)  






@admin.route("admin_view_users",methods=['get','post'])
def admin_view_users():
    data={}
    qq="select * from user where user_id='%s'"
    res=select(qq)
    data['feedb']=res

    return render_template("admin_view_users.html",data=data)  

