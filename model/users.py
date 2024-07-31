from flask_sqlalchemy import SQLAlchemy
from config.config import DB_URL
from datetime import datetime
from pytz import timezone
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def json(self):
        return {'id': self.id, 'username': self.username, 'email': self.email}


class IotDevice(db.Model):
    __tablename__ = 'iot_device_data'

    id = db.Column(db.Integer, primary_key=True)
    device = db.Column(db.String(255))
    status = db.Column(db.String(120))
    isActive = db.Column(db.String(1))
    event = db.Column(db.String(120))
    device_no = db.Column(db.String(120))
    created_at = db.Column(db.TIMESTAMP(
        True), default=datetime.now(timezone('Asia/Bangkok')))
    updated_at = db.Column(db.TIMESTAMP(True), default=datetime.now(
        timezone('Asia/Bangkok')), onupdate=datetime.now(timezone('Asia/Bangkok')))
    created_by = db.Column(db.String(120))
    updated_by = db.Column(db.String(120))

    def json(self):
        return {'id': self.id, 'device': self.device, 'status': self.status, 'isActive': self.isActive, 'event': self.event, 'device_no': self.device_no, 'created_at': self.created_at, 'updated_at': self.updated_at, 'created_by': self.created_by, 'updated_by': self.updated_by}
