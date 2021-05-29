from sqlalchemy import Column, Integer, String, create_engine, Sequence
from sqlalchemy.orm import  declarative_base, sessionmaker


engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Trick(Base):
	__tablename__ = 'tricks'

	id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
	platform = Column(String)
	title = Column(String)
	link = Column(String)
	content = Column(String)

	def __repr__(self):
	 	return "<User(platform='%s', title='%s', link='%s', content='%s')>"%( self.platform, self.title, self.link, self.content)

if __name__ == '__main__':
	t1 = Trick(platform='realpython', title='hdfkjsksd sjgsid sdsk', link='dsjsdvjkv', content='fzigbiuvbsdvbv sivbov obEVI')
	print(t1.platform)