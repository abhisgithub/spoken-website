from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Count, Sum, Min
from django.db.models import Q
from events.models import *
from cms.sortable import *
from events.filters import TrainingFilter
from events.views import get_page
import datetime
from django.http import Http404

# Create your views here.
def maphome(request):
    states = State.objects.all().exclude(name = 'Uncategorized')
    context = {
        'states': states
    }
    return render(request, 'statistics/templates/maphome.html', context)

def get_state_info(request, code):
    state = None
    try:
        state = State.objects.get(code = code)
        #academic_list = AcademicCenter.objects.filter(state = state).values_list('id')
        resource_centers = AcademicCenter.objects.filter(state = state, resource_center = 1).count()
        #workshop_details = Training.objects.filter(academic_id__in = academic_list, status = 4).aggregate(Sum('participant_counts'), Count('id'), Min('trdate'))
        workshop_details = Training.objects.filter(Q(status = 4) | (Q(training_type = 0) & Q(status__gt = 1) & Q(trdate__lte = datetime.date.today())), participant_counts__gt=0, academic__state_id = state.id).aggregate(Sum('participant_counts'), Count('id'), Min('trdate'))
        context = {
            'state': state,
            'workshops': workshop_details['id__count'],
            'participants': workshop_details['participant_counts__sum'],
            'resource_centers': resource_centers,
            'from_date': workshop_details['trdate__min']
        }
        return render(request, 'statistics/templates/get_state_info.html', context)
    except Exception, e:
        print e
        return HttpResponse('<h4 style="margin: 30px;">Permission Denied!</h4>')

def training(request, slug = None):
    """ Organiser index page """
    user = request.user
    collectionSet = None
    state = None
    participant_count = 0
    if slug:
        state = State.objects.filter(slug=slug)
        if not State.objects.filter(slug=slug):
            raise PermissionDenied()
        collectionSet = Training.objects.filter(Q(status = 4) | (Q(training_type = 0) & Q(status__gt = 1) & Q(trdate__lte = datetime.date.today())), academic__in = AcademicCenter.objects.filter(state__in = State.objects.filter(slug=slug)), participant_counts__gt=0).order_by('-trdate')
    else:
        collectionSet = Training.objects.filter(Q(status = 4) | (Q(training_type = 0) & Q(status__gt = 1) & Q(trdate__lte = datetime.date.today())),  participant_counts__gt=0).order_by('-trdate')
    header = {
        1: SortableHeader('#', False),
        2: SortableHeader('academic__state', True, 'State'),
        3: SortableHeader('academic__city', True, 'City'),
        4: SortableHeader('academic', True, 'Institution'),
        5: SortableHeader('foss', True, 'FOSS'),
        6: SortableHeader('organiser__user', True, 'Organiser'),
        7: SortableHeader('trdate', True, 'Date'),
        8: SortableHeader('Participants', False),
        9: SortableHeader('Action', False)
    }
    
    raw_get_data = request.GET.get('o', None)
    collection = get_sorted_list(request, collectionSet, header, raw_get_data)
    ordering = get_field_index(raw_get_data)
    
    # find state id
    state_id = None
    if 'academic__state' in request.GET and request.GET['academic__state'] and slug:
        # todo
        pass
    elif 'academic__state' in request.GET and request.GET['academic__state']:
        state = State.objects.get(id=request.GET['academic__state'])
    
    collection = TrainingFilter(request.GET, queryset=collection, state=state)
    # find participants count
    participant_count = collection.qs.aggregate(Sum('participant_counts'))
    context = {}
    context['form'] = collection.form
    
    page = request.GET.get('page')
    collection = get_page(collection, page)
    context['collection'] = collection
    context['header'] = header
    context['ordering'] = ordering
    context['state'] = slug
    context['participant_count'] = participant_count
    return render(request, 'statistics/templates/training.html', context)
    
def training_participant(request, wid=None):
    user = request.user
    if wid:
        try:
            wc = Training.objects.get(id=wid)
        except:
            raise PermissionDenied()
        if wc.status == 4:
            workshop_mdlusers = TrainingAttendance.objects.using('default').filter(training_id = wid, status__gt = 0).values_list('mdluser_id')
        else:
            workshop_mdlusers = TrainingAttendance.objects.using('default').filter(training_id = wid).values_list('mdluser_id')
        ids = []
        for wp in workshop_mdlusers:
            ids.append(wp[0])
            
        wp = MdlUser.objects.using('moodle').filter(id__in=ids)
        context = {
            'collection' : wp,
            'wc' : wc,
        }
        return render(request, 'statistics/templates/participant.html', context)
