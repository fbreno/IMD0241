from spyne import Application, ServiceBase, Integer, Unicode, rpc
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class TemperatureConverterService(ServiceBase):
    @rpc(Integer, Unicode, Unicode, _returns=Unicode)
    def converter_temperatura(ctx, temperatura, unidade_origem, unidade_destino):
        if unidade_origem == 'C':
           if unidade_destino == 'F':
               return TemperatureConverterService.celcius_to_fahrenheit(ctx, temperatura, unidade_origem, unidade_destino)
           elif unidade_destino == 'K':
               return TemperatureConverterService.celcius_to_kelvin(ctx, temperatura, unidade_origem, unidade_destino)
        elif unidade_origem == 'F':
                if unidade_destino == 'C':
                    return TemperatureConverterService.fahrenheit_to_celcius(ctx, temperatura, unidade_origem, unidade_destino)
                elif unidade_destino == 'K':
                    return TemperatureConverterService.fahrenheit_to_kelvin(ctx, temperatura, unidade_origem, unidade_destino)
        elif unidade_origem == 'K':
            if unidade_destino == 'F':
                return TemperatureConverterService.kelvin_to_fahrenheit(ctx, temperatura, unidade_origem, unidade_destino)
            elif unidade_destino == 'C':
                return TemperatureConverterService.kelvin_to_celcius(ctx, temperatura, unidade_origem, unidade_destino)
        else:
            return "Conversão não suportada"
    
    def celcius_to_fahrenheit(ctx, temperatura, unidade_origem, unidade_destino):
        if unidade_origem == 'C' and unidade_destino == 'F':
            temperatura_convertida = temperatura * 9 / 5 + 32
            return f"{temperatura} {unidade_origem} = {temperatura_convertida} {unidade_destino}"
        else:
            return "Conversão não suportada"
    def celcius_to_kelvin(ctx, temperatura, unidade_origem, unidade_destino):
        if unidade_origem == 'C' and unidade_destino == 'K':
            temperatura_convertida = temperatura + 273.15
            return f"{temperatura} {unidade_origem} = {temperatura_convertida} {unidade_destino}"
        else:
            return "Conversão não suportada"
    def fahrenheit_to_celcius(ctx, temperatura, unidade_origem, unidade_destino):
        if unidade_origem == 'F' and unidade_destino == 'C':
            temperatura_convertida = (temperatura - 32) * 5 / 9
            return f"{temperatura} {unidade_origem} = {temperatura_convertida} {unidade_destino}"
        else:
            return "Conversão não suportada"
    def fahrenheit_to_kelvin(ctx, temperatura, unidade_origem, unidade_destino):
        if unidade_origem == 'F' and unidade_destino == 'K':
            temperatura_convertida = (temperatura + 459.67) * 5 / 9
            return f"{temperatura} {unidade_origem} = {temperatura_convertida} {unidade_destino}"
        else:
            return "Conversão não suportada"
    def kelvin_to_celcius(ctx, temperatura, unidade_origem, unidade_destino):
        if unidade_origem == 'K' and unidade_destino == 'C':
            temperatura_convertida = temperatura - 273.15
            return f"{temperatura} {unidade_origem} = {temperatura_convertida} {unidade_destino}"
        else:
            return "Conversão não suportada"
    def kelvin_to_fahrenheit(ctx, temperatura, unidade_origem, unidade_destino):
        if unidade_origem == 'K' and unidade_destino == 'F':
            temperatura_convertida = temperatura * 9 / 5 - 459.67
            return f"{temperatura} {unidade_origem} = {temperatura_convertida} {unidade_destino}"
        else:
            return "Conversão não suportada"

application = Application([TemperatureConverterService], tns='tempconv', in_protocol=Soap11(validator='lxml'), out_protocol=Soap11())

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    wsgi_app = WsgiApplication(application)
    server = make_server('0.0.0.0', 8000, wsgi_app)
    server.serve_forever()