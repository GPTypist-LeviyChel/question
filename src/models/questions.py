from tortoise import fields, models
from src.enums.topic import QuestionTopic


class Question(models.Model):
    id = fields.UUIDField(pk=True)
    topic = fields.CharEnumField(QuestionTopic, max_length=20, null=False)
    text = fields.TextField(max_length=500, null=False)
    image_url = fields.TextField(max_length=500, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.text
