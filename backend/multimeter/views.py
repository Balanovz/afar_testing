from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Multimeter

@api_view(['GET'])
def getData(request):
    multimeter = Multimeter()
    response = {
        'connection_status': multimeter.connection_status,
        'voltage_ac': multimeter.get_voltage_ac(),
        'voltage_dc': multimeter.get_voltage_dc(),
        'current_ac': multimeter.get_current_ac(),
        'current_dc': multimeter.get_current_dc(),
    }
    return Response(response)
