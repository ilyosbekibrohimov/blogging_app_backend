from concurrent import futures
import grpc
import time

# import generated files
from generated_files import calculator_pb2
from generated_files import calculator_pb2_grpc

# import calculator
import calculator


class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def SquareRoot(self, request, context):
        response = calculator_pb2.Number()
        response.value = calculator.square_root(request.value)

        return response

    def Calculator(self, request, context):
        response = calculator_pb2.MyCalc.Response()
        response.result = calculator.addition(request.number1, request.number2)

        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)

print('Starting server. Listening on port 50051')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop()
