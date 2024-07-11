from django.shortcuts import render
from django.http import HttpResponse
from .models import Board, Topic, Post
from django.shortcuts import get_object_or_404
from django.views import generic

# Create your views here.

def index(request):
    boards = Board.objects.all()
    return render(request, 'index.html', {'boards': boards})

class TopicListbyBoard(generic.DetailView):
    """
    Generic class-based view for a list of blogs posted by a particular BlogAuthor.
    """
    model = Board
    paginate_by = 5
    template_name ='board/topic_list_by_board.html'
    
    def get_queryset(self):
        """
        Return list of Topic objects by Board (Board id specified in URL)
        """
        id = self.kwargs['pk']
        target_board=get_object_or_404(Board, pk = id)
        return Board.objects.filter(board=target_board)
        
    def get_context_data(self, **kwargs):
        """
        Add Board to context so they can be displayed in the template
        """
        # Call the base implementation first to get a context
        context = super(TopicListbyBoard, self).get_context_data(**kwargs)
        # Get the Topic object from the "pk" URL parameter and add it to the context
        context['topic'] = get_object_or_404(Topic, pk = self.kwargs['pk'])
        return context