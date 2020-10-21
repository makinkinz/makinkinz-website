from .models import Tags
def add_variable_to_context(request):
    tags = Tags.objects.all()
    return {
        'tags': tags
    }