from queue_implimentation import LinkedQueue

def simulate_customer_service():

    service_queue = LinkedQueue()

    customers = ["Mahmoud", "Nour", "Hamzi", "David", "Luna"]

    print("--- Customer Arrivals ---")
    
    for customer in customers:
        service_queue.enqueue(customer)
        print(f"Arriving: {customer}")

    print("\n--- Customer Service ---")

    while not service_queue.is_empty():
        served_customer = service_queue.dequeue()
        print(f"Serving: {served_customer}")
    else:
        print("\nDone all customers served.")


if __name__ == "__main__":
    simulate_customer_service()
