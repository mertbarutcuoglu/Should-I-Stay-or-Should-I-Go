from firebase import Firebase
class FirebaseLogger:
        
    config = {
    "apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "storageBucket": ""
    }
    firebase = Firebase(config)
    db = firebase.database()

    current_num_people = 0
    total_num_people = 0
    did_someone_leave = False

    def update_database(self): 
        data = {
            "current_people": self.current_num_people,
            "total_people": self.total_num_people                
        }
        self.db.child("users").child(self.active_user).update(data)


    def update(self, current_num_people):
        if not self.did_someone_leave:
            if self.total_num_people < current_num_people:
                self.total_num_people = current_num_people
            elif current_num_people < self.current_num_people:
                self.did_someone_leave = True
            self.current_num_people = current_num_people
            self.update_database()
            print('database updated')
            return 

        if self.did_someone_leave:
            if current_num_people  > self.current_num_people:
                self.did_someone_leave = False
                num_new_people = current_num_people - self.current_num_people
                self.total_num_people += num_new_people
                self.did_someone_leave = False
            self.current_num_people = current_num_people
            self.update_database()
            print('database updated')
            return

    def set_active_user(self, active_user):
        self.active_user = active_user



