import unittest
from app.models import Post, User, Comments
from app import db

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.new_comment = Comments(comment_content = 'content')
        db.session.add(self.new_comment)
        db.session.commit()
        
    def tearDown(self):
        Comments.query.delete()
        Post.query.delete()
        User.query.delete()
        db.session.commit()

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comments.query.all())>0)

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment_content, 'content')

    def test_get_comment_by_id(self):
        self.new_comment.save_comment()
        comment = Comments.get_comment(1)
        self.assertEquals(self.new_comment.comment_content, 'content')
