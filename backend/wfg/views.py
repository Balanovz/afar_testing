from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import WFG

@api_view(['GET'])
def getData(request):
    wfg = WFG()
    response = {
        'connection_status': wfg.connection_status,
        'ouput': wfg.get_output(),
        'amplitude': wfg.get_amplitude(),
        'shape': wfg.get_shape(),
        'frequency': wfg.get_frequency(),
    }
    return Response(response)
