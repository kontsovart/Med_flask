from app_config import db
# python3 manage.py migrate - for start migrations to db
# python3 manage.py upgrade for commit updates


class Condition(db.Model):
    __tablename__ = 'condition'

    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.String(300), nullable=False)

    def __init__(self, info):
        self.info = info

    def __repr__(self):
        return '<Condition {}>'.format(self.info)


class Description(db.Model):
    __tablename__ = 'description'

    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.String(300), nullable=False)

    def __init__(self,info):
        self.info = info

    def __repr__(self):
        return '<Descriprion {}>'.format(self.info)


class Transition(db.Model):
    __tablename__ = 'transition'

    id = db.Column(db.Integer, primary_key=True)
    # Firstly - commend the row below and run manage.py db migrate and manage.py db update. After this - uncomment this row and run following command again.
    next_state = db.Column(db.Integer)
    db.ForeignKeyConstraint(['next_state'], ["state.id"], use_alter=True, ondelete=True, name='fk_trans_state')
    condition = db.Column(db.Integer)  # , db.ForeignKey("condition.id"))
    db.ForeignKeyConstraint(['condition'], ['condition.id'], use_alter=True, name='fk_trans_cond', ondelete=True)

    def __init__(self, next_state, condition):
        self.next_state = next_state
        self.condition = condition

    def __repr__(self):
        return '<Transition ({}, {}, {})>'.format(self.id, self.condition, self.next_state)


prev_state_table = db.Table('prev_state_table', db.Model.metadata,
    db.Column('prev_states_id', db.Integer, db.ForeignKey('state.id'), primary_key=True),
    db.Column('prev_state_id', db.Integer, db.ForeignKey('state.id'), primary_key=True),
)

transition_state_table = db.Table('transition_state_table', db.Model.metadata,
    db.Column('transition_id', db.Integer, db.ForeignKey('transition.id'), primary_key=True),
    db.Column('state_id', db.Integer, db.ForeignKey('state.id'), primary_key=True),
)


class State(db.Model):
    __tablename__ = 'state'

    id = db.Column(db.Integer, primary_key=True)
    transitions = db.relationship("Transition", secondary=transition_state_table,
                                  backref='trans')

    prev_states = db.relationship("State", secondary=prev_state_table,
                                  primaryjoin=id == prev_state_table.c.prev_states_id,
                                  secondaryjoin=id == prev_state_table.c.prev_state_id,
                                  backref="prev",
                                  single_parent=True,
                                  cascade="all, delete-orphan",
                                  # post_update=True,
                                  passive_deletes=True)
    description = db.Column(db.Integer)
    db.ForeignKeyConstraint(['description'], ['description.id'], use_alter=True, name='fk_desc_state', ondelete=True)

    def __init__(self, transitions, prev_states, description):
        self.transitions = transitions
        self.prev_states = prev_states
        self.description = description

    def __repr__(self):
        return '<State ({}, {}, {}, {})>'.format(self.id, self.description, self.transitions, self.prev_states)
