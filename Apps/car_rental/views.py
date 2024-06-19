from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib import messages
from .forms import UploadFileForm
from .models import Contract
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from openpyxl import Workbook


# Create your views here.

class UploadFileView(LoginRequiredMixin, FormView):
    login_url = 'login'
    template_name = 'upload.html'
    form_class = UploadFileForm
    success_url = '/'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        query = self.request.GET.get('q')
        contract_list = Contract.get_filtered_contracts(query)

        paginator = Paginator(contract_list, 20)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        context['query'] = query
        context['columns'] = [
            'Nombres', 'Apellidos', 'Número de documento', 'Inicio de contrato', 'Cuota semanal',
            'Marca del auto', 'Modelo del auto', 'Placa del auto'
        ]

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            if form.save():
                messages.success(request, 'Archivo cargado correctamente')
                return super().get(request, *args, **kwargs)
            else:
                messages.error(request, form.errors['file'][0])
        else:
            messages.error(request, form.errors['file'][0])

        return redirect('upload_file')


def export_to_excel(request):
    query = request.GET.get('q')
    columns = request.POST.getlist('columns')
    if not columns:
        messages.error(request, 'Debe seleccionar al menos una columna')
        return redirect('upload_file')

    contract_list = Contract.get_filtered_contracts(query)
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="contracts.xlsx"'

    workbook = Workbook()
    sheet = workbook.active
    sheet.append(columns)

    column_to_property_map = {
        'Nombres': 'client.first_name',
        'Apellidos': 'client.last_name',
        'Número de documento': 'client.document',
        'Inicio de contrato': 'start_date',
        'Cuota semanal': 'weekly_fee',
        'Marca del auto': 'car.brand',
        'Modelo del auto': 'car.model',
        'Placa del auto': 'car.plaque'
    }

    for contract in contract_list:
        row = []
        for column in columns:
            property_name = column_to_property_map[column]
            properties = property_name.split('.')
            value = contract
            for prop in properties:
                value = getattr(value, prop)
            row.append(value)
        sheet.append(row)
    workbook.save(response)
    return response
