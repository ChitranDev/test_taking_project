#  answer_25 for answer related and question_25 for question related stuff

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/online_test'
db = SQLAlchemy(app)

date_now = datetime.now()

# tables for database

class create_test(db.Model):
    '''school_name, class_of_student, no_of_ques, email, type_of_ques, subject, date'''
    sno = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(100), nullable=False)
    class_of_student = db.Column(db.String(20), nullable=False)
    no_of_ques = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), nullable=True)
    type_of_ques = db.Column(db.String(50), nullable=False)
    subject = db.Column(db.String(20), nullable=False)
    # date = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return 'create_test ' + str(self.sno)

class question_25(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    create_test_sno = db.Column(db.Integer, nullable=False)
    question_no_1 = db.Column(db.String(200), nullable=True)
    question_no_2 = db.Column(db.String(200), nullable=True)
    question_no_3 = db.Column(db.String(200), nullable=True)
    question_no_4 = db.Column(db.String(200), nullable=False)
    question_no_5 = db.Column(db.String(200), nullable=True)
    question_no_6 = db.Column(db.String(200), nullable=True)
    question_no_7 = db.Column(db.String(200), nullable=True)
    question_no_8 = db.Column(db.String(200), nullable=True)
    question_no_9 = db.Column(db.String(200), nullable=True)
    question_no_10 = db.Column(db.String(200), nullable=True)
    question_no_11 = db.Column(db.String(200), nullable=True)
    question_no_12 = db.Column(db.String(200), nullable=True)
    question_no_13 = db.Column(db.String(200), nullable=True)
    question_no_14 = db.Column(db.String(200), nullable=True)
    question_no_15 = db.Column(db.String(200), nullable=True)
    question_no_16 = db.Column(db.String(200), nullable=True)
    question_no_17 = db.Column(db.String(200), nullable=True)
    question_no_18 = db.Column(db.String(200), nullable=True)
    question_no_19 = db.Column(db.String(200), nullable=True)
    question_no_20 = db.Column(db.String(200), nullable=True)
    question_no_21 = db.Column(db.String(200), nullable=True)
    question_no_22 = db.Column(db.String(200), nullable=True)
    question_no_23 = db.Column(db.String(200), nullable=True)
    question_no_24 = db.Column(db.String(200), nullable=True)
    question_no_25 = db.Column(db.String(200), nullable=True)
    marks_no_1 = db.Column(db.Integer, nullable=True)
    marks_no_2 = db.Column(db.Integer, nullable=True)
    marks_no_3 = db.Column(db.Integer, nullable=True)
    marks_no_4 = db.Column(db.Integer, nullable=True)
    marks_no_5 = db.Column(db.Integer, nullable=True)
    marks_no_6 = db.Column(db.Integer, nullable=True)
    marks_no_7 = db.Column(db.Integer, nullable=True)
    marks_no_8 = db.Column(db.Integer, nullable=True)
    marks_no_9 = db.Column(db.Integer, nullable=True)
    marks_no_10 = db.Column(db.Integer, nullable=True)
    marks_no_11 = db.Column(db.Integer, nullable=True)
    marks_no_12 = db.Column(db.Integer, nullable=True)
    marks_no_13 = db.Column(db.Integer, nullable=True)
    marks_no_14 = db.Column(db.Integer, nullable=True)
    marks_no_15 = db.Column(db.Integer, nullable=True)
    marks_no_16 = db.Column(db.Integer, nullable=True)
    marks_no_17 = db.Column(db.Integer, nullable=True)
    marks_no_18 = db.Column(db.Integer, nullable=True)
    marks_no_19 = db.Column(db.Integer, nullable=True)
    marks_no_20 = db.Column(db.Integer, nullable=True)
    marks_no_21 = db.Column(db.Integer, nullable=True)
    marks_no_22 = db.Column(db.Integer, nullable=True)
    marks_no_23 = db.Column(db.Integer, nullable=True)
    marks_no_24 = db.Column(db.Integer, nullable=True)
    marks_no_25 = db.Column(db.Integer, nullable=True)
    

    def __repr__(self):
        return 'question_25 ' + str(self.sno)

class answer_25(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    same_sno_of_test = db.Column(db.Integer, nullable=True, unique=False)
    name = db.Column(db.String(100), nullable=False)
    section = db.Column(db.String(10), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(30), nullable=True)
    subject = db.Column(db.String(12), nullable=True)
    date = db.Column(db.Integer, nullable=False)
    answer_no_1 = db.Column(db.String(200), nullable=True)
    answer_no_2 = db.Column(db.String(200), nullable=True)
    answer_no_3 = db.Column(db.String(200), nullable=True)
    answer_no_4 = db.Column(db.String(200), nullable=False)
    answer_no_5 = db.Column(db.String(200), nullable=True)
    answer_no_6 = db.Column(db.String(200), nullable=True)
    answer_no_7 = db.Column(db.String(200), nullable=True)
    answer_no_8 = db.Column(db.String(200), nullable=True)
    answer_no_9 = db.Column(db.String(200), nullable=True)
    answer_no_10 = db.Column(db.String(200), nullable=True)
    answer_no_11 = db.Column(db.String(200), nullable=True)
    answer_no_12 = db.Column(db.String(200), nullable=True)
    answer_no_13 = db.Column(db.String(200), nullable=True)
    answer_no_14 = db.Column(db.String(200), nullable=True)
    answer_no_15 = db.Column(db.String(200), nullable=True)
    answer_no_16 = db.Column(db.String(200), nullable=True)
    answer_no_17 = db.Column(db.String(200), nullable=True)
    answer_no_18 = db.Column(db.String(200), nullable=True)
    answer_no_19 = db.Column(db.String(200), nullable=True)
    answer_no_20 = db.Column(db.String(200), nullable=True)
    answer_no_21 = db.Column(db.String(200), nullable=True)
    answer_no_22 = db.Column(db.String(200), nullable=True)
    answer_no_23 = db.Column(db.String(200), nullable=True)
    answer_no_24 = db.Column(db.String(200), nullable=True)
    answer_no_25 = db.Column(db.String(200), nullable=True)
    marks_no_1 = db.Column(db.String(200), nullable=True, default='Unchecked')
    marks_no_2 = db.Column(db.String(200), nullable=True, default='Unchecked')
    marks_no_3 = db.Column(db.String(200), nullable=True, default='Unchecked')
    marks_no_4 = db.Column(db.String(200), nullable=True, default='Unchecked')
    marks_no_5 = db.Column(db.String(200), nullable=True, default='Unchecked')
    marks_no_6 = db.Column(db.String(200), nullable=True, default='Unchecked')
    marks_no_7 = db.Column(db.String(200), nullable=True, default='Unchecked')
    marks_no_8 = db.Column(db.String(200), nullable=True, default='Unchecked')
    marks_no_9 = db.Column(db.String(200), nullable=True, default='Unchecked')
    marks_no_10 = db.Column(db.String(200), nullable=True, default='Unchecked')
    marks_no_11 = db.Column(db.String(200), nullable=True, default='Unchecked')
    marks_no_12 = db.Column(db.String(200), nullable=True, default='Unchecked')
    marks_no_13 = db.Column(db.String(200), nullable=True, default='Unchecked')
    marks_no_14 = db.Column(db.String(200), nullable=True, default='Unchecked')
    marks_no_15 = db.Column(db.String(200), nullable=True, default='Unchecked')
    marks_no_16 = db.Column(db.String(200), nullable=True, default='Unchecked')
    marks_no_17 = db.Column(db.String(200), nullable=True, default='Unchecked')
    marks_no_18 = db.Column(db.String(200), nullable=True, default='Unchecked')
    marks_no_19 = db.Column(db.String(200), nullable=True, default='Unchecked')
    marks_no_20 = db.Column(db.String(200), nullable=True, default='Unchecked')
    marks_no_21 = db.Column(db.String(200), nullable=True, default='Unchecked')
    marks_no_22 = db.Column(db.String(200), nullable=True, default='Unchecked')
    marks_no_23 = db.Column(db.String(200), nullable=True, default='Unchecked')
    marks_no_24 = db.Column(db.String(200), nullable=True, default='Unchecked')
    marks_no_25 = db.Column(db.String(200), nullable=True, default='Unchecked')

    def __repr__(self):
        return 'answer_25 ' + str(self.sno)


# flask ROUTEs



# CODE TO MAKE CREATE TEST PAGE- 

# create test (home) page
@app.route("/", methods = ['GET', 'POST'])
def create_test():
    if(request.method=='POST'):
        '''Add entry to the database'''
        school_name = request.form.get('school_name')
        class_of_student = request.form.get('class')
        no_of_ques = request.form.get('no_of_ques')
        email = request.form.get('email')
        type_of_ques = request.form.get('type_of_ques')
        subject = request.form.get('subject')

        # making parameter in upper case
        school_name = school_name.upper()
        subject = subject.upper()
    
        entry = create_test(school_name=school_name, class_of_student=class_of_student,  no_of_ques=no_of_ques, email=email, type_of_ques=type_of_ques, subject=subject )

        db.session.add(entry)
        db.session.commit()
        id = create_test.query.all()[-1].sno

        return redirect(f'/create_question/{id}')  
    else:
        return render_template('create_test.html')

# set questions page
@app.route('/create_question/<string:id>', methods = ['GET', 'POST'])
def create_questions(id): 
  
    teacher_info = create_test.query.filter_by(sno=id).first()

    test = teacher_info.no_of_ques
    test = test.replace('Questions','')
    final_test1 = int(test)
    print(test)

    if(request.method=='POST'):
        '''Add entry to the database'''
        create_test_sno = id
        question_no_1 = request.form.get('question_no_1')
        marks_no_1 = request.form.get('marks_no_1')
        question_no_2 = request.form.get('question_no_2')
        marks_no_2 = request.form.get('marks_no_2')
        question_no_3 = request.form.get('question_no_3')
        marks_no_3 = request.form.get('marks_no_3')
        question_no_4 = request.form.get('question_no_4')
        marks_no_4 = request.form.get('marks_no_4')
        question_no_5 = request.form.get('question_no_5')
        marks_no_5 = request.form.get('marks_no_5')
        question_no_6 = request.form.get('question_no_6')
        marks_no_6 = request.form.get('marks_no_6')
        question_no_7 = request.form.get('question_no_7')
        marks_no_7 = request.form.get('marks_no_7')
        question_no_8 = request.form.get('question_no_8')
        marks_no_8 = request.form.get('marks_no_8')
        question_no_9 = request.form.get('question_no_9')
        marks_no_9 = request.form.get('marks_no_9')
        question_no_10 = request.form.get('question_no_10')
        marks_no_10 = request.form.get('marks_no_10')
        question_no_11 = request.form.get('question_no_11')
        marks_no_11 = request.form.get('marks_no_11')
        question_no_12 = request.form.get('question_no_12')
        marks_no_12 = request.form.get('marks_no_12')
        question_no_13 = request.form.get('question_no_13')
        marks_no_13 = request.form.get('marks_no_13')
        question_no_14 = request.form.get('question_no_14')
        marks_no_14 = request.form.get('marks_no_14')
        question_no_15 = request.form.get('question_no_15')
        marks_no_15 = request.form.get('marks_no_15')
        question_no_16 = request.form.get('question_no_16')
        marks_no_16 = request.form.get('marks_no_16')
        question_no_17 = request.form.get('question_no_17')
        marks_no_17 = request.form.get('marks_no_17')
        question_no_18 = request.form.get('question_no_18')
        marks_no_18 = request.form.get('marks_no_18')
        question_no_19 = request.form.get('question_no_19')
        marks_no_19 = request.form.get('marks_no_19')
        question_no_20 = request.form.get('question_no_20')
        marks_no_20 = request.form.get('marks_no_20')
        question_no_21 = request.form.get('question_no_21')
        marks_no_21 = request.form.get('marks_no_21')
        question_no_22 = request.form.get('question_no_22')
        marks_no_22 = request.form.get('marks_no_22')
        question_no_23 = request.form.get('question_no_23')
        marks_no_23 = request.form.get('marks_no_23')
        question_no_24 = request.form.get('question_no_24')
        marks_no_24 = request.form.get('marks_no_24')
        question_no_25 = request.form.get('question_no_25')
        marks_no_25 = request.form.get('marks_no_25')

        entry_question = question_25(create_test_sno=create_test_sno,question_no_1=question_no_1, question_no_2=question_no_2, question_no_3=question_no_3, question_no_4=question_no_4, question_no_5=question_no_5, question_no_6=question_no_6, question_no_7=question_no_7, question_no_8=question_no_8, question_no_9=question_no_9, question_no_10=question_no_10, question_no_11=question_no_11, question_no_12=question_no_12, question_no_13=question_no_13, question_no_14=question_no_14, question_no_15=question_no_15, question_no_16=question_no_16, question_no_17=question_no_17, question_no_18=question_no_18, question_no_19=question_no_19, question_no_20=question_no_20, question_no_21=question_no_21, question_no_22=question_no_22, question_no_23=question_no_23, question_no_24=question_no_24, question_no_25=question_no_25, marks_no_1=marks_no_1, marks_no_2=marks_no_2, marks_no_3=marks_no_3, marks_no_4=marks_no_4, marks_no_5=marks_no_5, marks_no_6=marks_no_6, marks_no_7=marks_no_7, marks_no_8=marks_no_8, marks_no_9=marks_no_9, marks_no_10=marks_no_10, marks_no_11=marks_no_11, marks_no_12=marks_no_12, marks_no_13=marks_no_13, marks_no_14=marks_no_14,marks_no_15=marks_no_15, marks_no_16=marks_no_16, marks_no_17=marks_no_17, marks_no_18=marks_no_18, marks_no_19=marks_no_19, marks_no_20=marks_no_20, marks_no_21=marks_no_21, marks_no_22 =marks_no_22, marks_no_23=marks_no_23, marks_no_24=marks_no_24, marks_no_25=marks_no_25) 

        db.session.add(entry_question)
        db.session.commit()

        return redirect(f"/successfully_done/{id}")        


    return render_template('create_questions.html', test=final_test1 ,id=id )

# test created successfully
@app.route('/successfully_done/<string:id>')
def test_successfully_created(id):

    questions_paper = create_test.query.filter_by(sno=id).first()

    # 'create_test_sno' of question_25 and 'sno' of create_test are equal
    sno_of_questions_paper_sno = questions_paper.sno
    email_create_test = questions_paper.email

    return render_template('successfully_created_test.html', sno=sno_of_questions_paper_sno,email_create_test=email_create_test)


# CODE TO MAKE GIVE TEST PAGE- 

# online test page (questions and answer submition)
@app.route('/test/<string:id>/', methods = ['GET','POST'])
def give_test(id):

    question = question_25.query.filter_by(create_test_sno=id).first()
    teacher_info = create_test.query.filter_by(sno=id).first()

    no_of_questions = teacher_info.no_of_ques

    # making no_of_question, a list of numbers  
    no_of_questions = no_of_questions.replace('Questions','')
    final_number_of_questions = int(no_of_questions)

    unique_number_for_each_test = id
        
    all_questions=[]
    if final_number_of_questions == 5:
        all_questions.append(f'1 {question.question_no_1}                   Marks:{question.marks_no_1} ')
        all_questions.append(f'2 {question.question_no_2}                   Marks:{question.marks_no_2} ')
        all_questions.append(f'3 {question.question_no_3}                   Marks:{question.marks_no_3} ')
        all_questions.append(f'4 {question.question_no_4}                  Marks:{question.marks_no_4} ')
        all_questions.append(f'5 {question.question_no_5}                   Marks:{question.marks_no_5} ')

    if final_number_of_questions == 10:
        all_questions.append(f'1 {question.question_no_1}                   Marks:{question.marks_no_1} ')
        all_questions.append(f'2 {question.question_no_2}                   Marks:{question.marks_no_2} ')
        all_questions.append(f'3 {question.question_no_3}                   Marks:{question.marks_no_3} ')
        all_questions.append(f'4 {question.question_no_4}                   Marks:{question.marks_no_4} ')
        all_questions.append(f'5 {question.question_no_5}                   Marks:{question.marks_no_5} ')
        all_questions.append(f'6 {question.question_no_6}                   Marks:{question.marks_no_6} ')
        all_questions.append(f'7 {question.question_no_7}                   Marks:{question.marks_no_7} ')
        all_questions.append(f'8 {question.question_no_8}                   Marks:{question.marks_no_8} ')
        all_questions.append(f'9 {question.question_no_9}                   Marks:{question.marks_no_9} ')
        all_questions.append(f'10 {question.question_no_10}                   Marks:{question.marks_no_10} ')

    if final_number_of_questions == 15:
        all_questions.append(f'1 {question.question_no_1}                    {question.marks_no_1}-Marks Question')
        all_questions.append(f'2 {question.question_no_2}                   {question.marks_no_2}-Marks Question')
        all_questions.append(f'3 {question.question_no_3}                   {question.marks_no_3}-Marks Question')
        all_questions.append(f'4 {question.question_no_4}                   {question.marks_no_4}-Marks Question')
        all_questions.append(f'5 {question.question_no_5}                   {question.marks_no_5}-Marks Question')
        all_questions.append(f'6 {question.question_no_6}                   {question.marks_no_6}-Marks Question')
        all_questions.append(f'7 {question.question_no_7}                  {question.marks_no_7}-Marks Question')
        all_questions.append(f'8 {question.question_no_8}                   {question.marks_no_8}-Marks Question')
        all_questions.append(f'9 {question.question_no_9}                   {question.marks_no_9}-Marks Question')
        all_questions.append(f'10 {question.question_no_10}                   {question.marks_no_10}-Marks Question ')
        all_questions.append(f'11 {question.question_no_11}                   {question.marks_no_11}-Marks Question ')
        all_questions.append(f'12 {question.question_no_12}                   {question.marks_no_12}-Marks Question ')
        all_questions.append(f'13 {question.question_no_13}                   {question.marks_no_13}-Marks Question ')
        all_questions.append(f'14 {question.question_no_14}                   {question.marks_no_14}-Marks Question ')
        all_questions.append(f'15 {question.question_no_15}                   {question.marks_no_15}-Marks Question ')

    if final_number_of_questions == 20:
        all_questions.append(f'1 {question.question_no_1}                   Marks:{question.marks_no_1} ')
        all_questions.append(f'2 {question.question_no_2}                   Marks:{question.marks_no_2} ')
        all_questions.append(f'3 {question.question_no_3}                   Marks:{question.marks_no_3} ')
        all_questions.append(f'4 {question.question_no_4}                   Marks:{question.marks_no_4} ')
        all_questions.append(f'5 {question.question_no_5}                   Marks:{question.marks_no_5} ')
        all_questions.append(f'6 {question.question_no_6}                   Marks:{question.marks_no_6} ')
        all_questions.append(f'7 {question.question_no_7}                   Marks:{question.marks_no_7} ')
        all_questions.append(f'8 {question.question_no_8}                   Marks:{question.marks_no_8} ')
        all_questions.append(f'9 {question.question_no_9}                   Marks:{question.marks_no_9} ')
        all_questions.append(f'10 {question.question_no_10}                   Marks:{question.marks_no_10} ')
        all_questions.append(f'11 {question.question_no_11}                   Marks:{question.marks_no_11} ')
        all_questions.append(f'12 {question.question_no_12}                   Marks:{question.marks_no_12} ')
        all_questions.append(f'13 {question.question_no_13}                   Marks:{question.marks_no_13} ')
        all_questions.append(f'14 {question.question_no_14}                   Marks:{question.marks_no_14} ')
        all_questions.append(f'15 {question.question_no_15}                   Marks:{question.marks_no_15} ')
        all_questions.append(f'16 {question.question_no_16}                   Marks:{question.marks_no_16} ')
        all_questions.append(f'17 {question.question_no_17}                   Marks:{question.marks_no_17} ')
        all_questions.append(f'18 {question.question_no_18}                   Marks:{question.marks_no_18} ')
        all_questions.append(f'19 {question.question_no_19}                   Marks:{question.marks_no_19} ')
        all_questions.append(f'20 {question.question_no_20}                   Marks:{question.marks_no_20} ')

    if final_number_of_questions == 25:
        all_questions.append(f'1 {question.question_no_1}                   Marks:{question.marks_no_1} ')
        all_questions.append(f'2 {question.question_no_2}                   Marks:{question.marks_no_2} ')
        all_questions.append(f'3 {question.question_no_3}                   Marks:{question.marks_no_3} ')
        all_questions.append(f'4 {question.question_no_4}                   Marks:{question.marks_no_4} ')
        all_questions.append(f'5 {question.question_no_5}                   Marks:{question.marks_no_5} ')
        all_questions.append(f'6 {question.question_no_6}                   Marks:{question.marks_no_6} ')
        all_questions.append(f'7 {question.question_no_7}                   Marks:{question.marks_no_7} ')
        all_questions.append(f'8 {question.question_no_8}                   Marks:{question.marks_no_8} ')
        all_questions.append(f'9 {question.question_no_9}                   Marks:{question.marks_no_9} ')
        all_questions.append(f'10 {question.question_no_10}                   Marks:{question.marks_no_10} ')
        all_questions.append(f'11 {question.question_no_11}                   Marks:{question.marks_no_11} ')
        all_questions.append(f'12 {question.question_no_12}                   Marks:{question.marks_no_12} ')
        all_questions.append(f'13 {question.question_no_13}                   Marks:{question.marks_no_13} ')
        all_questions.append(f'14 {question.question_no_14}                   Marks:{question.marks_no_14} ')
        all_questions.append(f'15 {question.question_no_15}                   Marks:{question.marks_no_15} ')
        all_questions.append(f'16 {question.question_no_16}                   Marks:{question.marks_no_16} ')
        all_questions.append(f'17 {question.question_no_17}                   Marks:{question.marks_no_17} ')
        all_questions.append(f'18 {question.question_no_18}                   Marks:{question.marks_no_18} ')
        all_questions.append(f'19 {question.question_no_19}                   Marks:{question.marks_no_19} ')
        all_questions.append(f'20 {question.question_no_20}                   Marks:{question.marks_no_20} ')
        all_questions.append(f'21 {question.question_no_21}                   Marks:{question.marks_no_21} ')
        all_questions.append(f'22 {question.question_no_22}                   Marks:{question.marks_no_22} ')
        all_questions.append(f'23 {question.question_no_23}                   Marks:{question.marks_no_23} ')
        all_questions.append(f'24 {question.question_no_24}                   Marks:{question.marks_no_24} ')
        all_questions.append(f'25 {question.question_no_25}                   Marks:{question.marks_no_25} ')

    if(request.method=='POST'):
        '''Add entry to the database'''

        name = request.form.get('name')
        section = request.form.get('section')
        phone = request.form.get('phone')
        email = request.form.get('email')
        subject = request.form.get('subject')
        answer_no_1 = request.form.get('answer_no_1 ')
        answer_no_2 = request.form.get('answer_no_2 ')
        answer_no_3 = request.form.get('answer_no_3 ')
        answer_no_4 = request.form.get('answer_no_4 ')
        answer_no_5 = request.form.get('answer_no_5 ')
        answer_no_6 = request.form.get('answer_no_6 ')
        answer_no_7 = request.form.get('answer_no_7 ')
        answer_no_8 = request.form.get('answer_no_8 ')
        answer_no_9 = request.form.get('answer_no_9 ')
        answer_no_10 = request.form.get('answer_no_10')
        answer_no_11 = request.form.get('answer_no_11')
        answer_no_12 = request.form.get('answer_no_12')
        answer_no_13 = request.form.get('answer_no_13')
        answer_no_14 = request.form.get('answer_no_14')
        answer_no_15 = request.form.get('answer_no_15')
        answer_no_16 = request.form.get('answer_no_16')
        answer_no_17 = request.form.get('answer_no_17')
        answer_no_18 = request.form.get('answer_no_18')
        answer_no_19 = request.form.get('answer_no_19')
        answer_no_20 = request.form.get('answer_no_20')
        answer_no_21 = request.form.get('answer_no_21')
        answer_no_22 = request.form.get('answer_no_22')
        answer_no_23 = request.form.get('answer_no_23')
        answer_no_24 = request.form.get('answer_no_24')
        answer_no_25 = request.form.get('answer_no_25')
        marks_no_1 = request.form.get('marks_no_1')
        marks_no_2 = request.form.get('marks_no_2')
        marks_no_3 = request.form.get('marks_no_3')
        marks_no_4 = request.form.get('marks_no_4')
        marks_no_5 = request.form.get('marks_no_5')
        marks_no_6 = request.form.get('marks_no_6')
        marks_no_7 = request.form.get('marks_no_7')
        marks_no_8 = request.form.get('marks_no_8')
        marks_no_9 = request.form.get('marks_no_9')
        marks_no_10 = request.form.get('marks_no_10')
        marks_no_11 = request.form.get('marks_no_11')
        marks_no_12 = request.form.get('marks_no_12')
        marks_no_13 = request.form.get('marks_no_13')
        marks_no_14 = request.form.get('marks_no_14')
        marks_no_15 = request.form.get('marks_no_15')
        marks_no_16 = request.form.get('marks_no_16')
        marks_no_17 = request.form.get('marks_no_17')
        marks_no_18 = request.form.get('marks_no_18')
        marks_no_19 = request.form.get('marks_no_19')
        marks_no_20 = request.form.get('marks_no_20')
        marks_no_21 = request.form.get('marks_no_21')
        marks_no_22 = request.form.get('marks_no_22')
        marks_no_23 = request.form.get('marks_no_23')
        marks_no_24 = request.form.get('marks_no_24')
        marks_no_25 = request.form.get('marks_no_25')
        

        ''' sno, same_identifier, name, section, phone, email, subject date '''

        same_identifier = id

        entry_answer = answer_25(  same_sno_of_test=same_identifier, name=name, section=section, phone=phone, email=email, subject=subject, date=date_now , answer_no_1=answer_no_1, answer_no_2=answer_no_2, answer_no_3=answer_no_3, answer_no_4=answer_no_4, answer_no_5=answer_no_5, answer_no_6=answer_no_6, answer_no_7=answer_no_7, answer_no_8=answer_no_8, answer_no_9=answer_no_9, answer_no_10=answer_no_10, answer_no_11=answer_no_11, answer_no_12=answer_no_12, answer_no_13=answer_no_13, answer_no_14=answer_no_14, answer_no_15=answer_no_15, answer_no_16=answer_no_16, answer_no_17=answer_no_17, answer_no_18=answer_no_18, answer_no_19=answer_no_19, answer_no_20=answer_no_20, answer_no_21=answer_no_21, answer_no_22=answer_no_22, answer_no_23=answer_no_23, answer_no_24=answer_no_24, answer_no_25=answer_no_25) 

        db.session.add(entry_answer)
        db.session.commit()

        sno = answer_25.query.all()[-1].sno
        print(sno)
        sno = str(sno)

        return redirect(f'/test_submitted/{sno}')
    
    return render_template('question_paper.html',all_questions=all_questions, id=id, teacher_info=teacher_info)

# test submitted successfully
@app.route('/test_submitted/<string:id>')
def test_submitted(id):
    student_info = answer_25.query.filter_by(sno=id).first()
    name = student_info.name
    email = student_info.email

    return render_template('test_submitted.html', name=name, email=email)


# CODE TO CHECK THE ANSWERS SUBMITTED BY STUDENTS-

# details of students (who submited the test)
@app.route('/check_answer/<string:id>')
def check_answer(id):
    students_info = answer_25.query.filter_by(same_sno_of_test=id).all()
    for student_info in students_info:
        print(student_info.name)



app.run(debug=True)



       