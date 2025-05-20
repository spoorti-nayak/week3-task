from django.shortcuts import render

TASKS = {
    'Sunday': 'Plan the week ahead.',
    'Monday': 'Prepare for meetings.',
    'Tuesday': 'Grocery shopping.',
    'Wednesday': 'Workout session.',
    'Thursday': 'Clean the house.',
    'Friday': 'Family movie night.',
    'Saturday': 'Gardening and relaxation.',
}
# Create your views here.

def index(request):
    return render(request, 'index.html', {'days': TASKS.keys()})

def day_task(request, day):
    task = TASKS.get(day)
    return render(request, 'day.html', {'day': day, 'task': task})