"""User registration model and schema"""
from marshmallow import Schema, fields


class UserSchema(Schema):
    """User registration schema"""
    name = fields.String(required=True)
    age = fields.Integer(required=True)
    user_id = fields.String(dump_only=True)
    process_status = fields.String(dump_only=True)


class User:
    """User model"""
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.age = kwargs.get('age', 0)
        self.user_id = kwargs.get('user_id', '')
        self.process_status = kwargs.get('process_status', 'none')

    def __repr__(self):
        return f'<{self.name}:{self.age}-{self.user_id}>'

    def get_user_id(self):
        """Return user ID of this user"""
        return self.user_id

user_schema = UserSchema()
users_schema = UserSchema(many=True)
