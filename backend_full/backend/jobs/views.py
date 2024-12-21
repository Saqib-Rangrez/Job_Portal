from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Job
from .serializers import JobSerializer

# Viewset for listing and handling job CRUD operations
class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

# POST API to add new job posting
@api_view(['POST'])
def add_job(request):
    data = request.data

    # Convert strings to Python booleans
    work_from_home = data['work_from_home'] == "TRUE"
    is_remote = data['is_remote'] == "TRUE"
    is_highlighted = data['is_highlighted'] == "TRUE"
    easy_apply = data['easy_apply'] == "TRUE"
    willing_to_sponsor = data['willing_to_sponsor'] == "TRUE"

    new_job = Job.objects.create(
        title=data['title'],
        company_name=data['company_name'],
        job_location=data['job_location'],
        posted_date=data['posted_date'],
        employment_type=data['employment_type'],
        is_remote=is_remote,
        work_from_home=work_from_home,
        salary=data['salary'],
        url=data['url'],
        summary=data['summary'],
        details_page_url=data['details_page_url'],
        is_highlighted=is_highlighted,
        workplace_types=data['workplace_types'],
        easy_apply=easy_apply,
        employer_type=data['employer_type'],
        company_page_url=data['company_page_url'],
        location=data['location'],
        willing_to_sponsor=willing_to_sponsor,
    )
    return Response(JobSerializer(new_job).data)
