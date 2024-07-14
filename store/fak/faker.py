import factory
from ..models import Category


class MyModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: 'Category {}'.format(n))
    description = factory.Faker('paragraph', nb_sentences=3, variable_nb_sentences=True)
    #category_img = factory.django.ImageField(filename='category_image.jpg')
    created_at = factory.Faker('date_time_this_year', tzinfo=None)
    #user = factory.SubFactory('user_id')  # Assuming MyUserFactory is defined
    #field3 = factory.Faker('random_int', min=1, max=100)

"""     @classmethod
    def create_batch(cls, size, **kwargs):
        return [cls.create(**kwargs) for _ in range(50)] """