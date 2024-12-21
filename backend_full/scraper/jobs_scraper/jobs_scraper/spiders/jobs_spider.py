import scrapy
import json
import requests
from urllib.parse import urlencode

class JobSpider(scrapy.Spider):
    name = 'job_spider'

    # Define the start URL (API endpoint to get job data)
    start_urls = ['https://job-search-api.svc.dhigroupinc.com/v1/dice/jobs/search']

    def start_requests(self):
        headers = {
            'x-api-key': '1YAt0R9wBg4WfsF9VB2778F5CHLAPMVW3WAZcKd8',  # Required API key for authentication
        }

        # Common parameters
        params = {
            'q': 'Software',
            'countryCode2': 'US',
            'radius': '30',
            'radiusUnit': 'mi',
            'page': '1',
            'pageSize': '20',
            'facets': 'employmentType|postedDate|workFromHomeAvailability|workplaceTypes|employerType|easyApply|isRemote|willingToSponsor',
            'filters.workplaceTypes': 'Remote',
            'filters.employmentType': 'CONTRACTS',
            'filters.postedDate': 'ONE',
            'currencyCode': 'USD',
            'fields': 'id|jobId|guid|summary|title|postedDate|modifiedDate|jobLocation.displayName|detailsPageUrl|salary|clientBrandId|companyPageUrl|companyLogoUrl|companyLogoUrlOptimized|positionId|companyName|employmentType|isHighlighted|score|easyApply|employerType|workFromHomeAvailability|workplaceTypes|isRemote|debug|jobMetadata|willingToSponsor',
            'culture': 'en',
            'recommendations': 'true',
            'interactionId': '0',
            'fj': 'true',
            'includeRemote': 'true',
        }

        # Loop through pages and generate requests
        for page in range(1, 6):  # Loop over 5 pages, adjust the range as needed
            params['page'] = page
            url_with_params = self.start_urls[0] + '?' + urlencode(params)

            yield scrapy.Request(
                url=url_with_params,
                method="GET",
                headers=headers,
                callback=self.parse,
            )

    # def parse(self, response):
    #     # Check if the response is valid and parse the JSON response
    #     if response.status == 200:
    #         data = json.loads(response.text)  # Parse the JSON response

    #         # Extract job data
    #         jobs = data.get('jobs', [])

    #         for job in jobs:
    #             job_data = {
    #                 'title': job.get('title'),
    #                 'company_name': job.get('companyName'),
    #                 'job_location': job.get('jobLocation', {}).get('displayName'),
    #                 'posted_date': job.get('postedDate'),
    #                 'employment_type': job.get('employmentType'),
    #                 'salary': job.get('salary'),
    #                 'url': job.get('url'),
    #                 'summary': job.get('summary'),
    #                 'details_page_url': job.get('detailsPageUrl'),
    #                 'work_from_home': job.get('workFromHomeAvailability', False),
    #                 'company_logo_url': job.get('companyLogoUrl'),
    #                 'company_logo_url_optimized': job.get('companyLogoUrlOptimized'),
    #                 'is_remote': job.get('isRemote', False),
    #                 'is_highlighted': job.get('isHighlighted', False),
    #                 'workplace_types': job.get('workplaceTypes', ''),
    #                 'easy_apply': job.get('easyApply', False),
    #                 'employer_type': job.get('employerType', ''),
    #                 'company_page_url': job.get('companyPageUrl', ''),
    #                 'location': job.get('location', ''),
    #                 'willing_to_sponsor': job.get('willingToSponsor', False),
    #             }

    #             # Now send this job data to your Django backend via a POST request
    #             post_url = 'http://localhost:8000/api/add_job/'  # Your Django API endpoint
    #             headers = {'Content-Type': 'application/json'}

    #             # Send a POST request to insert the scraped data into the database
    #             response = requests.post(post_url, json=job_data, headers=headers)

    #             # Check the response from Django to confirm the data was successfully inserted
    #             if response.status_code == 201:
    #                 self.log(f"Successfully posted job: {job['title']}")
    #             else:
    #                 self.log(f"Failed to post job: {job['title']}, Status Code: {response.status_code}")

    #         # Pagination (if applicable)
    #         next_page = data.get('nextPage', None)
    #         if next_page:
    #             yield scrapy.Request(next_page, callback=self.parse)
    #     else:
    #         self.logger.error(f"Failed to retrieve data: {response.status}")


    def parse(self, response):
    # Debugging: print raw response
        # print("Response Text:", response.text)

        try:
            data = response.json()  # Use .json() instead of json.loads(response.text)
            print("Data DIRECT:", data)
            # jobs = data.get('jobs', [])
            # print("Jobs Found:", jobs)  # Print out jobs to see if they exist in the response
            
            for job in data.get('data', []):
                job_data = {
                    'title': job.get('title'),
                    'company_name': job.get('companyName'),
                    'job_location': job.get('jobLocation', {}).get('displayName'),
                    'posted_date': job.get('postedDate'),
                    'employment_type': job.get('employmentType'),
                    'salary': job.get('salary'),
                    'url': job.get('url'),
                    'summary': job.get('summary'),
                    'details_page_url': job.get('detailsPageUrl'),
                    'work_from_home': job.get('workFromHomeAvailability', False),
                    'company_logo_url': job.get('companyLogoUrl'),
                    'company_logo_url_optimized': job.get('companyLogoUrlOptimized'),
                    'is_remote': job.get('isRemote', False),
                    'is_highlighted': job.get('isHighlighted', False),
                    'workplace_types': job.get('workplaceTypes', ''),
                    'easy_apply': job.get('easyApply', False),
                    'employer_type': job.get('employerType', ''),
                    'company_page_url': job.get('companyPageUrl', ''),
                    'location': job.get('location', ''),
                    'willing_to_sponsor': job.get('willingToSponsor', False),
                }
                
                print("Job Data:", job_data)

                # Now send this job data to your Django backend via a POST request
                post_url = 'http://localhost:8000/api/add_job/'  # Your Django API endpoint
                headers = {'Content-Type': 'application/json'}

                # Send a POST request to insert the scraped data into the database
                response = requests.post(post_url, json=job_data, headers=headers)

                # Check the response from Django to confirm the data was successfully inserted
                if response.status_code == 201:
                    self.log(f"Successfully posted job: {job['title']}")
                else:
                    self.log(f"Failed to post job: {job['title']}, Status Code: {response.status_code}")
        
            
        except Exception as e:
            self.log(f"Error while parsing response: {e}")
