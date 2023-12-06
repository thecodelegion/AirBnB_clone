from datetime import datetime
import uuid

class BaseModel:
     """
    Base class for other models.

    Attributes:
        id (str): A unique identifier in hexadecimal format.
        created_at (datetime): The date and time when the instance was created (in UTC).
        updated_at (datetime): The date and time when the instance was last updated (in UTC).
    """

    id = uuid.uuid4().hex # Assign unique id upon creation of a new instance
    created_at = datetime.utcnow() # Assign current time when an instance was created
    updated_at = created_at

    def __str__(self):
        """
        Return a string representation of the instance.

        Returns:
            str: A string containing the class name, unique ID, and attribute dictionary.
        """
        return f"{self.__class__} ({self.id}) {{{self.__dict__}}}".format(self=self)

    def save(self):
        """
        Update the 'updated_at' attribute with the current UTC time.
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
         """
        Convert the instance to a dictionary.

        Returns:
            dict: A dictionary containing the instance's attributes.
        """
        d = self.__dict__
        d['__class__'] = self.__class__
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        return d