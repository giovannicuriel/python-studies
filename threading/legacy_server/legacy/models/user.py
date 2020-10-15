
from marshmallow import Schema, fields

class UserSchema(Schema):
  name = fields.String(required=True)
  age = fields.Integer(required=True)
  user_id = fields.String(dump_only=True)
  process_status = fields.String(dump_only=True)

class User:
  def __init__(self, **kwargs):
    self.name = kwargs.get('name', '')
    self.age = kwargs.get('age', 0)
    self.user_id = kwargs.get('user_id', '')
    self.process_status = kwargs.get('process_status', 'none')

userSchema = UserSchema()
usersSchema = UserSchema(many=True)
