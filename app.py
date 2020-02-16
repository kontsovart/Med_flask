from app_config import *
from models import *
# from database import db_session

@app.route('/')
def hello():
    conn = db.engine.connect()
    s = db.select([State])
    res = conn.execute(s)
    qq = db.session.query(State).filter_by(id=52).one()
    print(qq)
    return f"Hello World!{qq}"


#@app.route('/<name>')
#def hello_name(name):
#    st = Transition(next_state=68, condition=Condition.query.filter_by(id=1).first())
#    db.session.add(st)
#    db.session.commit()
#    alex = State(transitions=[Transition.query.filter_by(id=1).first(), Transition.query.filter_by(id=5).first()], description=Description.query.filter_by(id=2).first(), prev_states=[State.query.filter_by(id=65).first(), State.query.filter_by(id=64).first()])
#    # alex = State(id=1, transitions=[], description='SOS', prev_states=[])
#    print(alex)
#    print(alex.transitions)
#    print(alex.prev_states)
#    db.session.add(alex)
#    db.session.commit()
    # Condition.insert().values(info='it works')
#    return "Hello {}!".format(name)

@app.route('/<name>')
def hello_name(name):
    st = db.session.query(State).filter_by(id=19).first()
    print(st)

if __name__ == '__main__':
    app.run()
