import datetime
from app.auth.v1.models.user_models import UserModels
from flask import request
from flask_restful import Resource
from flask_restful.reqparse import RequestParser

parser = RequestParser()


parser.add_argument("username", type=str, required=True,
                    help="Please input your name")
parser.add_argument("password", type=str, required=True,
                    help="Please input your password")
parser.add_argument("task", type=str, required=True,
                    help="Please input an task")
parser.add_argument("worktime", type=int, required=True,
                    help="Please input worktime")
parser.add_argument("breaktime", type=int, required=True,
                    help="Please input your breaktime")




class User(Resource):
    """
    User endpoints
    """

    def post(self):
        """
        Register a user endpoint
        """
        args = parser.parse_args()
        args = request.get_json()
        
        username = args["username"]
        password = args["password"]
        task = args["task"]
        worktime = args["worktime"]
        breaktime = args["breaktime"]
        

        newUser = UserModels(username,password,task,worktime,breaktime,datetime)
        newUser.save_user()

        return {
            "message": "User register successfully",
            "user": newUser.__dict__
        }, 201

    def get(self):
        pass
   