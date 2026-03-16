# ---------------------------------------------
# Plan Manager Class
# ---------------------------------------------
from planexceptions import InvalidPlanException, PlanNotFoundException
from plan import Plan
class PlanManager:

    def __init__(self):
        # dictionary to store plans
        self.plans = {}

    # -----------------------------------------
    # Add Plan
    # -----------------------------------------
    def add_plan(self, plan_id, plan_name, monthly_price, data_limit_gb):

        if monthly_price <= 0:
            raise InvalidPlanException("Price must be positive")

        if data_limit_gb < 0:
            raise InvalidPlanException("Data limit cannot be negative")

        if plan_id in self.plans:
            raise InvalidPlanException("Plan ID must be unique")

        plan = Plan(plan_id, plan_name, monthly_price, data_limit_gb)

        self.plans[plan_id] = plan

        print("Plan added successfully.")

    # -----------------------------------------
    # Update Plan Price
    # -----------------------------------------
    def update_price(self, plan_id, new_price):

        if plan_id not in self.plans:
            raise PlanNotFoundException("Plan not found")

        if new_price <= 0:
            raise InvalidPlanException("Price must be positive")

        plan = self.plans[plan_id]
        plan.monthly_price = new_price

        print("Plan price updated successfully.")

    # -----------------------------------------
    # Retrieve Plan
    # -----------------------------------------
    def get_plan(self, plan_id):

        if plan_id not in self.plans:
            raise PlanNotFoundException("Plan not found")

        return self.plans[plan_id]

    # -----------------------------------------
    # List Plans Cheaper Than Given Price
    # -----------------------------------------
    def list_cheaper_plans(self, price):

        result = []

        for plan in self.plans.values():
            if plan.monthly_price < price:
                result.append(plan)

        return result

    # -----------------------------------------
    # Find Highest Data Plan
    # -----------------------------------------
    def find_best_data_plan(self):

        if len(self.plans) == 0:
            return None

        best_plan = None

        for plan in self.plans.values():

            if best_plan is None or plan.data_limit_gb > best_plan.data_limit_gb:
                best_plan = plan

        return best_plan

    # -----------------------------------------
    # Show All Plans
    # -----------------------------------------
    def show_all_plans(self):

        if len(self.plans) == 0:
            print("No plans available.")
            return

        print("\nAvailable Plans")

        for plan in self.plans.values():
            print(plan)


    # ---------------------------------------------
    # Reporting Functions
    # ---------------------------------------------
    def show_cheaper_plans(manager):

        price = float(input("Enter price limit: "))

        plans = manager.list_cheaper_plans(price)

        print("\nPlans cheaper than", price)

        if len(plans) == 0:
            print("No plans found.")
            return

        for plan in plans:
            print(plan)


    def show_best_data_plan(manager):

        plan = manager.find_best_data_plan()

        if plan:
            print("\nHighest Data Plan:")
            print(plan)
        else:
            print("No plans available.")