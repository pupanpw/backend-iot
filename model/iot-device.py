from flask_sqlalchemy import SQLAlchemy
from config.config import DB_URL

db = SQLAlchemy()


class IotDevice(db.Model):
    __tablename__ = 'iot_device_data'

    id = db.Column(db.Integer, primary_key=True)
    device = db.Column(db.String(255))
    status = db.Column(db.String(120))
    isActive = db.Column(db.String(1))
    event = db.Column(db.String(120))
    created_at = db.Column(db.TIMESTAMP(True))
    updated_at = db.Column(db.TIMESTAMP(True))
    created_by = db.Column(db.String(120))
    updated_by = db.Column(db.String(120))

    def json(self):
        return {'id': self.id, 'device': self.device, 'status': self.status, 'isActive': self.isActive, 'event': self.event, 'created_at': self.created_at, 'updated_at': self.updated_at, 'created_by': self.created_by, 'updated_by': self.updated_by}
