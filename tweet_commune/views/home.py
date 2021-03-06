from django.views.generic import TemplateView

from tweet_commune.models.log_entry import LogEntry
from tweet_commune.models.submission import Submission


class HomeView(TemplateView):
    """
    Landing page view
    """

    template_name = "tweet_commune/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['queue_length'] = Submission.queue.length()
        context['log_entries'] = LogEntry.LogManager.top(3)
        context['is_up'] = LogEntry.LogManager.is_up()
        return context
