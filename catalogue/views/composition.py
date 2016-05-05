from rest_framework.generics import ListAPIView, RetrieveAPIView
from catalogue.models.composition import Composition
from catalogue.serializers.website.composition import CompositionSerializer

class CompositionListView(ListAPIView):
    template_name = "composition/composition_list.html"
    queryset = Composition.objects.all()
    serializer_class = CompositionSerializer


class CompositionDetailView(RetrieveAPIView):
    template_name = "composition/composition_detail.html"
    queryset = Composition.objects.all()
    serializer_class = CompositionSerializer