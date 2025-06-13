from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def submit(request):
    return HttpResponse("You submitted data successfully")

def resume_view(request):
    context = {
        'name': 'Ishaan Joshi',
        'email': 'ishaanjoshi75@gmail.com',
        'phone': '+91-7588110220',
        'location': 'Pune, India',
        'profile_summary': 'A passionate data science student with strong programming skills and hands-on experience in web development and machine learning.',
        'education': [
            {'degree': 'B.Sc. Data Science', 'institution': 'Savitribai Phule Pune University', 'year': '2023–2026'},
            {'degree': '12th Grade', 'institution': 'MES Higher Secondary School', 'year': '2023'},
        ],
        'experience': [
            {
                'position': 'Web Development Intern',
                'company': 'Tech Solutions',
                'duration': 'Jan 2025 – Apr 2025',
                'details': [
                    'Built responsive web apps using Django and React',
                    'Integrated REST APIs for dynamic content',
                    'Collaborated with UI/UX team for design improvements',
                ]
            },
            {
                'position': 'Freelancer',
                'company': 'Self-employed',
                'duration': '2023 – Present',
                'details': [
                    'Developed personal projects and tools using Python and JavaScript',
                    'Contributed to GitHub open-source repositories'
                ]
            },
        ],
        'skills': ['Python', 'Django', 'HTML5', 'CSS3', 'JavaScript', 'SQL', 'Git', 'Machine Learning'],
    }
    return render(request, 'index.html', context)