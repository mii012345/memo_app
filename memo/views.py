from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import HttpResponseRedirect

from .models import Memo

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'memo/index.html'
    context_object_name = 'latest_memo_list'

    def get_queryset(self):
        memos = Memo.objects.order_by('-pub_date')[:5]
        memo_list = []
        for memo in memos:
            if memo.delete is None:
                memo_list.append(memo)
                pubdate = str(memo.pub_date)
                year = pubdate.split()[0].split('-')[0]
                month = pubdate.split()[0].split('-')[1]
                date = pubdate.split()[0].split('-')[2]
                hour = pubdate.split()[1].split(':')[0]
                minu = pubdate.split()[1].split(':')[1]
                newdate = year+'年'+month+'月'+date+'日 '+hour+':'+minu
                memo.pub_date = newdate
        return memo_list

class DetailView(generic.DetailView):
    model = Memo
    template_name = 'memo/detail.html'

def insert(request):
    title = request.POST['title']
    memotype = request.POST['type']
    memo = request.POST['memo']
    mobject = Memo(memo_title=title, memo_type=memotype, memo_text=memo, pub_date=timezone.now())
    mobject.save()
    return HttpResponseRedirect(reverse('memo:index'))

def edit(request, memo_id):
    memo = get_object_or_404(Memo, pk=memo_id)
    try:
        selected_memo = memo.objects.get(pk=memo_id)
    except (KeyError, Memo.DoesNotExist):
        return HttpResponseRedirect(reverse('memo:index'))
    else:
        selected_memo.memo_text = request.POST['memo']
        selected_memo.save()
        return HttpResponseRedirect(reverse('memo:detail', args=(memo.id,)))

def delete(request, memo_id):
    memo = get_object_or_404(Memo, pk=memo_id)
    memo.delete = timezone.now()
    memo.save()
    return HttpResponseRedirect(reverse('memo:index'))
