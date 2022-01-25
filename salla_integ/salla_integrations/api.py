import frappe
import requests


@frappe.whitelist()
def get_orders():
    url_ = 'https://api.salla.dev/admin/v2/orders'
    Headers = {"Authorization": "Bearer 3f9cbf084412abe59769ca07d9c40191a6ff440bc561717388c8a3a6aea0b105" }
    # r_page = requests.get(url = url_, headers=Headers)
    # get_page_data = r_page.json()
    # last_page = get_page_data["pagination"]["totalPages"]
    # for x in range(150,157):
    #     data = {'page': x}
    r = requests.get(url = url_, headers=Headers)
    get_order_data = r.json()
    for order_data in get_order_data["data"]:
        already_listed = frappe.db.sql(""" select name from `tabSales Order` where order_id=%s """,(str(order_data["id"])))
        if already_listed:
            pass
        else:
            new_doc = frappe.new_doc("Sales Order")
            new_doc.order_id = order_data["id"]
            new_doc.reference_id = order_data["reference_id"]
            new_doc.total = order_data["total"]["amount"]
            for item in order_data["items"]:
                row = new_doc.append("items", {})
                row.item_name = item["name"]
                row.qty = item["quantity"]
            # new_doc.save()
            new_doc.submit()
				
@frappe.whitelist()			
def get_customers():
    url_ = 'https://api.salla.dev/admin/v2/customers'
    Headers = {"Authorization": "Bearer 3f9cbf084412abe59769ca07d9c40191a6ff440bc561717388c8a3a6aea0b105" }
    # r_page = requests.get(url = url_, headers=Headers)
    # get_page_data = r_page.json()
    # last_page = get_page_data["pagination"]["totalPages"]
    # for x in range(200,225):
    #     data = {'page': x}
    r = requests.get(url = url_, headers=Headers)
    get_employee_data = r.json()
    for emp_data in get_employee_data["data"]:
        already_customer = frappe.db.sql(""" select name from `tabCustomer` where customer_id=%s """,(str(emp_data["id"])))
        if already_customer:
            pass
        else:
            new_doc = frappe.new_doc("Customer")
            new_doc.customer_id = emp_data["id"]
            new_doc.customer_name = emp_data["first_name"] +" " + emp_data["last_name"]
            new_doc.mobile_code = emp_data["mobile_code"]
            new_doc.mobile = emp_data["mobile"]
            new_doc.gender = emp_data["gender"]
            new_doc.city = emp_data["city"]
            new_doc.country = emp_data["country"]
            new_doc.country_code = emp_data["country_code"]
            if emp_data["birthday"]:
                new_doc.birthday = str(emp_data["birthday"]["date"]).split(' ')[0]
            if emp_data["location"]:
                new_doc.geolocation = emp_data["location"]
            new_doc.save()
