from rest_framework.generics import ListAPIView, RetrieveAPIView
from catalogue.models.archive import Archive
from catalogue.serializers.website.archive import ArchiveSerializer

class ArchiveListView(ListAPIView):
    template_name = "archive/archive_list.html"
    queryset = Archive.objects.all()
    serializer_class = ArchiveSerializer


class ArchiveDetailView(RetrieveAPIView):
    template_name = "archive/archive_detail.html"
    queryset = Archive.objects.all()
    serializer_class = ArchiveSerializer