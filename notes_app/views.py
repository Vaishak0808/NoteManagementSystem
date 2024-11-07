from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm
from django.core.paginator import Paginator

@login_required
def note_list(request):
    notes = Note.objects.filter(user=request.user).order_by('-created_at')
    paginator = Paginator(notes, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'notes/note_list.html', {'page_obj': page_obj})

@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user  
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})

@login_required
def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form})

@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    note.delete()
    return redirect('note_list')
