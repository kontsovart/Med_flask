import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.schema import MetaData

from models import *


class TestQuery(unittest.TestCase):

    engine = create_engine('postgresql://postgres:password@localhost/med_flask')
    Session = sessionmaker(bind=engine, expire_on_commit=False)
    session = Session()
    try:
        def setUp(self):
            db.Model.metadata.drop_all(self.engine)
            db.Model.metadata.create_all(self.engine)
            self.condition = Condition('end')
            self.session.add(self.condition)

            self.description = Description(info='Opisanie')
            self.session.add(self.description)
            self.session.commit()

            self.state1 = State(transitions=[], prev_states=[], description=1)
            self.session.add(self.state1)
            self.session.commit()

            self.transition1 = Transition(next_state=1, condition=3)
            self.session.add(self.transition1)
            self.session.commit()

            self.transition2 = Transition(next_state=2, condition=4)
            self.session.add(self.transition2)
            self.session.commit()

            self.state2 = State(transitions=[self.session.query(Transition).filter_by(id=1).first(),
                                             self.session.query(Transition).filter_by(id=2).first()],
                                prev_states=[], description=1)
            self.session.add(self.state2)
            self.session.commit()

        def tearDown(self):
            # db.session.remove()

            # db.drop_all()
            self.session.close_all()

        def test_Condition(self):
            expected = [self.condition]
            result = self.session.query(Condition).filter_by().all()
            print(result, expected)
            self.assertEqual(result, expected)

        def test_State(self):
            expected = [self.state1, self.state2]
            result = self.session.query(State).all()
            print(result, expected)
            self.assertEqual(result, expected)
    except:
        session.rollback()


if __name__ == '__main__':
    unittest.main(verbosity=True)
