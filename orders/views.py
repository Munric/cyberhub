from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm
from services.models import Service

def create_order(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.service = service
            order.save()
            return redirect('order_success', order_id=order.id)  # ✅ redirect here
    else:
        form = OrderForm()

    return render(request, 'orders/create_order.html', {
        'form': form,
        'service': service
    })


def order_success(request):
    return render(request, 'orders/success.html')