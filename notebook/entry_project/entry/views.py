from django.shortcuts import render, get_object_or_404, redirect
from .models import Entry
from .forms import EntryForm

def entry_list(request):
    entries = Entry.objects.all()
    return render(request, 'entry/entry_list.html', {'entries': entries})

def entry_detail(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    return render(request, 'entry/entry_detail.html', {'entry': entry})

def entry_create(request):
    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('entry_list')
    else:
        form = EntryForm()
    return render(request, 'entry/entry_form.html', {'form': form})

def entry_update(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('entry_detail', pk=pk)
    else:
        form = EntryForm(instance=entry)
    return render(request, 'entry/entry_form.html', {'form': form})

def entry_delete(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect('entry_list')
    return render(request, 'entry/entry_confirm_delete.html', {'entry': entry})
