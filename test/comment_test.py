from app.models import Comment, User
from app import db

def setUp(self):
  self.user_P = User(username = 'Albunus',password = '25845600Al', email = 'alybtush3@gmail.com')
  self.new_comment = Comment(id=1,user_id=10,comment='Pretty pitch', pitch_id = 12 )

def tearDown(self):
  Comment.query.delete()
  User.query.delete()
        
def test_check_instance_variables(self):
  self.assertEquals(self.new_comment.id,1)
  self.assertEquals(self.new_comment.user_id,10)
  self.assertEquals(self.new_comment.comment,'Pretty pitch')
  self.assertEquals(self.new_comment.pitch_id,12)
        
def test_save_comment(self):
  self.new_comment.save_comment()
  self.assertTrue(len(Comment.query.all())>0)
        
def test_get_comment_by_id(self):
  self.new_comment.save_comment()
  got_comments = Comment.get_comments(12345)
  self.assertTrue(len(got_comments) == 1)