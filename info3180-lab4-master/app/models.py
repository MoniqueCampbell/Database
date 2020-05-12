from . import db
from werkzeug.security import generate_password_hash


class User(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'user'

    user_id = db.Column(db.String(20),primary_key = True)
    First_name = db.Column(db.String(20))
    Last_name = db.Column(db.String(20))
    Password = db.Column(db.String(255))
    Email = db.Column(db.String(80))
    File = db.Column(db.String(50))
    salt = db.Column(db.String(64))
    date_joined = db.Column(db.String(50))

    def __init__(self,user_id,fname,lname,password,email,file,salt,joined):
        self.user_id = user_id 
        self.First_name = fname
        self.Last_name = lname
        self.Password = generate_password_hash(password, method='pbkdf2:sha256')
        self.Email = email
        self.File = file
        self.salt = salt 
        self.date_joined = joined

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.user_id)

class Phone(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'Phone'

    user_id = db.Column(db.String(20),primary_key = True)
    telephone_no = db.Column(db.String(50))

    def __init__(self,user_id,tel):
        self.user_id = user_id
        telephone_no = tel

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.user_id)
    
class Address(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'Address'

    user_id = db.Column(db.String(20),primary_key = True)
    street_name = db.Column(db.String(100))
    city = db.Column(db.String(100))
    country = db.Column(db.String(50))

    def __init__(self,user_id,street,city,country):
        self.user_id = user_id
        self.street_name = street
        self.city = city
        self.country = country 

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.user_id)
class Profile(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'Profile'

    user_id = db.Column(db.String(20),primary_key = True)
    profile_id = db.Column(db.String(20))
    dob = db.Column(db.DateTime())
    gender = db.Column(db.String(50))
    nickname = db.Column(db.String(100))

    def __init__(self,user_id,profile_id,dob,gender,nickname):
        self.user_id = user_id 
        self.profile_id = profile_id
        self.dob = dob
        self.gender = gender
        self.nickname = nickname
        self.File = file
        self.salt = salt 
        self.date_joined = joined

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.user_id)
class Image(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'Image'

    image_id = db.Column(db.String(20),primary_key = True)
    image_name = db.Column(db.String(50))
    directory = db.Column(db.String(100))


    def __init__(self,image_id,image_name,directory):
        self.image_id = image_id 
        self.image_name = image_name
        self.directory = directory 

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.image_id)
class Post(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'Post'

    post_id = db.Column(db.String(20),primary_key = True)
    description = db.Column(db.String(250))

    def __init__(self,post_id,description):
        self.post_id = post_id 
        self.description = description

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.post_id)
class Commnent(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'Comment'

    com_id = db.Column(db.String(20),primary_key = True)
    post_id = db.Column(db.String(20))
    usr_text = db.Column(db.String(250))

    def __init__(self,com_id,post_id,usr_text):
        self.com_id = user_id 
        self.post_id = post_id
        self.usr_text = usr_text

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.com_id)
class Group1(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'Group1'

    group_id = db.Column(db.String(20),primary_key = True)
    group_name = db.Column(db.String(50))

    def __init__(self,group_id,group_name):
        self.group_id = group_id 
        self.group_name = group_name

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.group_id)
class Commented(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'Commented'

    user_id = db.Column(db.String(20),primary_key = True)
    com_id = db.Column(db.String(20))
    post_id = db.Column(db.String(20))
    usr_text = db.Column(db.String(250))
    com_date = db.Column(db.DateTime())
    com_time = db.Column(db.DateTime())

    def __init__(self,user_id,com_id,post_id,usr_text,com_date,com_time):
        self.user_id = user_id 
        self.com_id = com_id
        self.post_id = post_id
        self.usr_text = usr_text
        self.com_date = com_date
        self.com_time = com_time

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.user_id)
class friends_with(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'friends_with'

    user_id = db.Column(db.String(20),primary_key = True)
    friend_id = db.Column(db.String(20))
    group_id = db.Column(db.String(20))

    def __init__(self,user_id,friend_id,group_id):
        self.user_id = user_id 
        self.friend_id = friend_id
        self.group_id = group_id

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.user_id)
class creates(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'creates'

    editor_id = db.Column(db.String(20),primary_key = True)
    group_id = db.Column(db.String(20))
    user_id = db.Column(db.String(20))
    create_date = db.Column(db.DateTime())
    
    def __init__(self,editor_id,group_id,user_id,create_date):
        self.user_id = user_id 
        self.group_id = group_id
        self.editor_id = editor_id
        self.create_date = create_date 

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.editor_id)
class joins (db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'joins'

    user_id = db.Column(db.String(20),primary_key = True)
    group_id = db.Column(db.String(20))
    join_date = db.Column(db.DateTime())

    def __init__(self,user_id,group_id,join_date):
        self.user_id = user_id 
        self.group_id = group_id
        self.join_date = join_date

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.user_id)
class belongs(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'belongs'

    post_id = db.Column(db.String(20),primary_key = True)
    group_id = db.Column(db.String(20))

    def __init__(self,post_id,group_id):
        self.post_id = post_id 
        self.group_id = group_id

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.post_id)
class adds(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'adds'

    image_id = db.Column(db.String(20),primary_key = True)
    user_id = db.Column(db.String(20))

    def __init__(self,image_id,user_id):
        self.image_id = image_id
        self.user_id = user_id 

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.image_id)
class submits(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'submits'
    
    post_id = db.Column(db.String(20,primary_key = True)
    user_id = db.Column(db.String(20))

    def __init__(self,post_id,user_id):
        self.post_id = post_id 
        self.user_id = user_id 

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.post_id)
class Profile_pic(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'profile_pic'

    profile_id = db.Column(db.String(20),primary_key = True)
    image_id = db.Column(db.String(20))

    def __init__(self,profile_id,image_id):
        self.profile_id = profile_id
        self.user_id = user_id 

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.profile_id)
class post_image(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'post_image'
    post_id = db.Column(db.String(20),primary_key = True)
    image_id = db.Column(db.String(20))

    def __init__(self,post_id,image_id):
        self.post_id = post_id
        self.image_id = image_id 

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.post_id)
class register(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'register'

    user_id = db.Column(db.String(20),primary_key = True)
    profile_id = db.Column(db.String(20))

    def __init__(self,user_id,profile_id):
        self.user_id = user_id
        self.profile_id = profile_id

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.user_id)

