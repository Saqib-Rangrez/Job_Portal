from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)  # Essential field, no null allowed
    company_name = models.CharField(max_length=255)  # Essential field, no null allowed
    company_logo_url = models.URLField(blank=True, null=True)
    company_logo_url_optimized = models.URLField(blank=True, null=True)
    job_location = models.CharField(max_length=255, blank=True, null=True, default='Unknown Location')  # Allows null
    posted_date = models.DateTimeField(blank=True, null=True)  # Allows null
    employment_type = models.CharField(max_length=100, blank=True, null=True)  # Allows null
    is_remote = models.BooleanField(default=False)
    work_from_home = models.BooleanField(default=False)
    salary = models.CharField(max_length=100, blank=True, null=True)  # Allows null
    url = models.URLField(blank=True, null=True, default='http://example.com')  # Allows null
    summary = models.TextField(blank=True, null=True, default='No description available')  # Allows null
    details_page_url = models.URLField(blank=True, null=True, default='http://example.com/details')  # Allows null
    is_highlighted = models.BooleanField(default=False)
    workplace_types = models.CharField(max_length=100, blank=True, null=True, default='Remote')  # Allows null
    easy_apply = models.BooleanField(default=False)
    employer_type = models.CharField(max_length=100, blank=True, null=True, default='Unknown')  # Allows null
    company_page_url = models.URLField(blank=True, null=True, default='http://example.com/company')  # Allows null
    location = models.CharField(max_length=255, blank=True, null=True, default='Unknown Location')  # Allows null
    willing_to_sponsor = models.BooleanField(default=False)

    def __str__(self):
        return self.title
