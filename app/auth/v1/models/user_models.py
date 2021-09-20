class UserModels():
    """
    Class for the user operations

    """
    users = {}

    def __init__(self, username, password, task,worktime,breaktime,datetime,) -> None:
        """
        Initialize the user models
        """
        self.id = len(UserModels.users) + 1
        self.username = username
        self.password = password
        self.task = task
        self.worktime = worktime
        self.breaktime = breaktime
        self.time = datetime.now().strftime("%H:%M")
        

    def save_user(self):
        """
        Method to register a user instance and update the data structure
        """
        user_record = dict(
            id=self.id,
            username=self.username,
            password=self.password,
            task=self.task,
            worktime=self.worktime,
            breaktime=self.breaktime,
            time=self.time
            
        )
        self.users.update({
            self.id: user_record
        })
    