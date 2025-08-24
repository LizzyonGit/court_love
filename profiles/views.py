from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """
    Displays the user's profile.
    **Context**

    ``form``
        Instance of :form:`profiles.UserProfileForm`.
    ``orders``
        All orders by the user.
    ``on_profile_page``
        Boolean value which is true in template,
        to adapt toast message on profile page
    ``profile``
        Instance of :model:`profiles.UserProfile`

    **Template**

    :template:`profiles/profile.html`
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            # reload page so removebutton dissappears or appears when it should
            return redirect('profile')
        else:
            messages.error(request, 'Update failed. Ensure the form is valid.')

    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all().order_by('-order_date',)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
        'profile': profile,

    }

    return render(request, template, context)


def order_history(request, order_number):
    """
    Displays a previous order confirmation
    for the user
    **Context**
    ``order``
        A single order by the user.
    ``from_profile_page``
        Boolean value which is true for this request,
        to display button to go back to profile

    **Template**

    :template:`checkout/checkout_success.html`
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
