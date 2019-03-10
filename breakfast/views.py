
from django.shortcuts import render
from breakfast.models import Continent
from breakfast.models import Recipe
#from breakfast.forms import UserForm


def home(request):
    return render(request, 'breakfast/home.html', {})


def about(request):
    return render(request, 'breakfast/about.html', {})


def contact_us(request):
    return render(request, 'breakfast/contact_us.html', {})


def sign_in(request):
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Your Breakfast account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
    """
    return render(request, 'breakfast/sign_in.html', {})


def sign_up(request):
    return render(request, 'breakfast/sign_up.html', {})


def my_account(request):
    return render(request, 'breakfast/my_account.html', {})


def continent_page(request, continent_name_slug):
    
    context_dict = {}

    try:
        continent = Continent.objects.get(slug=continent_name_slug)
        recipe = Recipe.objects.filter(continent=continent)

        context_dict['recipe'] = recipe
        context_dict['continent'] = continent
    except Continent.DoesNotExist:
        context_dict['category'] = None
        context_dict['recipe'] = None

    return render(request, 'breakfast/continent_page.html', context_dict)


def add_recipe(request):
    form = RecipeForm()

    # A HTTP POST?
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            # Now that the category is saved
            # We could give a confirmation message
            # But since the most recent category added is on the index page
            # Then we can direct the user back to the index page.
            return home(request)
        else:
            # The supplied form contained errors -
            # just print them to the terminal.
            print(form.errors)
    # Will handle the bad form, new form, or no form supplied cases.
    # Render the form with error messages (if any).
    return render(request, 'breakfast/recipe_page.html', {'form': form})


def recipe_page(request, recipe_name_slug):

    context_dict = {}

    try:
        recipe = Recipe.object.get(slug=recipe_name_slug)
        continent = Recipe.object.get(continent)
        description = Recipe.object.get(description)
        ingredients = Recipe.object.get(ingredients)

        context_dict['recipe'] = recipe
        context_dict['continent'] = continent
        context_dict['description'] = description
        context_dict['ingredients'] = ingredients
    except Recipe.DoesNotExist:
        context_dict['recipe'] = None
        context_dict['continent'] = None
        context_dict['description'] = None
        context_dict['ingredients'] = None
        
    return render(request, 'breakfast/recipe_page.html', context_dict)
   

