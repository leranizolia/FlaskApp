import models
from app import db
from models import Post

db.create_all()

p1 = Post(title='First post', body='First post')
p2 = Post(title='Second post!', body='Second post')
p3 = Post(title='Third post, test !', body='Third post')


db.session.add_all([p1, p2, p3])
db.session.commit()




