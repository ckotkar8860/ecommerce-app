from django.shortcuts import render, redirect
from django.views import View
from .models import Order
from .forms import OrderForm

class OrderListView(View):
    def get(self, request):
        orders = Order.objects.all()
        return render(request, 'orders/order_list.html', {'orders': orders})

class OrderCreateView(View):
    def get(self, request):
        form = OrderForm()
        return render(request, 'orders/order_form.html', {'form': form})

    def post(self, request):
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
        return render(request, 'orders/order_form.html', {'form': form})

class OrderDetailView(View):
    def get(self, request, pk):
        order = Order.objects.get(pk=pk)
        return render(request, 'orders/order_detail.html', {'order': order})