import pandas as pd

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Employee


class ExcelUploadAPIView(APIView):

    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        return render(request, "upload.html")

    def post(self, request):

        excel_file = request.FILES['file']

        df = pd.read_excel(excel_file)

        excel_emp_ids = []

        for _, row in df.iterrows():

            emp_id = str(row['Emp ID'])
            excel_emp_ids.append(emp_id)

            Employee.objects.update_or_create(
                emp_id=emp_id,
                defaults={
                    'emp_name': row['Emp Name'],
                    'email': row['Employee email ID'],
                    'experience': row['Total Experience'],
                    'primary_skill': row['Primary Skills'],
                    'secondary_skill': row['Secondary Skills'],
                    'cm_name': row['CM Name'],
                    'profile_status': row['Profile Status'],
                    'customer': row['Customer'],
                    'date_shared': row['Date Shared'],
                    'project_owner': row['Project Owner']
                }
            )

        Employee.objects.exclude(emp_id__in=excel_emp_ids).delete()

        return Response({
            "message": "Excel Synced Successfully"
        })