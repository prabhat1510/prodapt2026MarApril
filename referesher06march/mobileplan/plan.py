# ---------------------------------------------
# Plan Class (Data Model)
# ---------------------------------------------
class Plan:

    def __init__(self, plan_id, plan_name, monthly_price, data_limit_gb):
        self.plan_id = plan_id
        self.plan_name = plan_name
        self.monthly_price = monthly_price
        self.data_limit_gb = data_limit_gb

    def __str__(self):
        return f"{self.plan_id} | {self.plan_name} | Price: ₹{self.monthly_price} | Data: {self.data_limit_gb} GB"

