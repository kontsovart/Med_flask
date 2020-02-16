from app_config import *
from models import *
from flask import render_template, request, abort, session, redirect, url_for
from flask_login import LoginManager, login_required
import json, os


def select_condition_or_description(name):
    if name == 'condition':
        return Condition
    elif name == 'description':
        return Description
    else:
        return None


def select_table(name):
    if name == 'Condition':
        return redirect(url_for('add_to_condition', name='condition'))
    elif name == 'Description':
        return redirect(url_for('add_to_condition', name='description'))
    elif name == 'Transition':
        return redirect(url_for('add_to_transition'))
    else:
        return redirect(url_for('add_to_state'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['password'] == 'password' and request.form['username'] == 'admin':
            session['logged_in'] = True
            return redirect(url_for('admin_main'))
        else:
            abort(401)
    return render_template('login.html')


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))


@app.route('/admin', methods=['POST', 'GET'])
def admin_main():
    if request.method == 'POST':
        return select_table(request.form['table'])
    return render_template('admin_main.html', tables=['Condition', 'Description', 'State', 'Transition'])


@app.route('/admin/transition', methods=['POST', 'GET'])
def add_to_transition():
    if request.method == 'POST':
        print(request.form['condition'], type(request.form['condition']))
        if request.form["button"] == 'Delete':
            db.session.query(Transition).filter_by(condition=request.form['condition'], next_state=request.form['next_state']).delete()
            db.session.commit()
        elif request.form["button"] == 'Submit':
            a = Transition(request.form['next_state'], request.form['condition'])
            print(a, request.form['condition'])
            db.session.add(a)
            db.session.commit()
        else:
            a = db.session.query(Transition).filter_by(next_state=request.form['next_state'], condition=request.form['condition']).all()
            for item in a:
                item.condition = request.form['update_condition']
                item.next_state = request.form['update_state']
            # print(update(Transition).values(condition=request.form['update_condition'], next_state=request.form['update_state']).where(Transition.condition == request.form['condition'] and Transition.next_state == request.form['next_state']))
            db.session.commit()
    q = db.session.query(Transition).all()
    print(q)
    return render_template('test_transition.html', data=[i.__dict__ for i in q])


@app.route('/admin/state', methods=['POST', 'GET'])
def add_to_state():
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        prev_states = [int(i) for i in request.form.getlist('prev_states')]
        transitions = [int(i) for i in request.form.getlist('transitions')]
        description = request.form['description']
        if request.form['button'] == 'Save':
            a = State(transitions=[db.session.query(Transition).filter_by(id=i).first() for i in transitions],
                      prev_states=[db.session.query(State).filter_by(id=i).first() for i in prev_states],
                      description=description)
            db.session.add(a)
            db.session.commit()
        if request.form['button'] == 'Delete':
            try:
                x = db.session.query(State).get(request.form['new_state'])
                print(x)
                db.session.delete(x)
                db.session.commit()
            except:
                pass
        if request.form['button'] == 'Update':
            try:
                a = db.session.query(State).filter_by(id=request.form['new_state']).one()
                a.transitions = [db.session.query(Transition).filter_by(id=i).first() for i in transitions]
                a.prev_states = [db.session.query(State).filter_by(id=i).first() for i in prev_states]
                a.description = description
                db.session.commit()
            except:
                pass
    trans = db.session.query(Transition).all()
    desc = db.session.query(Description).all()
    states = db.session.query(State).all()
    for s in states:
        print(s)
    return render_template('test_state.html', prev_states=[i.__dict__ for i in states], description=[i.__dict__ for i in desc], transitions=[i.__dict__ for i in trans])


@app.route('/admin/<name>', methods=['POST', 'GET'])
def add_to_condition(name):
    if name != 'condition' and name != 'description':
        abort(404)
    if request.method == 'POST':
        info = request.form['info']
        data = request.form['data']
        if request.form['button'] == 'Delete':
            x = db.session.query(select_condition_or_description(name)).get(data)
            db.session.delete(x)
            db.session.commit()
        if info != '':
            if request.form['button'] == 'Save':
                a = select_condition_or_description(name)(info)
                db.session.add(a)
                db.session.commit()
            elif request.form['button'] == 'Update':
                a = db.session.query(select_condition_or_description(name)).get(data)
                a.info = info
                db.session.commit()
    data = db.session.query(select_condition_or_description(name)).all()
    return render_template('test_condition_and_description.html', data=data, name=name)


if __name__ == '__main__':
    login_manager = LoginManager()
    login_manager.init_app(app)
    app.run()
