import pandas as pd
from django import forms
from datetime import datetime

from Apps.car_rental.models import Car, Contract, Client


class UploadFileForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control', 'accept': '.xlsx, .csv'}))

    def is_valid(self):
        file = self.files['file']

        if file.name.split('.')[-1] not in ['xlsx', 'csv']:
            self.add_error('file', 'El archivo debe ser del tipo .xlsx o .csv')
            return False

        if not file.size > 0:
            return False

        df = pd.read_excel(file, engine='openpyxl') if file.name.split('.')[-1] == 'xlsx' else \
            (file.seek(0), pd.read_csv(file))[1]

        if df.empty:
            self.add_error('file', 'El archivo no tiene datos')
            return False

        if not all(col in df.columns for col in
                   ['Nombres', 'Apellidos', 'Número de documento', 'Inicio de contrato', 'Cuota semanal',
                    'Marca del auto', 'Modelo del auto', 'Placa del auto']):
            self.add_error('file', 'El archivo no tiene las columnas correctas')
            return False
        return True

    def save(self):
        if not self.is_valid():
            return None

        file = self.files['file']

        df = pd.read_excel(file, engine='openpyxl') if file.name.split('.')[-1] == 'xlsx' else \
            (file.seek(0), pd.read_csv(file))[1]

        for index, row in df.iterrows():
            try:
                car = Car.objects.get_or_create(
                    brand=row['Marca del auto'],
                    model=row['Modelo del auto'],
                    plaque=row['Placa del auto']
                )[0]
                client = Client.objects.get_or_create(
                    first_name=row['Nombres'],
                    last_name=row['Apellidos'],
                    document=row['Número de documento']
                )[0]
                Contract.objects.create(
                    client=client,
                    car=car,
                    start_date=datetime.strptime(row['Inicio de contrato'], '%Y-%m-%d'),
                    weekly_fee=row['Cuota semanal']
                )

            except Exception as e:
                self.add_error('file', f'Error en la fila {index + 2}: {str(e)}')
                return False

        return True
