from .models import Testimonial

def testimonials_context(request):
    return {
        'testimonials': Testimonial.objects.all()
    }
