# Role Management for Online Booking App

class Role:
    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions

# Define roles
staff_member = Role('Staff Member', ['view_own_bookings'])
team_leader = Role('Team Leader', ['manage_team_bookings'])
administrator = Role('Administrator', ['full_access'])
