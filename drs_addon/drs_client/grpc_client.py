import grpc
import logging

from .drs_protocol_pb2 import *
from .drs_protocol_pb2_grpc import *

def main():
    thread = GRPCClient(None)
    thread.start()


class GRPCClient():
    stub = None
    sessionKey = ""
    id = 1

    @classmethod
    def Connect(cls, addr, id):
        print("Starting grpc client")
        cls.id = id
        channel =  grpc.insecure_channel(addr)
        cls.stub = JobsManagerStub(channel)
        logging.info(f"Performing connection request")
        response = cls.stub.ConnectRequest(Request(UserId=cls.id, SessionKey="", Body="fsdf"))
        print(f"client received: {response.Success}, {response.Body}" )
        cls.sessionKey = response.Body
        logging.info(f"Response: \n\tSuccess:{response.Success}, \n\tBody:{response.Body}")

    @classmethod
    def Render(cls):
        logging.info(f"Performing render request")
        response = cls.stub.RenderRequest(Request(UserId=cls.id, SessionKey=cls.sessionKey, Body="fsdf"))
        print(f"Response: \n\tSuccess:{response.Success}, \n\tBody:{response.Body}" )
        logging.info(f"Response: \n\tSuccess:{response.Success}, \n\tBody:{response.Body}")
        return response

    @classmethod
    def JobPoll(cls, uuid):
        logging.info(f"Performing jobpoll request")
        response = cls.stub.JobPollRequest(Request(UserId=cls.id, SessionKey=cls.sessionKey, Body=uuid))
        print(f"Response: \n\tSuccess:{response.Success}, \n\tBody:{response.Body}, \n\tFragmentIndex:{response.FragmentIndexes}" )
        logging.info(f"Response: \n\tSuccess:{response.Success}, \n\tBody:{response.Body}, \n\tFragmentIndex:{response.FragmentIndexes}")
        return response

    @classmethod
    def ReportProgress(cls, fragmentIndex):
        logging.info(f"Performing reportprogress request")
        response = cls.stub.ReportProgressRequest(Request(UserId=cls.id, SessionKey=cls.sessionKey, Body=fragmentIndex))
        print(f"Response: \n\tSuccess:{response.Success}, \n\tBody:{response.Body}" )
        logging.info(f"Response: \n\tSuccess:{response.Success}, \n\tBody:{response.Body}")
        return response

if __name__ == "__main__":
    main()