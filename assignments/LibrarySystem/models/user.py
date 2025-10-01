class User:
    def __init__(self, user_id, name, email, borrowed_items=None):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.borrowed_items = borrowed_items or []

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "borrowed_items": self.borrowed_items,
        }

    @staticmethod
    def from_dict(data):
        return User(
            user_id=data["user_id"],
            name=data["name"],
            email=data.get("email", "unknown@example.com"),
            borrowed_items=data.get("borrowed_items", [])
        )
    
