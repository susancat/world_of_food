from django.core.urlresolvers import reverse
from django.test import TestCase

class HomePageTests(TestCase):
    def test_home_using_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'breakfast/home.html')

    def test_home_has_title(self):
        response = self.client.get(reverse('home'))
        self.assertIn(b'<title>', response.content)
        self.assertIn(b'</title>', response.content)


class AboutPageTests(TestCase):
        
    def test_about_contains_create_message(self):
        response = self.client.get(reverse('about'))
        self.assertIn(b'You also get a chance to engage with our community of users', response.content)
        
    def test_about_using_template(self):
        response = self.client.get(reverse('about'))

        self.assertTemplateUsed(response, 'breakfast/about.html')
        
        
        
class ModelTests(TestCase):

    def setUp(self):
        try:
            from populate_food import populate
            populate()
        except ImportError:
            print('The module populate_food does not exist')
        except NameError:
            print('The function populate() does not exist or is not correct')
        except:
            print('Something went wrong in the populate() function :-(')
        
        
    def get_continent(self, continent_name_slug):
        
        from breakfast.models import Continent
        try:                  
            con = Continent.objects.get(slug=continent_name_slug)
        except Continent.DoesNotExist:    
            con = None
        return con


class ViewTests(TestCase):

    def setUp(self):
        try:
            from forms import RecipeForm
            from forms import UserProfileForm
            from forms import ContactForm

        except ImportError:
            print('The module forms does not exist')
        except NameError:
            print('The form does not exist or is not correct')
        except:
            print('Something else went wrong :-(')

    pass