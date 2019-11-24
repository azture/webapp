import time, uuid

from orm import Model, SringField, BooleanField, FloatField, TextField

def next_id():
    return '%015d%s000' % (int(time.time()*1000), uuid.uuid4().hex)

class User(Model):
    __table__ = 'users'

    id = stringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = SringField(ddl='varchar(50)')
    passwd = SringField(ddl='varchar(50)')
    admin = BooleanField()
    name = SringField(ddl='varchar(500)')
    image = SringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time)


class Blog(Model):
    __table__ = 'blogs'

    id = stringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = SringField(ddl='varchar(50)')
    user_name = SringField(ddl='varchar(50)')
    user_image = SringField(ddl='varchar(500)')
    name = SringField(ddl='varchar(50)')
    summary = SringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)


class Comment(Model):
    __table__ = 'comments'
    id = stringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = SringField(ddl='varchar(50)')
    user_id = SringField(ddl='varchar(50)')
    user_name = SringField(ddl='varchar(50)')
    user_image = SringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)
