# Database Manager

This module handles all database operations for the Facebook Reply System.

## Features
- User management and authentication
- Message logging and storage
- Reply history tracking
- Analytics and statistics

## Database Schema

### Users Table
- user_id (Primary Key)
- username
- email
- created_at
- updated_at

### Messages Table
- message_id (Primary Key)
- user_id (Foreign Key)
- message_text
- message_type (comment/message)
- received_at
- replied (boolean)

### Replies Table
- reply_id (Primary Key)
- message_id (Foreign Key)
- reply_text
- sent_at
- status (success/failed)

## Usage

```python
from database import DatabaseManager

db = DatabaseManager()
db.save_message(user_id, message_text)
db.get_pending_messages()
```