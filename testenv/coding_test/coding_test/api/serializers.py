#writing script to convert data to json
from rest_framework  import serializers
from blog.models import Post

# use this command in manage.py shell to get list of all fields in Post model
#  from blog.models import Post;[f.name for f in Post._meta.get_fields()]

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=('id', 'cover', 'cover2', 'slug', 'text', 'quote', 'quote_name', 'l_heading', 'l_heading_text', 's_heading', 's_heading_text', 'text2', 'title', 'author', 'category', 'created_date', 'tag_1', 'tag_2', 'tag_3')